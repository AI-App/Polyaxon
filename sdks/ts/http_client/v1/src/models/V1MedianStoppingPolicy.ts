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

/* tslint:disable */
/* eslint-disable */
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
 */

import { exists, mapValues } from '../runtime';
/**
 * Early stopping with median stopping, this policy computes running medians across
 * all runs and stops those whose best performance is worse than the median
 * of the running runs.
 * @export
 * @interface V1MedianStoppingPolicy
 */
export interface V1MedianStoppingPolicy {
    /**
     * 
     * @type {string}
     * @memberof V1MedianStoppingPolicy
     */
    kind?: string;
    /**
     * Interval/Frequency for applying the policy.
     * @type {number}
     * @memberof V1MedianStoppingPolicy
     */
    evaluationInterval?: number;
    /**
     * 
     * @type {number}
     * @memberof V1MedianStoppingPolicy
     */
    minInterval?: number;
    /**
     * 
     * @type {number}
     * @memberof V1MedianStoppingPolicy
     */
    minSamples?: number;
}

export function V1MedianStoppingPolicyFromJSON(json: any): V1MedianStoppingPolicy {
    return V1MedianStoppingPolicyFromJSONTyped(json, false);
}

export function V1MedianStoppingPolicyFromJSONTyped(json: any, ignoreDiscriminator: boolean): V1MedianStoppingPolicy {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'kind': !exists(json, 'kind') ? undefined : json['kind'],
        'evaluationInterval': !exists(json, 'evaluationInterval') ? undefined : json['evaluationInterval'],
        'minInterval': !exists(json, 'minInterval') ? undefined : json['minInterval'],
        'minSamples': !exists(json, 'minSamples') ? undefined : json['minSamples'],
    };
}

export function V1MedianStoppingPolicyToJSON(value?: V1MedianStoppingPolicy | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'kind': value.kind,
        'evaluationInterval': value.evaluationInterval,
        'minInterval': value.minInterval,
        'minSamples': value.minSamples,
    };
}


