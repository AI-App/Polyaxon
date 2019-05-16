from hpsearch.exceptions import ExperimentGroupException
from hpsearch.iteration_managers.base import BaseIterationManager
from hpsearch.iteration_managers.logger import logger
from hpsearch.schemas import HyperbandIterationConfig
from schemas import Optimization


class HyperbandIterationManager(BaseIterationManager):
    def get_metric_name(self):
        return self.experiment_group.hptuning_config.hyperband.metric.name

    def create_iteration(self, num_suggestions=0):
        """Create an iteration for the experiment group."""
        from db.models.experiment_groups import ExperimentGroupIteration

        search_manager = self.experiment_group.search_manager
        iteration_config = self.experiment_group.iteration_config

        if iteration_config is None:
            iteration = 0
            bracket_iteration = 0
        else:
            should_reschedule = search_manager.should_reschedule(
                iteration=iteration_config.iteration,
                bracket_iteration=iteration_config.bracket_iteration)
            should_reduce_configs = search_manager.should_reduce_configs(
                iteration=iteration_config.iteration,
                bracket_iteration=iteration_config.bracket_iteration)
            if should_reschedule:
                iteration = iteration_config.iteration + 1
                bracket_iteration = 0
            elif should_reduce_configs:
                iteration = iteration_config.iteration
                bracket_iteration = iteration_config.bracket_iteration + 1
            else:
                raise ValueError(
                    'Hyperband create iteration failed for `{}`, '
                    'could not reschedule ot reduce configs'.format(self.experiment_group.id))

        # Create a new iteration config
        iteration_config = HyperbandIterationConfig(
            iteration=iteration,
            num_suggestions=num_suggestions,
            bracket_iteration=bracket_iteration)
        iteration_config.experiment_ids = []
        return ExperimentGroupIteration.objects.create(
            experiment_group=self.experiment_group,
            data=iteration_config.to_dict())

    def get_reduced_configs(self):
        """Reduce the experiments to restart."""
        iteration_config = self.experiment_group.iteration_config
        if iteration_config is None:
            logger.error(
                'Experiment group `%s` attempt to update iteration, but has no iteration',
                self.experiment_group.id,
                extra={'stack': True})
            return
        search_manager = self.experiment_group.search_manager

        # Get the number of experiments to keep
        n_configs_to_keep = search_manager.get_n_config_to_keep_for_iteration(
            iteration=iteration_config.iteration,
            bracket_iteration=iteration_config.bracket_iteration)

        # Get the last group's experiments metrics
        experiments_metrics = self.experiment_group.iteration_config.experiments_metrics
        if experiments_metrics is None:
            raise ExperimentGroupException()

        # Order the experiments
        reverse = Optimization.maximize(
            self.experiment_group.hptuning_config.hyperband.metric.optimization)
        experiments_metrics = sorted(experiments_metrics, key=lambda x: x[1], reverse=reverse)

        # Keep n experiments
        return [xp[0] for xp in experiments_metrics[:n_configs_to_keep]]

    def reduce_configs(self):
        """Reduce the experiments to restart."""
        experiment_ids = self.get_reduced_configs()
        experiments = self.experiment_group.experiments.filter(id__in=experiment_ids)
        self.create_iteration()
        iteration_config = self.experiment_group.iteration_config
        hptuning_config = self.experiment_group.hptuning_config
        n_resources = self.experiment_group.search_manager.get_resources_for_iteration(
            iteration=iteration_config.iteration)
        resource_value = self.experiment_group.search_manager.get_n_resources(
            n_resources=n_resources, bracket_iteration=iteration_config.bracket_iteration
        )
        resource_name = hptuning_config.hyperband.resource.name
        resource_value = hptuning_config.hyperband.resource.cast_value(resource_value)

        # Check if we need to resume or restart the experiments
        for experiment in experiments:
            declarations = experiment.declarations
            declarations[resource_name] = resource_value
            declarations_spec = {'declarations': declarations}
            specification = experiment.specification.patch(declarations_spec)
            status_message = 'Hyperband iteration: {}, bracket iteration: {}'.format(
                iteration_config.iteration,
                iteration_config.bracket_iteration)

            if hptuning_config.hyperband.resume:
                experiment.resume(
                    declarations=declarations,
                    config=specification.parsed_data,
                    message=status_message)
            else:
                experiment.restart(
                    experiment_group=self.experiment_group,
                    declarations=declarations,
                    config=specification.parsed_data)
