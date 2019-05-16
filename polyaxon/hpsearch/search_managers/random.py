from hpsearch.search_managers.base import BaseSearchAlgorithmManager
from hpsearch.search_managers.utils import get_random_suggestions
from schemas import SearchAlgorithms


class RandomSearchManager(BaseSearchAlgorithmManager):
    """Random search algorithm manager for hyperparameter optimization."""

    NAME = SearchAlgorithms.RANDOM

    def get_suggestions(self, iteration_config=None):
        """Return a list of suggestions based on random search.

        Params:
            matrix: `dict` representing the {hyperparam: hyperparam matrix config}.
            n_suggestions: number of suggestions to make.
        """
        matrix = self.hptuning_config.matrix
        n_suggestions = self.hptuning_config.random_search.n_experiments
        seed = self.hptuning_config.seed
        return get_random_suggestions(matrix=matrix, n_suggestions=n_suggestions, seed=seed)
