from django.db.models import Count

from db.models.experiments import Experiment

experiments = Experiment.objects.select_related(
    'status',
    'original_experiment',
    'original_experiment__user',
    'original_experiment__project',
    'original_experiment__project__user',
    'original_experiment__experiment_group',
    'original_experiment__experiment_group__project',
    'original_experiment__experiment_group__project__user',
)
experiments = experiments.prefetch_related(
    'user',
    'project',
    'project__user',
    'experiment_group',
    'experiment_group__project',
    'experiment_group__project__user',
    'build_job',
    'build_job__project',
    'build_job__project__user',
)

experiments_details = experiments.annotate(
    Count('jobs', distinct=True)
)

experiments_auditing = Experiment.objects.select_related(
    'status',
)
experiments_auditing = experiments_auditing.prefetch_related(
    'user',
    'project',
    'project__user',
    'experiment_group',
    'experiment_group__project',
    'experiment_group__project__user',
)
