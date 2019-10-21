from rest_framework import fields, serializers

from db.models.nodes import ClusterNode, NodeGPU


class GPUSerializer(serializers.ModelSerializer):
    uuid = fields.UUIDField(format='hex', read_only=True)
    cluster_node = fields.SerializerMethodField()

    class Meta:
        model = NodeGPU
        exclude = ('id', )

    def get_cluster_node(self, obj):
        return obj.cluster_node.uuid.hex


class ClusterNodeSerializer(serializers.ModelSerializer):
    uuid = fields.UUIDField(format='hex', read_only=True)

    class Meta:
        model = ClusterNode
        fields = ('uuid', 'sequence', 'name', 'hostname', 'role', 'memory', 'cpu', 'n_gpus',)


class ClusterNodeDetailSerializer(ClusterNodeSerializer):
    gpus = GPUSerializer(many=True)

    class Meta:
        model = ClusterNode
        exclude = ('id', 'cluster',)
