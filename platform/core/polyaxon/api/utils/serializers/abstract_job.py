from rest_framework import fields, serializers

from api.utils.serializers.job_resources import JobResourcesSerializer


class JobSerializer(serializers.ModelSerializer):
    cpu = fields.DictField(allow_null=True)
    memory = fields.DictField(allow_null=True)
    gpu = fields.DictField(allow_null=True)
    tpu = fields.DictField(allow_null=True)
    resources = JobResourcesSerializer(read_only=True)

    class Meta:
        fields = ('image', 'resources', 'cpu', 'memory', 'gpu', 'tpu')
        extra_kwargs = {
            'cpu': {'write_only': True},
            'memory': {'write_only': True},
            'gpu': {'write_only': True},
            'tpu': {'write_only': True}}

    @staticmethod
    def _has_resources(validated_data):
        cpu = validated_data['cpu']
        memory = validated_data['memory']
        gpu = validated_data['gpu']
        tpu = validated_data['tpu']
        if cpu is None and memory is None and gpu is None and tpu is None:
            return False
        return True

    @staticmethod
    def _get_resources(validated_data):
        cpu = validated_data['cpu']
        memory = validated_data['memory']
        gpu = validated_data['gpu']
        tpu = validated_data['tpu']
        return {'cpu': cpu, 'memory': memory, 'gpu': gpu, 'tpu': tpu}

    def _create_resources(self, validated_data):
        if self._has_resources(validated_data):
            resources = JobResourcesSerializer(data=self._get_resources(validated_data))
            resources.is_valid(raise_exception=True)
            return resources.save()
        return None

    def _update_resources(self, resources_instance, validated_data):
        if self._has_resources(validated_data):
            resources = JobResourcesSerializer(instance=resources_instance,
                                               data=self._get_resources(validated_data))
            resources.is_valid(raise_exception=True)
            return resources.save()
        return None
