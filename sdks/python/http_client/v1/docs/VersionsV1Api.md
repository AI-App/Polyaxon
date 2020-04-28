# polyaxon_sdk.VersionsV1Api
Polyaxon sdk

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_handler**](VersionsV1Api.md#get_log_handler) | **GET** /api/v1/log_handler | Update current user
[**get_versions**](VersionsV1Api.md#get_versions) | **GET** /api/v1/version | Get current user


# **get_log_handler**
> V1LogHandler get_log_handler()

Update current user

### Example

* Api Key Authentication (ApiKey):
```python
from __future__ import print_function
import time
import polyaxon_sdk
from polyaxon_sdk.rest import ApiException
from pprint import pprint
configuration = polyaxon_sdk.Configuration()
# Configure API key authorization: ApiKey
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with polyaxon_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polyaxon_sdk.VersionsV1Api(api_client)
    
    try:
        # Update current user
        api_response = api_instance.get_log_handler()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionsV1Api->get_log_handler: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1LogHandler**](V1LogHandler.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**204** | No content. |  -  |
**403** | You don&#39;t have permission to access the resource. |  -  |
**404** | Resource does not exist. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> V1Versions get_versions()

Get current user

### Example

* Api Key Authentication (ApiKey):
```python
from __future__ import print_function
import time
import polyaxon_sdk
from polyaxon_sdk.rest import ApiException
from pprint import pprint
configuration = polyaxon_sdk.Configuration()
# Configure API key authorization: ApiKey
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"

# Enter a context with an instance of the API client
with polyaxon_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polyaxon_sdk.VersionsV1Api(api_client)
    
    try:
        # Get current user
        api_response = api_instance.get_versions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionsV1Api->get_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1Versions**](V1Versions.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**204** | No content. |  -  |
**403** | You don&#39;t have permission to access the resource. |  -  |
**404** | Resource does not exist. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

