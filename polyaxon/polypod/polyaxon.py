import json

from polypod.tensorflow import TensorflowSpawner
from schemas import TaskType


class PolyaxonSpawner(TensorflowSpawner):

    @staticmethod
    def _get_schedule(task_type):
        if task_type == TaskType.MASTER:
            return 'train_and_evaluate'
        if task_type == TaskType.WORKER:
            return 'train'
        if task_type == TaskType.PS:
            return 'run_std_server'

    def get_pod_command_args(self, task_type, task_idx):
        spec_data = json.dumps(self.spec.parsed_data)
        schedule = self._get_schedule(task_type=task_type)

        args = [
            "from polyaxon.polyaxonfile.local_runner import start_experiment_run; "
            "start_experiment_run('{polyaxonfile}', '{experiment_id}', "
            "'{task_type}', {task_idx}, '{schedule}')".format(
                polyaxonfile=spec_data,
                experiment_id=0,
                task_type=task_type,
                task_idx=task_idx,
                schedule=schedule)]
        return ["python3", "-c"], args
