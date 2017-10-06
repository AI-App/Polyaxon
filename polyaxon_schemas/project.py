# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from marshmallow import Schema, fields, post_load

from polyaxon_schemas.base import BaseConfig


class ProjectSchema(Schema):
    name = fields.Str()  # TODO: must be slug
    uuid = fields.UUID(allow_none=True)
    description = fields.Str(allow_none=True)
    is_public = fields.Boolean(allow_none=True)

    class Meta:
        ordered = True

    @post_load
    def make(self, data):
        return ProjectConfig(**data)


class ProjectConfig(BaseConfig):
    SCHEMA = ProjectSchema
    IDENTIFIER = 'project'
    REDUCED_ATTRIBUTES = ['uuid', 'description']

    def __init__(self, name, uuid=None, description=None, is_public=True):
        self.name = name
        self.uuid = uuid
        self.description = description
        self.is_public = is_public
