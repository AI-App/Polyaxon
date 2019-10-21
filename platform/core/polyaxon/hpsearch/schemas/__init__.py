from hpsearch.schemas.base_iteration import BaseIterationConfig
from hpsearch.schemas.bayesian_optimization import BOIterationConfig
from hpsearch.schemas.hyperband import HyperbandIterationConfig
from schemas import SearchAlgorithms


def get_iteration_config(search_algorithm, iteration=None):
    if SearchAlgorithms.is_hyperband(search_algorithm):
        if not iteration:
            raise ValueError('No iteration was provided')
        return HyperbandIterationConfig.from_dict(iteration)
    if SearchAlgorithms.is_bo(search_algorithm):
        if not iteration:
            raise ValueError('No iteration was provided')
        return BOIterationConfig.from_dict(iteration)
    return BaseIterationConfig.from_dict(iteration)
