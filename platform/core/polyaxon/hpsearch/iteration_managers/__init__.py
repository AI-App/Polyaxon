from hpsearch.iteration_managers.base import BaseIterationManager
from hpsearch.iteration_managers.bayesian_optimization import BOIterationManager
from hpsearch.iteration_managers.hyperband import HyperbandIterationManager
from schemas import SearchAlgorithms


def get_search_iteration_manager(experiment_group):
    if SearchAlgorithms.is_hyperband(experiment_group.search_algorithm):
        return HyperbandIterationManager(experiment_group=experiment_group)
    if SearchAlgorithms.is_bo(experiment_group.search_algorithm):
        return BOIterationManager(experiment_group=experiment_group)

    return BaseIterationManager(experiment_group=experiment_group)
