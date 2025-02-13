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

from marshmallow import fields

from polyaxon.schemas.base import BaseCamelSchema, BaseConfig


class OperatorsSchema(BaseCamelSchema):
    tfjob = fields.Bool(allow_none=True)
    pytorchjob = fields.Bool(allow_none=True)
    mpijob = fields.Bool(allow_none=True)
    mxjob = fields.Bool(allow_none=True)
    xgbjob = fields.Bool(allow_none=True)
    sparkjob = fields.Bool(allow_none=True)

    @staticmethod
    def schema_config():
        return OperatorsConfig


class OperatorsConfig(BaseConfig):
    SCHEMA = OperatorsSchema
    REDUCED_ATTRIBUTES = [
        "tfjob",
        "pytorchjob",
        "mpijob",
        "mxjob",
        "xgbjob",
        "sparkjob",
    ]

    def __init__(
        self,
        tfjob=None,
        pytorchjob=None,
        mpijob=None,
        mxjob=None,
        xgbjob=None,
        sparkjob=None,
    ):
        self.tfjob = tfjob
        self.pytorchjob = pytorchjob
        self.mpijob = mpijob
        self.mxjob = mxjob
        self.xgbjob = xgbjob
        self.sparkjob = sparkjob
