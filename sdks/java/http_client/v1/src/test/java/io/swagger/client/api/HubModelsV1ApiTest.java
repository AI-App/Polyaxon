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

import io.swagger.client.ApiException;
import io.swagger.client.model.RuntimeError;
import io.swagger.client.model.V1HubModel;
import io.swagger.client.model.V1ListHubModelsResponse;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for HubModelsV1Api
 */
@Ignore
public class HubModelsV1ApiTest {

    private final HubModelsV1Api api = new HubModelsV1Api();

    
    /**
     * Create dashboard
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createHubModelTest() throws ApiException {
        String owner = null;
        V1HubModel body = null;
        V1HubModel response = api.createHubModel(owner, body);

        // TODO: test validations
    }
    
    /**
     * Delete dashboard
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteHubModelTest() throws ApiException {
        String owner = null;
        String uuid = null;
        api.deleteHubModel(owner, uuid);

        // TODO: test validations
    }
    
    /**
     * Get dashboard
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getHubModelTest() throws ApiException {
        String owner = null;
        String uuid = null;
        V1HubModel response = api.getHubModel(owner, uuid);

        // TODO: test validations
    }
    
    /**
     * List dashboard names
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listHubModelNamesTest() throws ApiException {
        String owner = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        String query = null;
        V1ListHubModelsResponse response = api.listHubModelNames(owner, offset, limit, sort, query);

        // TODO: test validations
    }
    
    /**
     * List dashboards
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listHubModelsTest() throws ApiException {
        String owner = null;
        Integer offset = null;
        Integer limit = null;
        String sort = null;
        String query = null;
        V1ListHubModelsResponse response = api.listHubModels(owner, offset, limit, sort, query);

        // TODO: test validations
    }
    
    /**
     * Patch dashboard
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void patchHubModelTest() throws ApiException {
        String owner = null;
        String modelUuid = null;
        V1HubModel body = null;
        V1HubModel response = api.patchHubModel(owner, modelUuid, body);

        // TODO: test validations
    }
    
    /**
     * Update dashboard
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateHubModelTest() throws ApiException {
        String owner = null;
        String modelUuid = null;
        V1HubModel body = null;
        V1HubModel response = api.updateHubModel(owner, modelUuid, body);

        // TODO: test validations
    }
    
}
