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
 * The version of the OpenAPI document: 1.5.4
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The V1MedianStoppingPolicy model module.
 * @module model/V1MedianStoppingPolicy
 * @version 1.5.4
 */
class V1MedianStoppingPolicy {
    /**
     * Constructs a new <code>V1MedianStoppingPolicy</code>.
     * Early stopping with median stopping, this policy computes running medians across all runs and stops those whose best performance is worse than the median of the running runs.
     * @alias module:model/V1MedianStoppingPolicy
     */
    constructor() { 
        
        V1MedianStoppingPolicy.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>V1MedianStoppingPolicy</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/V1MedianStoppingPolicy} obj Optional instance to populate.
     * @return {module:model/V1MedianStoppingPolicy} The populated <code>V1MedianStoppingPolicy</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new V1MedianStoppingPolicy();

            if (data.hasOwnProperty('kind')) {
                obj['kind'] = ApiClient.convertToType(data['kind'], 'String');
            }
            if (data.hasOwnProperty('evaluation_interval')) {
                obj['evaluation_interval'] = ApiClient.convertToType(data['evaluation_interval'], 'Number');
            }
            if (data.hasOwnProperty('min_interval')) {
                obj['min_interval'] = ApiClient.convertToType(data['min_interval'], 'Number');
            }
            if (data.hasOwnProperty('min_samples')) {
                obj['min_samples'] = ApiClient.convertToType(data['min_samples'], 'Number');
            }
        }
        return obj;
    }


}

/**
 * @member {String} kind
 * @default 'median'
 */
V1MedianStoppingPolicy.prototype['kind'] = 'median';

/**
 * Interval/Frequency for applying the policy.
 * @member {Number} evaluation_interval
 */
V1MedianStoppingPolicy.prototype['evaluation_interval'] = undefined;

/**
 * @member {Number} min_interval
 */
V1MedianStoppingPolicy.prototype['min_interval'] = undefined;

/**
 * @member {Number} min_samples
 */
V1MedianStoppingPolicy.prototype['min_samples'] = undefined;






export default V1MedianStoppingPolicy;

