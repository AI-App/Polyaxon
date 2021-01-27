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
    V1Cache,
    V1CacheFromJSON,
    V1CacheFromJSONTyped,
    V1CacheToJSON,
    V1EventTrigger,
    V1EventTriggerFromJSON,
    V1EventTriggerFromJSONTyped,
    V1EventTriggerToJSON,
    V1Hook,
    V1HookFromJSON,
    V1HookFromJSONTyped,
    V1HookToJSON,
    V1IO,
    V1IOFromJSON,
    V1IOFromJSONTyped,
    V1IOToJSON,
    V1Join,
    V1JoinFromJSON,
    V1JoinFromJSONTyped,
    V1JoinToJSON,
    V1Plugins,
    V1PluginsFromJSON,
    V1PluginsFromJSONTyped,
    V1PluginsToJSON,
    V1Termination,
    V1TerminationFromJSON,
    V1TerminationFromJSONTyped,
    V1TerminationToJSON,
    V1TriggerPolicy,
    V1TriggerPolicyFromJSON,
    V1TriggerPolicyFromJSONTyped,
    V1TriggerPolicyToJSON,
} from './';

/**
 * 
 * @export
 * @interface V1CompiledOperation
 */
export interface V1CompiledOperation {
    /**
     * 
     * @type {number}
     * @memberof V1CompiledOperation
     */
    version?: number;
    /**
     * 
     * @type {string}
     * @memberof V1CompiledOperation
     */
    kind?: string;
    /**
     * 
     * @type {string}
     * @memberof V1CompiledOperation
     */
    name?: string;
    /**
     * 
     * @type {string}
     * @memberof V1CompiledOperation
     */
    description?: string;
    /**
     * 
     * @type {Array<string>}
     * @memberof V1CompiledOperation
     */
    tags?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof V1CompiledOperation
     */
    presets?: Array<string>;
    /**
     * 
     * @type {string}
     * @memberof V1CompiledOperation
     */
    queue?: string;
    /**
     * 
     * @type {V1Cache}
     * @memberof V1CompiledOperation
     */
    cache?: V1Cache;
    /**
     * 
     * @type {V1Termination}
     * @memberof V1CompiledOperation
     */
    termination?: V1Termination;
    /**
     * 
     * @type {V1Plugins}
     * @memberof V1CompiledOperation
     */
    plugins?: V1Plugins;
    /**
     * 
     * @type {object}
     * @memberof V1CompiledOperation
     */
    schedule?: object;
    /**
     * 
     * @type {Array<V1EventTrigger>}
     * @memberof V1CompiledOperation
     */
    events?: Array<V1EventTrigger>;
    /**
     * 
     * @type {Array<V1Hook>}
     * @memberof V1CompiledOperation
     */
    hooks?: Array<V1Hook>;
    /**
     * 
     * @type {Array<string>}
     * @memberof V1CompiledOperation
     */
    dependencies?: Array<string>;
    /**
     * 
     * @type {V1TriggerPolicy}
     * @memberof V1CompiledOperation
     */
    trigger?: V1TriggerPolicy;
    /**
     * 
     * @type {string}
     * @memberof V1CompiledOperation
     */
    conditions?: string;
    /**
     * 
     * @type {boolean}
     * @memberof V1CompiledOperation
     */
    skip_on_upstream_skip?: boolean;
    /**
     * 
     * @type {object}
     * @memberof V1CompiledOperation
     */
    matrix?: object;
    /**
     * 
     * @type {{ [key: string]: V1Join; }}
     * @memberof V1CompiledOperation
     */
    joins?: { [key: string]: V1Join; };
    /**
     * 
     * @type {Array<V1IO>}
     * @memberof V1CompiledOperation
     */
    inputs?: Array<V1IO>;
    /**
     * 
     * @type {Array<V1IO>}
     * @memberof V1CompiledOperation
     */
    outputs?: Array<V1IO>;
    /**
     * 
     * @type {Array<V1IO>}
     * @memberof V1CompiledOperation
     */
    contexts?: Array<V1IO>;
    /**
     * 
     * @type {boolean}
     * @memberof V1CompiledOperation
     */
    is_approved?: boolean;
    /**
     * 
     * @type {object}
     * @memberof V1CompiledOperation
     */
    run?: object;
}

