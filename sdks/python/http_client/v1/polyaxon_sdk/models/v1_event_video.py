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


import pprint
import re  # noqa: F401

import six


class V1EventVideo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "height": "int",
        "width": "int",
        "colorspace": "int",
        "path": "str",
        "content_type": "str",
    }

    attribute_map = {
        "height": "height",
        "width": "width",
        "colorspace": "colorspace",
        "path": "path",
        "content_type": "content_type",
    }

    def __init__(
        self, height=None, width=None, colorspace=None, path=None, content_type=None
    ):  # noqa: E501
        """V1EventVideo - a model defined in Swagger"""  # noqa: E501

        self._height = None
        self._width = None
        self._colorspace = None
        self._path = None
        self._content_type = None
        self.discriminator = None

        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if colorspace is not None:
            self.colorspace = colorspace
        if path is not None:
            self.path = path
        if content_type is not None:
            self.content_type = content_type

    @property
    def height(self):
        """Gets the height of this V1EventVideo.  # noqa: E501

        Height of the video.  # noqa: E501

        :return: The height of this V1EventVideo.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this V1EventVideo.

        Height of the video.  # noqa: E501

        :param height: The height of this V1EventVideo.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this V1EventVideo.  # noqa: E501

        Width of the video.  # noqa: E501

        :return: The width of this V1EventVideo.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this V1EventVideo.

        Width of the video.  # noqa: E501

        :param width: The width of this V1EventVideo.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def colorspace(self):
        """Gets the colorspace of this V1EventVideo.  # noqa: E501


        :return: The colorspace of this V1EventVideo.  # noqa: E501
        :rtype: int
        """
        return self._colorspace

    @colorspace.setter
    def colorspace(self, colorspace):
        """Sets the colorspace of this V1EventVideo.


        :param colorspace: The colorspace of this V1EventVideo.  # noqa: E501
        :type: int
        """

        self._colorspace = colorspace

    @property
    def path(self):
        """Gets the path of this V1EventVideo.  # noqa: E501


        :return: The path of this V1EventVideo.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1EventVideo.


        :param path: The path of this V1EventVideo.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def content_type(self):
        """Gets the content_type of this V1EventVideo.  # noqa: E501


        :return: The content_type of this V1EventVideo.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this V1EventVideo.


        :param content_type: The content_type of this V1EventVideo.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(V1EventVideo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1EventVideo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
