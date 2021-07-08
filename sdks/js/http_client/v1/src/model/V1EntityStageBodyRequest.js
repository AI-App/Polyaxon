// Copyright 2018-2021 Polyaxon, Inc.
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

/**
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * The version of the OpenAPI document: 1.10.1
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import V1StageCondition from './V1StageCondition';

/**
 * The V1EntityStageBodyRequest model module.
 * @module model/V1EntityStageBodyRequest
 * @version 1.10.1
 */
class V1EntityStageBodyRequest {
    /**
     * Constructs a new <code>V1EntityStageBodyRequest</code>.
     * @alias module:model/V1EntityStageBodyRequest
     */
    constructor() { 
        
        V1EntityStageBodyRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>V1EntityStageBodyRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/V1EntityStageBodyRequest} obj Optional instance to populate.
     * @return {module:model/V1EntityStageBodyRequest} The populated <code>V1EntityStageBodyRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new V1EntityStageBodyRequest();

            if (data.hasOwnProperty('owner')) {
                obj['owner'] = ApiClient.convertToType(data['owner'], 'String');
            }
            if (data.hasOwnProperty('entity')) {
                obj['entity'] = ApiClient.convertToType(data['entity'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('condition')) {
                obj['condition'] = V1StageCondition.constructFromObject(data['condition']);
            }
        }
        return obj;
    }


}

/**
 * @member {String} owner
 */
V1EntityStageBodyRequest.prototype['owner'] = undefined;

/**
 * @member {String} entity
 */
V1EntityStageBodyRequest.prototype['entity'] = undefined;

/**
 * @member {String} name
 */
V1EntityStageBodyRequest.prototype['name'] = undefined;

/**
 * @member {module:model/V1StageCondition} condition
 */
V1EntityStageBodyRequest.prototype['condition'] = undefined;






export default V1EntityStageBodyRequest;

