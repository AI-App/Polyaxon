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

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from polyaxon_sdk.api_client import ApiClient


class ConnectionsV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_connection(self, owner, body, **kwargs):  # noqa: E501
        """Create connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_connection(owner, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param V1ConnectionResponse body: Connection body (required)
        :return: V1ConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_connection_with_http_info(
                owner, body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.create_connection_with_http_info(
                owner, body, **kwargs
            )  # noqa: E501
            return data

    def create_connection_with_http_info(self, owner, body, **kwargs):  # noqa: E501
        """Create connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_connection_with_http_info(owner, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param V1ConnectionResponse body: Connection body (required)
        :return: V1ConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["owner", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_connection" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'owner' is set
        if "owner" not in params or params["owner"] is None:
            raise ValueError(
                "Missing the required parameter `owner` when calling `create_connection`"
            )  # noqa: E501
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `create_connection`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner" in params:
            path_params["owner"] = params["owner"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKey"]  # noqa: E501

        return self.api_client.call_api(
            "/api/v1/orgs/{owner}/connections",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="V1ConnectionResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_connection(self, owner, uuid, **kwargs):  # noqa: E501
        """Delete connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_connection(owner, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param str uuid: Uuid identifier of the entity (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_connection_with_http_info(
                owner, uuid, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_connection_with_http_info(
                owner, uuid, **kwargs
            )  # noqa: E501
            return data

    def delete_connection_with_http_info(self, owner, uuid, **kwargs):  # noqa: E501
        """Delete connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_connection_with_http_info(owner, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param str uuid: Uuid identifier of the entity (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["owner", "uuid"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_connection" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'owner' is set
        if "owner" not in params or params["owner"] is None:
            raise ValueError(
                "Missing the required parameter `owner` when calling `delete_connection`"
            )  # noqa: E501
        # verify the required parameter 'uuid' is set
        if "uuid" not in params or params["uuid"] is None:
            raise ValueError(
                "Missing the required parameter `uuid` when calling `delete_connection`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner" in params:
            path_params["owner"] = params["owner"]  # noqa: E501
        if "uuid" in params:
            path_params["uuid"] = params["uuid"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKey"]  # noqa: E501

        return self.api_client.call_api(
            "/api/v1/orgs/{owner}/connections/{uuid}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_connection(self, owner, uuid, **kwargs):  # noqa: E501
        """Get connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connection(owner, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param str uuid: Uuid identifier of the entity (required)
        :return: V1ConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_connection_with_http_info(
                owner, uuid, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_connection_with_http_info(
                owner, uuid, **kwargs
            )  # noqa: E501
            return data

    def get_connection_with_http_info(self, owner, uuid, **kwargs):  # noqa: E501
        """Get connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connection_with_http_info(owner, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param str uuid: Uuid identifier of the entity (required)
        :return: V1ConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["owner", "uuid"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_connection" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'owner' is set
        if "owner" not in params or params["owner"] is None:
            raise ValueError(
                "Missing the required parameter `owner` when calling `get_connection`"
            )  # noqa: E501
        # verify the required parameter 'uuid' is set
        if "uuid" not in params or params["uuid"] is None:
            raise ValueError(
                "Missing the required parameter `uuid` when calling `get_connection`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner" in params:
            path_params["owner"] = params["owner"]  # noqa: E501
        if "uuid" in params:
            path_params["uuid"] = params["uuid"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKey"]  # noqa: E501

        return self.api_client.call_api(
            "/api/v1/orgs/{owner}/connections/{uuid}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="V1ConnectionResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_connection_names(self, owner, **kwargs):  # noqa: E501
        """List connections names  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_connection_names(owner, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param int offset: Pagination offset.
        :param int limit: Limit size.
        :param str sort: Sort to order the search.
        :param str query: Query filter the search search.
        :return: V1ListConnectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_connection_names_with_http_info(
                owner, **kwargs
            )  # noqa: E501
        else:
            (data) = self.list_connection_names_with_http_info(
                owner, **kwargs
            )  # noqa: E501
            return data

    def list_connection_names_with_http_info(self, owner, **kwargs):  # noqa: E501
        """List connections names  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_connection_names_with_http_info(owner, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param int offset: Pagination offset.
        :param int limit: Limit size.
        :param str sort: Sort to order the search.
        :param str query: Query filter the search search.
        :return: V1ListConnectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["owner", "offset", "limit", "sort", "query"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_connection_names" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'owner' is set
        if "owner" not in params or params["owner"] is None:
            raise ValueError(
                "Missing the required parameter `owner` when calling `list_connection_names`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner" in params:
            path_params["owner"] = params["owner"]  # noqa: E501

        query_params = []
        if "offset" in params:
            query_params.append(("offset", params["offset"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501
        if "sort" in params:
            query_params.append(("sort", params["sort"]))  # noqa: E501
        if "query" in params:
            query_params.append(("query", params["query"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKey"]  # noqa: E501

        return self.api_client.call_api(
            "/api/v1/orgs/{owner}/connections/names",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="V1ListConnectionsResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_connections(self, owner, **kwargs):  # noqa: E501
        """List connections  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_connections(owner, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param int offset: Pagination offset.
        :param int limit: Limit size.
        :param str sort: Sort to order the search.
        :param str query: Query filter the search search.
        :return: V1ListConnectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_connections_with_http_info(owner, **kwargs)  # noqa: E501
        else:
            (data) = self.list_connections_with_http_info(owner, **kwargs)  # noqa: E501
            return data

    def list_connections_with_http_info(self, owner, **kwargs):  # noqa: E501
        """List connections  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_connections_with_http_info(owner, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param int offset: Pagination offset.
        :param int limit: Limit size.
        :param str sort: Sort to order the search.
        :param str query: Query filter the search search.
        :return: V1ListConnectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["owner", "offset", "limit", "sort", "query"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_connections" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'owner' is set
        if "owner" not in params or params["owner"] is None:
            raise ValueError(
                "Missing the required parameter `owner` when calling `list_connections`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner" in params:
            path_params["owner"] = params["owner"]  # noqa: E501

        query_params = []
        if "offset" in params:
            query_params.append(("offset", params["offset"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501
        if "sort" in params:
            query_params.append(("sort", params["sort"]))  # noqa: E501
        if "query" in params:
            query_params.append(("query", params["query"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKey"]  # noqa: E501

        return self.api_client.call_api(
            "/api/v1/orgs/{owner}/connections",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="V1ListConnectionsResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def patch_connection(self, owner, connection_uuid, body, **kwargs):  # noqa: E501
        """Patch connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_connection(owner, connection_uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param str connection_uuid: UUID (required)
        :param V1ConnectionResponse body: Connection body (required)
        :return: V1ConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.patch_connection_with_http_info(
                owner, connection_uuid, body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.patch_connection_with_http_info(
                owner, connection_uuid, body, **kwargs
            )  # noqa: E501
            return data

    def patch_connection_with_http_info(
        self, owner, connection_uuid, body, **kwargs
    ):  # noqa: E501
        """Patch connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_connection_with_http_info(owner, connection_uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param str connection_uuid: UUID (required)
        :param V1ConnectionResponse body: Connection body (required)
        :return: V1ConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["owner", "connection_uuid", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_connection" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'owner' is set
        if "owner" not in params or params["owner"] is None:
            raise ValueError(
                "Missing the required parameter `owner` when calling `patch_connection`"
            )  # noqa: E501
        # verify the required parameter 'connection_uuid' is set
        if "connection_uuid" not in params or params["connection_uuid"] is None:
            raise ValueError(
                "Missing the required parameter `connection_uuid` when calling `patch_connection`"
            )  # noqa: E501
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `patch_connection`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner" in params:
            path_params["owner"] = params["owner"]  # noqa: E501
        if "connection_uuid" in params:
            path_params["connection.uuid"] = params["connection_uuid"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKey"]  # noqa: E501

        return self.api_client.call_api(
            "/api/v1/orgs/{owner}/connections/{connection.uuid}",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="V1ConnectionResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_connection(self, owner, connection_uuid, body, **kwargs):  # noqa: E501
        """Update connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_connection(owner, connection_uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param str connection_uuid: UUID (required)
        :param V1ConnectionResponse body: Connection body (required)
        :return: V1ConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_connection_with_http_info(
                owner, connection_uuid, body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_connection_with_http_info(
                owner, connection_uuid, body, **kwargs
            )  # noqa: E501
            return data

    def update_connection_with_http_info(
        self, owner, connection_uuid, body, **kwargs
    ):  # noqa: E501
        """Update connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_connection_with_http_info(owner, connection_uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: Owner of the namespace (required)
        :param str connection_uuid: UUID (required)
        :param V1ConnectionResponse body: Connection body (required)
        :return: V1ConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["owner", "connection_uuid", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_connection" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'owner' is set
        if "owner" not in params or params["owner"] is None:
            raise ValueError(
                "Missing the required parameter `owner` when calling `update_connection`"
            )  # noqa: E501
        # verify the required parameter 'connection_uuid' is set
        if "connection_uuid" not in params or params["connection_uuid"] is None:
            raise ValueError(
                "Missing the required parameter `connection_uuid` when calling `update_connection`"
            )  # noqa: E501
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `update_connection`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner" in params:
            path_params["owner"] = params["owner"]  # noqa: E501
        if "connection_uuid" in params:
            path_params["connection.uuid"] = params["connection_uuid"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["ApiKey"]  # noqa: E501

        return self.api_client.call_api(
            "/api/v1/orgs/{owner}/connections/{connection.uuid}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="V1ConnectionResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
