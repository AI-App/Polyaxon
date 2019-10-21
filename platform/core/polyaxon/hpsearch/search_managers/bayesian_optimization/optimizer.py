from hpsearch.search_managers.bayesian_optimization.acquisition_function import UtilityFunction
from hpsearch.search_managers.bayesian_optimization.space import SearchSpace


class BOOptimizer(object):

    def __init__(self, hptuning_config):
        self.hptuning_config = hptuning_config
        self.n_initial_trials = self.hptuning_config.bo.n_initial_trials
        self.space = SearchSpace(hptuning_config=hptuning_config)
        self.utility_function = UtilityFunction(
            config=hptuning_config.bo.utility_function, seed=hptuning_config.seed)
        self.n_warmup = hptuning_config.bo.utility_function.n_warmup or 5
        self.n_iter = hptuning_config.bo.utility_function.n_iter or 10

    def _maximize(self):
        """ Find argmax of the acquisition function."""
        if not self.space.is_observations_valid():
            return None
        y_max = self.space.y.max()
        self.utility_function.gaussian_process.fit(self.space.x, self.space.y)
        return self.utility_function.max_compute(y_max=y_max,
                                                 bounds=self.space.bounds,
                                                 n_warmup=self.n_warmup,
                                                 n_iter=self.n_iter)

    def add_observations(self, configs, metrics):
        # Turn configs and metrics into data points
        self.space.add_observations(configs=configs, metrics=metrics)

    def get_suggestion(self):
        x = self._maximize()
        return self.space.get_suggestion(x)
