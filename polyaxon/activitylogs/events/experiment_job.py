import activitylogs

from event_manager.events import experiment_job

activitylogs.subscribe(experiment_job.ExperimentJobViewedEvent)
activitylogs.subscribe(experiment_job.ExperimentJobResourcesViewedEvent)
activitylogs.subscribe(experiment_job.ExperimentJobLogsViewedEvent)
activitylogs.subscribe(experiment_job.ExperimentJobStatusesViewedEvent)
