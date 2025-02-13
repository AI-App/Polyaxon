#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import polyaxon_sdk

from marshmallow import fields, validate

from polyaxon.containers.names import MAIN_JOB_CONTAINER
from polyaxon.k8s import k8s_schemas
from polyaxon.polyflow.environment import EnvironmentSchema
from polyaxon.polyflow.init import InitSchema
from polyaxon.polyflow.run.base import BaseRun
from polyaxon.polyflow.run.kinds import V1RunKind
from polyaxon.polyflow.run.resources import V1RunResources
from polyaxon.polyflow.run.utils import DestinationImageMixin
from polyaxon.schemas.base import BaseCamelSchema, BaseConfig
from polyaxon.schemas.fields.swagger import SwaggerField


class JobSchema(BaseCamelSchema):
    kind = fields.Str(allow_none=True, validate=validate.Equal(V1RunKind.JOB))
    environment = fields.Nested(EnvironmentSchema, allow_none=True)
    connections = fields.List(fields.Str(), allow_none=True)
    volumes = fields.List(SwaggerField(cls=k8s_schemas.V1Volume), allow_none=True)
    init = fields.List(fields.Nested(InitSchema), allow_none=True)
    sidecars = fields.List(SwaggerField(cls=k8s_schemas.V1Container), allow_none=True)
    container = SwaggerField(
        cls=k8s_schemas.V1Container,
        defaults={"name": MAIN_JOB_CONTAINER},
        allow_none=True,
    )

    @staticmethod
    def schema_config():
        return V1Job


class V1Job(BaseConfig, BaseRun, DestinationImageMixin, polyaxon_sdk.V1Job):
    """Jobs are used to train machine learning models,
    process a dataset, execute generic tasks and can be used to perform a variety of functions
    from compiling a model to running an ETL operation.

    Args:
        kind: str, should be equal `job`
        environment: [V1Environment](/docs/core/specification/environment/), optional
        connections: List[str], optional
        volumes: List[[Kubernetes Volume](https://kubernetes.io/docs/concepts/storage/volumes/)],
             optional
        init: List[[V1Init](/docs/core/specification/init/)], optional
        sidecars: List[[sidecar containers](/docs/core/specification/sidecars/)], optional
        container: [Kubernetes Container](https://kubernetes.io/docs/concepts/containers/)

    ## YAML usage

    ```yaml
    >>> run:
    >>>   kind: job
    >>>   environment:
    >>>   connections:
    >>>   volumes:
    >>>   init:
    >>>   sidecars:
    >>>   container:
    ```

    ## Python usage

    ```python
    >>> from polyaxon.polyflow import V1Environment, V1Init, V1Job
    >>> from polyaxon.k8s import k8s_schemas
    >>> job = V1Job(
    >>>     environment=V1Environment(...),
    >>>     connections=["connection-name1"],
    >>>     volumes=[k8s_schemas.V1Volume(...)],
    >>>     init=[V1Init(...)],
    >>>     sidecars=[k8s_schemas.V1Container(...)],
    >>>     container=k8s_schemas.V1Container(...),
    >>> )
    ```

    ## Fields

    ### kind

    The kind signals to the CLI, client, and other tools that this component's runtime is a job.

    If you are using the python client to create the runtime,
    this field is not required and is set by default.

    ```yaml
    >>> run:
    >>>   kind: job
    ```

    ### environment

    Optional [environment section](/docs/core/specification/environment/),
    it provides a way to inject pod related information.

    ```yaml
    >>> run:
    >>>   kind: job
    >>>   environment:
    >>>     labels:
    >>>        key1: "label1"
    >>>        key2: "label2"
    >>>      annotations:
    >>>        key1: "value1"
    >>>        key2: "value2"
    >>>      nodeSelector:
    >>>        node_label: node_value
    >>>      ...
    >>>  ...
    ```

    ### connections

    A list of [connection names](/docs/setup/connections/) to resolve for the job.

    <blockquote class="light">
    If you are referencing a connection it must be configured.
    All referenced connections will be checked:

     * If they are accessible in the context of the project of this run

     * If the user running the operation can have access to those connections
    </blockquote>

     After checks, the connections will be resolved and inject any volumes, secrets, configMaps,
    environment variables for your main container to function correctly.

    ```yaml
    >>> run:
    >>>   kind: job
    >>>   connections: [connection1, connection2]
    ```

    ### volumes

    A list of [Kubernetes Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
    to resolve and mount for your jobs.

    This is an advanced use-case where configuring a connection is not an option.

    When you add a volume you need to mount it manually to your container(s).

    ```yaml
    >>> run:
    >>>   kind: job
    >>>   volumes:
    >>>     - name: volume1
    >>>       persistentVolumeClaim:
    >>>         claimName: pvc1
    >>>   ...
    >>>   container:
    >>>     name: myapp-container
    >>>     image: busybox:1.28
    >>>     command: ['sh', '-c', 'echo custom init container']
    >>>     volumeMounts:
    >>>     - name: volume1
    >>>       mountPath: /mnt/vol/path
    ```

    ### init

    A list of [init handlers and containers](/docs/core/specification/init/)
    to resolve for the job.

    <blockquote class="light">
    If you are referencing a connection it must be configured.
    All referenced connections will be checked:

     * If they are accessible in the context of the project of this run

     * If the user running the operation can have access to those connections
    </blockquote>

    ```yaml
    >>> run:
    >>>   kind: job
    >>>   init:
    >>>     - artifacts:
    >>>         dirs: ["path/on/the/default/artifacts/store"]
    >>>     - connection: gcs-large-datasets
    >>>       artifacts:
    >>>         dirs: ["data"]
    >>>       container:
    >>>         resources:
    >>>           requests:
    >>>             memory: "256Mi"
    >>>             cpu: "500m"
    >>>     - container:
    >>>       name: myapp-container
    >>>       image: busybox:1.28
    >>>       command: ['sh', '-c', 'echo custom init container']
    ```

    ### sidecars


    A list of [sidecar containers](/docs/core/specification/sidecars/)
    that will used as sidecars.

    ```yaml
    >>> run:
    >>>   kind: job
    >>>   sidecars:
    >>>     - name: sidecar2
    >>>       image: busybox:1.28
    >>>       command: ['sh', '-c', 'echo sidecar2']
    >>>     - name: sidecar1
    >>>       image: busybox:1.28
    >>>       command: ['sh', '-c', 'echo sidecar1']
    >>>       resources:
    >>>         requests:
    >>>           memory: "128Mi"
    >>>           cpu: "500m"
    ```

    ### container

    The [main Kubernetes Container](https://kubernetes.io/docs/concepts/containers/)
    that will run your experiment training or data processing logic.

    ```yaml
    >>> run:
    >>>   kind: job
    >>>   container:
    >>>     name: tensorflow:2.1
    >>>     init:
    >>>       - connection: my-tf-code-repo
    >>>     command: ["python", "/plx-context/artifacts/my-tf-code-repo/model.py"]
    ```
    """

    SCHEMA = JobSchema
    IDENTIFIER = V1RunKind.JOB
    REDUCED_ATTRIBUTES = [
        "kind",
        "container",
        "environment",
        "init",
        "sidecars",
        "connections",
        "volumes",
    ]

    def get_resources(self):
        return V1RunResources.from_container(self.container)

    def get_all_containers(self):
        return [self.container] if self.container else []

    def get_all_connections(self):
        return self.connections or []

    def get_all_init(self):
        return self.init or []
