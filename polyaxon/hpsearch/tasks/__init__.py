import auditor

from db.getters.experiment_groups import get_running_experiment_group
from event_manager.events.experiment_group import (
    EXPERIMENT_GROUP_BO,
    EXPERIMENT_GROUP_GRID,
    EXPERIMENT_GROUP_HYPERBAND,
    EXPERIMENT_GROUP_RANDOM
)
from hpsearch.tasks import bo, grid, health, hyperband, random  # noqa
from polyaxon.celery_api import celery_app
from polyaxon.settings import HPCeleryTasks, Intervals
from schemas import SearchAlgorithms


@celery_app.task(name=HPCeleryTasks.HP_CREATE, bind=True, max_retries=None, ignore_result=True)
def hp_create(self, experiment_group_id):
    experiment_group = get_running_experiment_group(experiment_group_id=experiment_group_id)
    if not experiment_group and self.request.retries < 2:
        # Schedule another task
        self.retry(countdown=Intervals.EXPERIMENTS_SCHEDULER)
        return

    create(experiment_group)


def create(experiment_group):
    if SearchAlgorithms.is_grid(experiment_group.search_algorithm):
        auditor.record(event_type=EXPERIMENT_GROUP_GRID,
                       instance=experiment_group)
        return grid.create(experiment_group=experiment_group)
    elif SearchAlgorithms.is_random(experiment_group.search_algorithm):
        auditor.record(event_type=EXPERIMENT_GROUP_RANDOM,
                       instance=experiment_group)
        return random.create(experiment_group=experiment_group)
    elif SearchAlgorithms.is_hyperband(experiment_group.search_algorithm):
        auditor.record(event_type=EXPERIMENT_GROUP_HYPERBAND,
                       instance=experiment_group)
        return hyperband.create(experiment_group=experiment_group)
    elif SearchAlgorithms.is_bo(experiment_group.search_algorithm):
        auditor.record(event_type=EXPERIMENT_GROUP_BO,
                       instance=experiment_group)
        return bo.create(experiment_group=experiment_group)
    return None


@celery_app.task(name=HPCeleryTasks.HP_START, ignore_result=True)
def hp_start(experiment_group_id):
    experiment_group = get_running_experiment_group(experiment_group_id=experiment_group_id)
    if not experiment_group:
        return

    start(experiment_group)


def start(experiment_group):
    task = None
    if SearchAlgorithms.is_grid(experiment_group.search_algorithm):
        task = HPCeleryTasks.HP_GRID_SEARCH_START
    elif SearchAlgorithms.is_random(experiment_group.search_algorithm):
        task = HPCeleryTasks.HP_RANDOM_SEARCH_START
    elif SearchAlgorithms.is_hyperband(experiment_group.search_algorithm):
        task = HPCeleryTasks.HP_HYPERBAND_START
    elif SearchAlgorithms.is_bo(experiment_group.search_algorithm):
        task = HPCeleryTasks.HP_BO_START

    if task:
        celery_app.send_task(
            task,
            kwargs={'experiment_group_id': experiment_group.id},
            countdown=1)
