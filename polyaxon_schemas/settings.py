# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from marshmallow import Schema, fields, post_load, validate

from polyaxon_schemas.base import BaseConfig
from polyaxon_schemas.logging import LoggingSchema, LoggingConfig


class GPUOptionsSchema(Schema):
    gpu_memory_fraction = fields.Float(allow_none=True)
    allow_growth = fields.Bool(allow_none=True)
    per_process_gpu_memory_fraction = fields.Float(allow_none=True)

    class Meta:
        ordered = True

    @post_load
    def make(self, data):
        return GPUOptionsConfig(**data)


class GPUOptionsConfig(BaseConfig):
    IDENTIFIER = 'session'
    SCHEMA = GPUOptionsSchema

    def __init__(self,
                 gpu_memory_fraction=None,
                 allow_growth=True,
                 per_process_gpu_memory_fraction=None):
        self.gpu_memory_fraction = gpu_memory_fraction
        self.allow_growth = allow_growth
        self.per_process_gpu_memory_fraction = per_process_gpu_memory_fraction


class SessionSchema(Schema):
    # To indicate which worker/ps index this session config belongs to
    index = fields.Int(allow_none=True)
    gpu_options = fields.Nested(GPUOptionsSchema, allow_none=True)
    log_device_placement = fields.Bool(allow_none=True)
    allow_soft_placement = fields.Bool(allow_none=True)
    intra_op_parallelism_threads = fields.Int(allow_none=True)
    inter_op_parallelism_threads = fields.Int(allow_none=True)

    class Meta:
        ordered = True

    @post_load
    def make(self, data):
        return SessionConfig(**data)


class SessionConfig(BaseConfig):
    IDENTIFIER = 'session'
    SCHEMA = SessionSchema
    REDUCED_ATTRIBUTES = ['index']

    def __init__(self,
                 index=None,
                 log_device_placement=True,
                 gpu_options=GPUOptionsConfig(),
                 allow_soft_placement=True,
                 intra_op_parallelism_threads=None,
                 inter_op_parallelism_threads=None):
        self.index = index
        self.gpu_options = gpu_options
        self.log_device_placement = log_device_placement
        self.allow_soft_placement = allow_soft_placement
        self.intra_op_parallelism_threads = intra_op_parallelism_threads
        self.inter_op_parallelism_threads = inter_op_parallelism_threads


class ClusterSchema(Schema):
    master = fields.List(fields.Str, allow_none=True)
    worker = fields.List(fields.Str, allow_none=True)
    ps = fields.List(fields.Str, allow_none=True)

    class Meta:
        ordered = True

    @post_load
    def make(self, data):
        return ClusterConfig(**data)


class ClusterConfig(BaseConfig):
    IDENTIFIER = 'cluster'
    SCHEMA = ClusterSchema

    def __init__(self, master=None, worker=None, ps=None):
        self.master = master
        self.worker = worker
        self.ps = ps


class RunSchema(Schema):
    tf_random_seed = fields.Int(allow_none=True)
    save_summary_steps = fields.Int(allow_none=True)
    save_checkpoints_secs = fields.Int(allow_none=True)
    save_checkpoints_steps = fields.Int(allow_none=True)
    keep_checkpoint_max = fields.Int(allow_none=True)
    keep_checkpoint_every_n_hours = fields.Int(allow_none=True)

    session = fields.Nested(SessionSchema, allow_none=True)
    cluster = fields.Nested(ClusterSchema, allow_none=True)

    class Meta:
        ordered = True

    @post_load
    def make(self, data):
        return RunConfig(**data)


class RunConfig(BaseConfig):
    IDENTIFIER = 'run'
    SCHEMA = RunSchema

    def __init__(self,
                 tf_random_seed=None,
                 save_summary_steps=100,
                 save_checkpoints_secs=None,
                 save_checkpoints_steps=None,
                 keep_checkpoint_max=5,
                 keep_checkpoint_every_n_hours=10000,
                 session=None,
                 cluster=None):
        self.tf_random_seed = tf_random_seed
        self.save_summary_steps = save_summary_steps
        self.save_checkpoints_secs = save_checkpoints_secs
        self.save_checkpoints_steps = save_checkpoints_steps
        self.keep_checkpoint_max = keep_checkpoint_max
        self.keep_checkpoint_every_n_hours = keep_checkpoint_every_n_hours
        self.session = session
        self.cluster = cluster


class EnvironmentSchema(Schema):
    n_workers = fields.Int(allow_none=True)
    n_ps = fields.Int(allow_none=True)
    delay_workers_by_global_step = fields.Bool(allow_none=True)
    run_config = fields.Nested(RunSchema, allow_none=True)
    default_worker_config = fields.Nested(SessionSchema, allow_none=True)
    default_ps_config = fields.Nested(SessionSchema, allow_none=True)
    worker_configs = fields.Nested(SessionSchema, many=True, allow_none=True)
    ps_configs = fields.Nested(SessionSchema, many=True, allow_none=True)

    class Meta:
        ordered = True

    @post_load
    def make(self, data):
        return EnvironmentConfig(**data)


class EnvironmentConfig(BaseConfig):
    IDENTIFIER = 'environment'
    SCHEMA = EnvironmentSchema

    def __init__(self,
                 n_workers=0,
                 n_ps=0,
                 delay_workers_by_global_step=False,
                 run_config=None,
                 default_worker_config=None,
                 default_ps_config=None,
                 worker_configs=None,
                 ps_configs=None):
        self.n_workers = n_workers
        self.n_ps = n_ps
        self.delay_workers_by_global_step = delay_workers_by_global_step
        self.run_config = run_config
        self.default_worker_config = default_worker_config
        self.default_ps_config = default_ps_config
        self.worker_configs = worker_configs
        self.ps_configs = ps_configs


class RunTypes(object):
    LOCAL = 'local'
    MINIKUBE = 'minikube'
    KUBERNETES = 'kubernetes'
    AWS = 'aws'

    VALUES = [LOCAL, MINIKUBE, KUBERNETES, AWS]


class SettingsSchema(Schema):
    logging = fields.Nested(LoggingSchema, allow_none=True)
    export_strategies = fields.Str(allow_none=True)
    run_type = fields.Str(allow_none=True,
                          validate=validate.OneOf(RunTypes.VALUES))
    concurrent_experiments = fields.Int(allow_none=True)

    class Meta:
        ordered = True

    @post_load
    def make(self, data):
        return SettingsConfig(**data)


class SettingsConfig(BaseConfig):
    SCHEMA = SettingsSchema
    IDENTIFIER = 'settings'

    def __init__(self,
                 logging=LoggingConfig(),
                 export_strategies=None,
                 run_type=RunTypes.LOCAL,
                 concurrent_experiments=1):
        self.logging = logging
        self.export_strategies = export_strategies
        self.run_type = run_type
        self.concurrent_experiments = concurrent_experiments