export function V1CompiledOperationFromJSON(json: any): V1CompiledOperation {
    return V1CompiledOperationFromJSONTyped(json, false);
}

export function V1CompiledOperationFromJSONTyped(json: any, ignoreDiscriminator: boolean): V1CompiledOperation {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'version': !exists(json, 'version') ? undefined : json['version'],
        'kind': !exists(json, 'kind') ? undefined : json['kind'],
        'name': !exists(json, 'name') ? undefined : json['name'],
        'description': !exists(json, 'description') ? undefined : json['description'],
        'tags': !exists(json, 'tags') ? undefined : json['tags'],
        'presets': !exists(json, 'presets') ? undefined : json['presets'],
        'queue': !exists(json, 'queue') ? undefined : json['queue'],
        'cache': !exists(json, 'cache') ? undefined : V1CacheFromJSON(json['cache']),
        'termination': !exists(json, 'termination') ? undefined : V1TerminationFromJSON(json['termination']),
        'plugins': !exists(json, 'plugins') ? undefined : V1PluginsFromJSON(json['plugins']),
        'schedule': !exists(json, 'schedule') ? undefined : json['schedule'],
        'events': !exists(json, 'events') ? undefined : ((json['events'] as Array<any>).map(V1EventTriggerFromJSON)),
        'hooks': !exists(json, 'hooks') ? undefined : ((json['hooks'] as Array<any>).map(V1HookFromJSON)),
        'dependencies': !exists(json, 'dependencies') ? undefined : json['dependencies'],
        'trigger': !exists(json, 'trigger') ? undefined : V1TriggerPolicyFromJSON(json['trigger']),
        'conditions': !exists(json, 'conditions') ? undefined : json['conditions'],
        'skip_on_upstream_skip': !exists(json, 'skip_on_upstream_skip') ? undefined : json['skip_on_upstream_skip'],
        'matrix': !exists(json, 'matrix') ? undefined : json['matrix'],
        'joins': !exists(json, 'joins') ? undefined : (mapValues(json['joins'], V1JoinFromJSON)),
        'inputs': !exists(json, 'inputs') ? undefined : ((json['inputs'] as Array<any>).map(V1IOFromJSON)),
        'outputs': !exists(json, 'outputs') ? undefined : ((json['outputs'] as Array<any>).map(V1IOFromJSON)),
        'contexts': !exists(json, 'contexts') ? undefined : ((json['contexts'] as Array<any>).map(V1IOFromJSON)),
        'is_approved': !exists(json, 'is_approved') ? undefined : json['is_approved'],
        'run': !exists(json, 'run') ? undefined : json['run'],
    };
}

export function V1CompiledOperationToJSON(value?: V1CompiledOperation | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'version': value.version,
        'kind': value.kind,
        'name': value.name,
        'description': value.description,
        'tags': value.tags,
        'presets': value.presets,
        'queue': value.queue,
        'cache': V1CacheToJSON(value.cache),
        'termination': V1TerminationToJSON(value.termination),
        'plugins': V1PluginsToJSON(value.plugins),
        'schedule': value.schedule,
        'events': value.events === undefined ? undefined : ((value.events as Array<any>).map(V1EventTriggerToJSON)),
        'hooks': value.hooks === undefined ? undefined : ((value.hooks as Array<any>).map(V1HookToJSON)),
        'dependencies': value.dependencies,
        'trigger': V1TriggerPolicyToJSON(value.trigger),
        'conditions': value.conditions,
        'skip_on_upstream_skip': value.skip_on_upstream_skip,
        'matrix': value.matrix,
        'joins': value.joins === undefined ? undefined : (mapValues(value.joins, V1JoinToJSON)),
        'inputs': value.inputs === undefined ? undefined : ((value.inputs as Array<any>).map(V1IOToJSON)),
        'outputs': value.outputs === undefined ? undefined : ((value.outputs as Array<any>).map(V1IOToJSON)),
        'contexts': value.contexts === undefined ? undefined : ((value.contexts as Array<any>).map(V1IOToJSON)),
        'is_approved': value.is_approved,
        'run': value.run,
    };
}


