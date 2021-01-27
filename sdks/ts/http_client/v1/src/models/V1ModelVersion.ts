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
    V1StageCondition,
    V1StageConditionFromJSON,
    V1StageConditionFromJSONTyped,
    V1StageConditionToJSON,
    V1Stages,
    V1StagesFromJSON,
    V1StagesFromJSONTyped,
    V1StagesToJSON,
} from './';

/**
 * 
 * @export
 * @interface V1ModelVersion
 */
export interface V1ModelVersion {
    /**
     * 
     * @type {string}
     * @memberof V1ModelVersion
     */
    uuid?: string;
    /**
     * 
     * @type {string}
     * @memberof V1ModelVersion
     */
    name?: string;
    /**
     * 
     * @type {string}
     * @memberof V1ModelVersion
     */
    description?: string;
    /**
     * 
     * @type {Array<string>}
     * @memberof V1ModelVersion
     */
    tags?: Array<string>;
    /**
     * 
     * @type {number}
     * @memberof V1ModelVersion
     */
    live_state?: number;
    /**
     * 
     * @type {Date}
     * @memberof V1ModelVersion
     */
    created_at?: Date;
    /**
     * 
     * @type {Date}
     * @memberof V1ModelVersion
     */
    updated_at?: Date;
    /**
     * 
     * @type {V1Stages}
     * @memberof V1ModelVersion
     */
    stage?: V1Stages;
    /**
     * 
     * @type {Array<V1StageCondition>}
     * @memberof V1ModelVersion
     */
    stage_conditions?: Array<V1StageCondition>;
    /**
     * 
     * @type {string}
     * @memberof V1ModelVersion
     */
    run?: string;
    /**
     * 
     * @type {object}
     * @memberof V1ModelVersion
     */
    run_info?: object;
    /**
     * 
     * @type {string}
     * @memberof V1ModelVersion
     */
    metadata?: string;
}

export function V1ModelVersionFromJSON(json: any): V1ModelVersion {
    return V1ModelVersionFromJSONTyped(json, false);
}

export function V1ModelVersionFromJSONTyped(json: any, ignoreDiscriminator: boolean): V1ModelVersion {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'uuid': !exists(json, 'uuid') ? undefined : json['uuid'],
        'name': !exists(json, 'name') ? undefined : json['name'],
        'description': !exists(json, 'description') ? undefined : json['description'],
        'tags': !exists(json, 'tags') ? undefined : json['tags'],
        'live_state': !exists(json, 'live_state') ? undefined : json['live_state'],
        'created_at': !exists(json, 'created_at') ? undefined : (new Date(json['created_at'])),
        'updated_at': !exists(json, 'updated_at') ? undefined : (new Date(json['updated_at'])),
        'stage': !exists(json, 'stage') ? undefined : V1StagesFromJSON(json['stage']),
        'stage_conditions': !exists(json, 'stage_conditions') ? undefined : ((json['stage_conditions'] as Array<any>).map(V1StageConditionFromJSON)),
        'run': !exists(json, 'run') ? undefined : json['run'],
        'run_info': !exists(json, 'run_info') ? undefined : json['run_info'],
        'metadata': !exists(json, 'metadata') ? undefined : json['metadata'],
    };
}

export function V1ModelVersionToJSON(value?: V1ModelVersion | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'uuid': value.uuid,
        'name': value.name,
        'description': value.description,
        'tags': value.tags,
        'live_state': value.live_state,
        'created_at': value.created_at === undefined ? undefined : (value.created_at.toISOString()),
        'updated_at': value.updated_at === undefined ? undefined : (value.updated_at.toISOString()),
        'stage': V1StagesToJSON(value.stage),
        'stage_conditions': value.stage_conditions === undefined ? undefined : ((value.stage_conditions as Array<any>).map(V1StageConditionToJSON)),
        'run': value.run,
        'run_info': value.run_info,
        'metadata': value.metadata,
    };
}


