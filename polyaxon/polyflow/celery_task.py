from billiard.exceptions import SoftTimeLimitExceeded
from hestia.list_utils import to_list

from db.models.operations import OperationRun
from workers.base import PolyaxonTask


class OperationRunDoesNotExist(Exception):
    pass


class OperationRunError(Exception):
    pass


class OperationTask(PolyaxonTask):
    """Base operation celery task with basic logging."""
    _operation_run = None

    def __call__(self, *args, **kwargs):
        try:
            self._operation_run = OperationRun.objects.get(id=kwargs['operation_run_id'])
        except (KeyError, OperationRun.DoesNotExist):
            raise OperationRunDoesNotExist
        self._operation_run.on_run()
        self.max_retries = self._operation_run.operation.max_retries
        # pylint:disable=attribute-defined-outside-init
        self.countdown = self._operation_run.operation.get_countdown(self.request.retries)

        super().__call__(*args, **kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """Update query status and send email notification to a user"""
        super().on_failure(exc, task_id, args, kwargs, einfo)
        if isinstance(exc, OperationRunDoesNotExist):
            return
        self._operation_run.on_failure()

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        super().on_retry(exc, task_id, args, kwargs, einfo)
        self._operation_run.on_retry()

    def on_success(self, retval, task_id, args, kwargs):
        """Send email notification and a file, if requested to do so by a user"""
        super().on_success(retval, task_id, args, kwargs)
        self._operation_run.on_success()


class ClassBasedTask(object):
    """A class based task to use for operation tasks."""
    retry_for = None

    @classmethod
    def run(cls, task_bind, *args, **kwargs):
        retry_for = cls.retry_for or []
        retry_for = to_list(retry_for)
        if SoftTimeLimitExceeded not in retry_for:
            retry_for.append(SoftTimeLimitExceeded)
        try:
            return cls._run(task_bind, *args, **kwargs)
        except tuple(retry_for) as exc:  # pylint:disable=catching-non-exception
            if task_bind.request.retries < task_bind.max_retries:
                raise task_bind.retry(countdown=task_bind.countdown)
            else:
                raise exc  # pylint:disable=raising-non-exception

    @staticmethod
    def _run(task_bind, *args, **kwargs):
        raise NotImplemented  # noqa
