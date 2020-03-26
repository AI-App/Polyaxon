// Copyright 2018-2020 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/*
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * OpenAPI spec version: 1.0.7
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.api;

import io.swagger.client.ApiCallback;
import io.swagger.client.ApiClient;
import io.swagger.client.ApiException;
import io.swagger.client.ApiResponse;
import io.swagger.client.Configuration;
import io.swagger.client.Pair;
import io.swagger.client.ProgressRequestBody;
import io.swagger.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import java.io.File;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ArtifactsStoresV1Api {
    private ApiClient apiClient;

    public ArtifactsStoresV1Api() {
        this(Configuration.getDefaultApiClient());
    }

    public ArtifactsStoresV1Api(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return apiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /**
     * Build call for uploadArtifact
     * @param owner Owner of the namespace (required)
     * @param uuid Unique integer identifier of the entity (required)
     * @param uploadfile The file to upload. (required)
     * @param path File path query params. (optional)
     * @param overwrite File path query params. (optional)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call uploadArtifactCall(String owner, String uuid, File uploadfile, String path, Boolean overwrite, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/api/v1/catalogs/{owner}/artifacts/{uuid}/upload"
            .replaceAll("\\{" + "owner" + "\\}", apiClient.escapeString(owner.toString()))
            .replaceAll("\\{" + "uuid" + "\\}", apiClient.escapeString(uuid.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        if (path != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("path", path));
        if (overwrite != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("overwrite", overwrite));

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();
        if (uploadfile != null)
        localVarFormParams.put("uploadfile", uploadfile);

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            "multipart/form-data"
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] { "ApiKey" };
        return apiClient.buildCall(localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }

    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call uploadArtifactValidateBeforeCall(String owner, String uuid, File uploadfile, String path, Boolean overwrite, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        
        // verify the required parameter 'owner' is set
        if (owner == null) {
            throw new ApiException("Missing the required parameter 'owner' when calling uploadArtifact(Async)");
        }
        
        // verify the required parameter 'uuid' is set
        if (uuid == null) {
            throw new ApiException("Missing the required parameter 'uuid' when calling uploadArtifact(Async)");
        }
        
        // verify the required parameter 'uploadfile' is set
        if (uploadfile == null) {
            throw new ApiException("Missing the required parameter 'uploadfile' when calling uploadArtifact(Async)");
        }
        

        com.squareup.okhttp.Call call = uploadArtifactCall(owner, uuid, uploadfile, path, overwrite, progressListener, progressRequestListener);
        return call;

    }

    /**
     * Upload artifact to a store
     * 
     * @param owner Owner of the namespace (required)
     * @param uuid Unique integer identifier of the entity (required)
     * @param uploadfile The file to upload. (required)
     * @param path File path query params. (optional)
     * @param overwrite File path query params. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public void uploadArtifact(String owner, String uuid, File uploadfile, String path, Boolean overwrite) throws ApiException {
        uploadArtifactWithHttpInfo(owner, uuid, uploadfile, path, overwrite);
    }

    /**
     * Upload artifact to a store
     * 
     * @param owner Owner of the namespace (required)
     * @param uuid Unique integer identifier of the entity (required)
     * @param uploadfile The file to upload. (required)
     * @param path File path query params. (optional)
     * @param overwrite File path query params. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Void> uploadArtifactWithHttpInfo(String owner, String uuid, File uploadfile, String path, Boolean overwrite) throws ApiException {
        com.squareup.okhttp.Call call = uploadArtifactValidateBeforeCall(owner, uuid, uploadfile, path, overwrite, null, null);
        return apiClient.execute(call);
    }

    /**
     * Upload artifact to a store (asynchronously)
     * 
     * @param owner Owner of the namespace (required)
     * @param uuid Unique integer identifier of the entity (required)
     * @param uploadfile The file to upload. (required)
     * @param path File path query params. (optional)
     * @param overwrite File path query params. (optional)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call uploadArtifactAsync(String owner, String uuid, File uploadfile, String path, Boolean overwrite, final ApiCallback<Void> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = uploadArtifactValidateBeforeCall(owner, uuid, uploadfile, path, overwrite, progressListener, progressRequestListener);
        apiClient.executeAsync(call, callback);
        return call;
    }
}
