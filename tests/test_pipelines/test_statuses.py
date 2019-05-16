import pytest

from constants.pipelines import OperationStatuses, PipelineStatuses
from tests.base.case import BaseTest


@pytest.mark.pipelines_mark
class TestStatusesTransition(BaseTest):
    def test_pipeline_statuses_transition(self):  # pylint:disable=too-many-branches
        # Cannot transition to `CREATED`
        for status in PipelineStatuses.VALUES:
            assert PipelineStatuses.can_transition(
                status_from=status, status_to=PipelineStatuses.CREATED) is False

        # CREATED -> SCHEDULED
        for status in PipelineStatuses.VALUES:
            can_transition = PipelineStatuses.can_transition(
                status_from=status, status_to=PipelineStatuses.SCHEDULED)
            if status in {PipelineStatuses.CREATED, PipelineStatuses.WARNING}:
                assert can_transition is True
            else:
                assert can_transition is False

        # SCHEDULED -> RUNNING
        for status in PipelineStatuses.VALUES:
            can_transition = PipelineStatuses.can_transition(
                status_from=status, status_to=PipelineStatuses.RUNNING)
            if status in {PipelineStatuses.SCHEDULED, PipelineStatuses.WARNING}:
                assert can_transition is True
            else:
                assert can_transition is False

        # {SCHEDULED, RUNNING} -> FINISHED
        for status in PipelineStatuses.VALUES:
            can_transition = PipelineStatuses.can_transition(
                status_from=status, status_to=PipelineStatuses.FINISHED)
            if status in {PipelineStatuses.CREATED,
                          PipelineStatuses.SCHEDULED,
                          PipelineStatuses.WARNING,
                          PipelineStatuses.RUNNING}:
                assert can_transition is True
            else:
                assert can_transition is False

        # {CREATED, SCHEDULED, RUNNING} -> STOPPED
        for status in PipelineStatuses.VALUES:
            can_transition = PipelineStatuses.can_transition(
                status_from=status, status_to=PipelineStatuses.STOPPED)
            if status in {PipelineStatuses.CREATED,
                          PipelineStatuses.SCHEDULED,
                          PipelineStatuses.WARNING,
                          PipelineStatuses.RUNNING}:
                assert can_transition is True
            else:
                assert can_transition is False

        # {CREATED, SCHEDULED, STOPPED} -> SKIPPED
        for status in PipelineStatuses.VALUES:
            can_transition = PipelineStatuses.can_transition(
                status_from=status, status_to=PipelineStatuses.SKIPPED)
            if status in {PipelineStatuses.CREATED,
                          PipelineStatuses.SCHEDULED,
                          PipelineStatuses.WARNING,
                          PipelineStatuses.STOPPED}:
                assert can_transition is True
            else:
                assert can_transition is False

    def test_operation_statuses_transition(self):  # pylint:disable=too-many-branches
        # Cannot transition to `CREATED`
        for status in OperationStatuses.VALUES:
            assert OperationStatuses.can_transition(
                status_from=status, status_to=OperationStatuses.CREATED) is False

        # {CREATED, RETRYING} -> SCHEDULED
        for status in OperationStatuses.VALUES:
            can_transition = OperationStatuses.can_transition(
                status_from=status, status_to=OperationStatuses.SCHEDULED)
            if status in {OperationStatuses.CREATED,
                          OperationStatuses.RETRYING,
                          OperationStatuses.WARNING}:
                assert can_transition is True
            else:
                assert can_transition is False

        # SCHEDULED -> RUNNING
        for status in OperationStatuses.VALUES:
            can_transition = OperationStatuses.can_transition(
                status_from=status, status_to=OperationStatuses.RUNNING)
            if status in {OperationStatuses.SCHEDULED, OperationStatuses.WARNING}:
                assert can_transition is True
            else:
                assert can_transition is False

        # RUNNING -> SUCCEEDED
        for status in OperationStatuses.VALUES:
            can_transition = OperationStatuses.can_transition(
                status_from=status, status_to=OperationStatuses.SUCCEEDED)
            if status in {OperationStatuses.RUNNING, OperationStatuses.WARNING}:
                assert can_transition is True
            else:
                assert can_transition is False

        # {SCHEDULED, RUNNING} -> FAILED
        for status in OperationStatuses.VALUES:
            can_transition = OperationStatuses.can_transition(
                status_from=status, status_to=OperationStatuses.FAILED)
            if status in {OperationStatuses.SCHEDULED,
                          OperationStatuses.RUNNING,
                          OperationStatuses.WARNING}:
                assert can_transition is True
            else:
                assert can_transition is False

        # ALL_VALUES -> UPSTREAM_FAILED
        for status in OperationStatuses.VALUES:
            can_transition = OperationStatuses.can_transition(
                status_from=status, status_to=OperationStatuses.UPSTREAM_FAILED)
            if status == OperationStatuses.UPSTREAM_FAILED:
                assert can_transition is False
            else:
                assert can_transition is True

        # {CREATED, SCHEDULED, RUNNING} -> STOPPED
        for status in OperationStatuses.VALUES:
            can_transition = OperationStatuses.can_transition(
                status_from=status, status_to=OperationStatuses.STOPPED)
            if status in {OperationStatuses.CREATED,
                          OperationStatuses.SCHEDULED,
                          OperationStatuses.RUNNING,
                          OperationStatuses.WARNING}:
                assert can_transition is True
            else:
                assert can_transition is False

        # {CREATED, SCHEDULED, STOPPED} -> SKIPPED
        for status in OperationStatuses.VALUES:
            can_transition = OperationStatuses.can_transition(
                status_from=status, status_to=OperationStatuses.SKIPPED)
            if status in {OperationStatuses.CREATED,
                          OperationStatuses.SCHEDULED,
                          OperationStatuses.STOPPED,
                          OperationStatuses.WARNING}:
                assert can_transition is True
            else:
                assert can_transition is False

        # {SCHEDULED, RUNNING, FAILED, STOPPED, SKIPPED, RETRYING} -> RETRYING
        for status in OperationStatuses.VALUES:
            can_transition = OperationStatuses.can_transition(
                status_from=status, status_to=OperationStatuses.RETRYING)
            if status in {OperationStatuses.SCHEDULED,
                          OperationStatuses.RUNNING,
                          OperationStatuses.FAILED,
                          OperationStatuses.STOPPED,
                          OperationStatuses.SKIPPED,
                          OperationStatuses.WARNING,
                          OperationStatuses.RETRYING}:
                assert can_transition is True
            else:
                assert can_transition is False
