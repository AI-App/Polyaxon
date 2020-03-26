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
from polyaxon_sdk.api.run_profiles_v1_api import RunProfilesV1Api  # noqa: E501
from polyaxon_sdk.rest import ApiException


class TestRunProfilesV1Api(unittest.TestCase):
    """RunProfilesV1Api unit test stubs"""

    def setUp(self):
        self.api = polyaxon_sdk.api.run_profiles_v1_api.RunProfilesV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_run_profile(self):
        """Test case for create_run_profile

        Create hub component  # noqa: E501
        """
        pass

    def test_delete_run_profile(self):
        """Test case for delete_run_profile

        Delete hub component  # noqa: E501
        """
        pass

    def test_get_run_profile(self):
        """Test case for get_run_profile

        Get hub component  # noqa: E501
        """
        pass

    def test_list_run_profile_names(self):
        """Test case for list_run_profile_names

        List hub component names  # noqa: E501
        """
        pass

    def test_list_run_profiles(self):
        """Test case for list_run_profiles

        List hub components  # noqa: E501
        """
        pass

    def test_patch_run_profile(self):
        """Test case for patch_run_profile

        Patch hub component  # noqa: E501
        """
        pass

    def test_update_run_profile(self):
        """Test case for update_run_profile

        Update hub component  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
