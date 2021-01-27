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
 * The version of the OpenAPI document: 1.5.4
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import {
    V1CleanPodPolicy,
    V1CleanPodPolicyFromJSON,
    V1CleanPodPolicyFromJSONTyped,
    V1CleanPodPolicyToJSON,
    V1KFReplica,
    V1KFReplicaFromJSON,
    V1KFReplicaFromJSONTyped,
    V1KFReplicaToJSON,
} from './';

/**
 * 
 * @export
 * @interface V1TFJob
 */
export interface V1TFJob {
    /**
     * 
     * @type {string}
     * @memberof V1TFJob
     */
    kind?: string;
    /**
     * 
     * @type {V1CleanPodPolicy}
     * @memberof V1TFJob
     */
    cleanPodPolicy?: V1CleanPodPolicy;
    /**
     * 
     * @type {V1KFReplica}
     * @memberof V1TFJob
     */
    chief?: V1KFReplica;
    /**
     * 
     * @type {V1KFReplica}
     * @memberof V1TFJob
     */
    ps?: V1KFReplica;
    /**
     * 
     * @type {V1KFReplica}
     * @memberof V1TFJob
     */
    worker?: V1KFReplica;
    /**
     * 
     * @type {V1KFReplica}
     * @memberof V1TFJob
     */
    evaluator?: V1KFReplica;
}

export function V1TFJobFromJSON(json: any): V1TFJob {
    return V1TFJobFromJSONTyped(json, false);
}

export function V1TFJobFromJSONTyped(json: any, ignoreDiscriminator: boolean): V1TFJob {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'kind': !exists(json, 'kind') ? undefined : json['kind'],
        'cleanPodPolicy': !exists(json, 'cleanPodPolicy') ? undefined : V1CleanPodPolicyFromJSON(json['cleanPodPolicy']),
        'chief': !exists(json, 'chief') ? undefined : V1KFReplicaFromJSON(json['chief']),
        'ps': !exists(json, 'ps') ? undefined : V1KFReplicaFromJSON(json['ps']),
        'worker': !exists(json, 'worker') ? undefined : V1KFReplicaFromJSON(json['worker']),
        'evaluator': !exists(json, 'evaluator') ? undefined : V1KFReplicaFromJSON(json['evaluator']),
    };
}

export function V1TFJobToJSON(value?: V1TFJob | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'kind': value.kind,
        'cleanPodPolicy': V1CleanPodPolicyToJSON(value.cleanPodPolicy),
        'chief': V1KFReplicaToJSON(value.chief),
        'ps': V1KFReplicaToJSON(value.ps),
        'worker': V1KFReplicaToJSON(value.worker),
        'evaluator': V1KFReplicaToJSON(value.evaluator),
    };
}


