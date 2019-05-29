from hestia.signal_decorators import ignore_raw, ignore_updates

from django.db.models.signals import post_save
from django.dispatch import receiver

import auditor

from db.models.experiment_groups import ExperimentGroupIteration
from events.registry.experiment_group import EXPERIMENT_GROUP_ITERATION


@receiver(post_save,
          sender=ExperimentGroupIteration,
          dispatch_uid="experiment_group_iteration_saved")
@ignore_updates
@ignore_raw
def new_experiment_group_iteration(sender, **kwargs):
    instance = kwargs['instance']
    auditor.record(event_type=EXPERIMENT_GROUP_ITERATION,
                   instance=instance.experiment_group)
