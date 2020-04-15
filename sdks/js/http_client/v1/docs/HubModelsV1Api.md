# PolyaxonSdk.HubModelsV1Api

Polyaxon&#39;s typescript client

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createHubModel**](HubModelsV1Api.md#createHubModel) | **POST** /api/v1/orgs/{owner}/models | Create dashboard
[**deleteHubModel**](HubModelsV1Api.md#deleteHubModel) | **DELETE** /api/v1/orgs/{owner}/models/{uuid} | Delete dashboard
[**getHubModel**](HubModelsV1Api.md#getHubModel) | **GET** /api/v1/orgs/{owner}/models/{uuid} | Get dashboard
[**listHubModelNames**](HubModelsV1Api.md#listHubModelNames) | **GET** /api/v1/orgs/{owner}/models/names | List dashboard names
[**listHubModels**](HubModelsV1Api.md#listHubModels) | **GET** /api/v1/orgs/{owner}/models | List dashboards
[**patchHubModel**](HubModelsV1Api.md#patchHubModel) | **PATCH** /api/v1/orgs/{owner}/models/{model.uuid} | Patch dashboard
[**updateHubModel**](HubModelsV1Api.md#updateHubModel) | **PUT** /api/v1/orgs/{owner}/models/{model.uuid} | Update dashboard



## createHubModel

> V1HubModel createHubModel(owner, body)

Create dashboard

### Example

```javascript
import PolyaxonSdk from 'polyaxon-sdk';
let defaultClient = PolyaxonSdk.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PolyaxonSdk.HubModelsV1Api();
let owner = "owner_example"; // String | Owner of the namespace
let body = new PolyaxonSdk.V1HubModel(); // V1HubModel | Model body
apiInstance.createHubModel(owner, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| Owner of the namespace | 
 **body** | [**V1HubModel**](V1HubModel.md)| Model body | 

### Return type

[**V1HubModel**](V1HubModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteHubModel

> Object deleteHubModel(owner, uuid)

Delete dashboard

### Example

```javascript
import PolyaxonSdk from 'polyaxon-sdk';
let defaultClient = PolyaxonSdk.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PolyaxonSdk.HubModelsV1Api();
let owner = "owner_example"; // String | Owner of the namespace
let uuid = "uuid_example"; // String | Uuid identifier of the entity
apiInstance.deleteHubModel(owner, uuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| Owner of the namespace | 
 **uuid** | **String**| Uuid identifier of the entity | 

### Return type

**Object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHubModel

> V1HubModel getHubModel(owner, uuid)

Get dashboard

### Example

```javascript
import PolyaxonSdk from 'polyaxon-sdk';
let defaultClient = PolyaxonSdk.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PolyaxonSdk.HubModelsV1Api();
let owner = "owner_example"; // String | Owner of the namespace
let uuid = "uuid_example"; // String | Uuid identifier of the entity
apiInstance.getHubModel(owner, uuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| Owner of the namespace | 
 **uuid** | **String**| Uuid identifier of the entity | 

### Return type

[**V1HubModel**](V1HubModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listHubModelNames

> V1ListHubModelsResponse listHubModelNames(owner, opts)

List dashboard names

### Example

```javascript
import PolyaxonSdk from 'polyaxon-sdk';
let defaultClient = PolyaxonSdk.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PolyaxonSdk.HubModelsV1Api();
let owner = "owner_example"; // String | Owner of the namespace
let opts = {
  'offset': 56, // Number | Pagination offset.
  'limit': 56, // Number | Limit size.
  'sort': "sort_example", // String | Sort to order the search.
  'query': "query_example" // String | Query filter the search search.
};
apiInstance.listHubModelNames(owner, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| Owner of the namespace | 
 **offset** | **Number**| Pagination offset. | [optional] 
 **limit** | **Number**| Limit size. | [optional] 
 **sort** | **String**| Sort to order the search. | [optional] 
 **query** | **String**| Query filter the search search. | [optional] 

### Return type

[**V1ListHubModelsResponse**](V1ListHubModelsResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listHubModels

> V1ListHubModelsResponse listHubModels(owner, opts)

List dashboards

### Example

```javascript
import PolyaxonSdk from 'polyaxon-sdk';
let defaultClient = PolyaxonSdk.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PolyaxonSdk.HubModelsV1Api();
let owner = "owner_example"; // String | Owner of the namespace
let opts = {
  'offset': 56, // Number | Pagination offset.
  'limit': 56, // Number | Limit size.
  'sort': "sort_example", // String | Sort to order the search.
  'query': "query_example" // String | Query filter the search search.
};
apiInstance.listHubModels(owner, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| Owner of the namespace | 
 **offset** | **Number**| Pagination offset. | [optional] 
 **limit** | **Number**| Limit size. | [optional] 
 **sort** | **String**| Sort to order the search. | [optional] 
 **query** | **String**| Query filter the search search. | [optional] 

### Return type

[**V1ListHubModelsResponse**](V1ListHubModelsResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchHubModel

> V1HubModel patchHubModel(owner, model_uuid, body)

Patch dashboard

### Example

```javascript
import PolyaxonSdk from 'polyaxon-sdk';
let defaultClient = PolyaxonSdk.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PolyaxonSdk.HubModelsV1Api();
let owner = "owner_example"; // String | Owner of the namespace
let model_uuid = "model_uuid_example"; // String | UUID
let body = new PolyaxonSdk.V1HubModel(); // V1HubModel | Model body
apiInstance.patchHubModel(owner, model_uuid, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| Owner of the namespace | 
 **model_uuid** | **String**| UUID | 
 **body** | [**V1HubModel**](V1HubModel.md)| Model body | 

### Return type

[**V1HubModel**](V1HubModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateHubModel

> V1HubModel updateHubModel(owner, model_uuid, body)

Update dashboard

### Example

```javascript
import PolyaxonSdk from 'polyaxon-sdk';
let defaultClient = PolyaxonSdk.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new PolyaxonSdk.HubModelsV1Api();
let owner = "owner_example"; // String | Owner of the namespace
let model_uuid = "model_uuid_example"; // String | UUID
let body = new PolyaxonSdk.V1HubModel(); // V1HubModel | Model body
apiInstance.updateHubModel(owner, model_uuid, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| Owner of the namespace | 
 **model_uuid** | **String**| UUID | 
 **body** | [**V1HubModel**](V1HubModel.md)| Model body | 

### Return type

[**V1HubModel**](V1HubModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

