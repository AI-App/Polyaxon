#!/usr/bin/python
#
# Copyright 2018-2020 Polyaxon, Inc.
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

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    OpenAPI spec version: 1.0.7
    Contact: contact@polyaxon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import polyaxon_sdk
from polyaxon_sdk.api.hub_components_v1_api import HubComponentsV1Api  # noqa: E501
from polyaxon_sdk.rest import ApiException


class TestHubComponentsV1Api(unittest.TestCase):
    """HubComponentsV1Api unit test stubs"""

    def setUp(self):
        self.api = (
            polyaxon_sdk.api.hub_components_v1_api.HubComponentsV1Api()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_create_hub_component(self):
        """Test case for create_hub_component

        Create hub model  # noqa: E501
        """
        pass

    def test_delete_hub_component(self):
        """Test case for delete_hub_component

        Delete hub model  # noqa: E501
        """
        pass

    def test_get_hub_component(self):
        """Test case for get_hub_component

        Get hub model  # noqa: E501
        """
        pass

    def test_list_hub_componebt_names(self):
        """Test case for list_hub_componebt_names

        List hub model names  # noqa: E501
        """
        pass

    def test_list_hub_components(self):
        """Test case for list_hub_components

        List hub models  # noqa: E501
        """
        pass

    def test_patch_hub_component(self):
        """Test case for patch_hub_component

        Patch hub model  # noqa: E501
        """
        pass

    def test_update_hub_component(self):
        """Test case for update_hub_component

        Update hub model  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
