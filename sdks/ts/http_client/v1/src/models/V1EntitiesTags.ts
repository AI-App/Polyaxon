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
/**
 * 
 * @export
 * @interface V1EntitiesTags
 */
export interface V1EntitiesTags {
    /**
     * 
     * @type {Array<string>}
     * @memberof V1EntitiesTags
     */
    uuids?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof V1EntitiesTags
     */
    tags?: Array<string>;
}

export function V1EntitiesTagsFromJSON(json: any): V1EntitiesTags {
    return V1EntitiesTagsFromJSONTyped(json, false);
}

export function V1EntitiesTagsFromJSONTyped(json: any, ignoreDiscriminator: boolean): V1EntitiesTags {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'uuids': !exists(json, 'uuids') ? undefined : json['uuids'],
        'tags': !exists(json, 'tags') ? undefined : json['tags'],
    };
}

export function V1EntitiesTagsToJSON(value?: V1EntitiesTags | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'uuids': value.uuids,
        'tags': value.tags,
    };
}


