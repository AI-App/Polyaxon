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
import {
    V1ArtifactsMount,
    V1ArtifactsMountFromJSON,
    V1ArtifactsMountFromJSONTyped,
    V1ArtifactsMountToJSON,
    V1ArtifactsType,
    V1ArtifactsTypeFromJSON,
    V1ArtifactsTypeFromJSONTyped,
    V1ArtifactsTypeToJSON,
    V1AuthType,
    V1AuthTypeFromJSON,
    V1AuthTypeFromJSONTyped,
    V1AuthTypeToJSON,
    V1CompiledOperation,
    V1CompiledOperationFromJSON,
    V1CompiledOperationFromJSONTyped,
    V1CompiledOperationToJSON,
    V1ConnectionSchema,
    V1ConnectionSchemaFromJSON,
    V1ConnectionSchemaFromJSONTyped,
    V1ConnectionSchemaToJSON,
    V1ConnectionType,
    V1ConnectionTypeFromJSON,
    V1ConnectionTypeFromJSONTyped,
    V1ConnectionTypeToJSON,
    V1EarlyStopping,
    V1EarlyStoppingFromJSON,
    V1EarlyStoppingFromJSONTyped,
    V1EarlyStoppingToJSON,
    V1Event,
    V1EventFromJSON,
    V1EventFromJSONTyped,
    V1EventToJSON,
    V1EventType,
    V1EventTypeFromJSON,
    V1EventTypeFromJSONTyped,
    V1EventTypeToJSON,
    V1GcsType,
    V1GcsTypeFromJSON,
    V1GcsTypeFromJSONTyped,
    V1GcsTypeToJSON,
    V1HpParams,
    V1HpParamsFromJSON,
    V1HpParamsFromJSONTyped,
    V1HpParamsToJSON,
    V1K8sResourceType,
    V1K8sResourceTypeFromJSON,
    V1K8sResourceTypeFromJSONTyped,
    V1K8sResourceTypeToJSON,
    V1Matrix,
    V1MatrixFromJSON,
    V1MatrixFromJSONTyped,
    V1MatrixToJSON,
    V1MatrixKind,
    V1MatrixKindFromJSON,
    V1MatrixKindFromJSONTyped,
    V1MatrixKindToJSON,
    V1Operation,
    V1OperationFromJSON,
    V1OperationFromJSONTyped,
    V1OperationToJSON,
    V1PolyaxonInitContainer,
    V1PolyaxonInitContainerFromJSON,
    V1PolyaxonInitContainerFromJSONTyped,
    V1PolyaxonInitContainerToJSON,
    V1PolyaxonSidecarContainer,
    V1PolyaxonSidecarContainerFromJSON,
    V1PolyaxonSidecarContainerFromJSONTyped,
    V1PolyaxonSidecarContainerToJSON,
    V1Reference,
    V1ReferenceFromJSON,
    V1ReferenceFromJSONTyped,
    V1ReferenceToJSON,
    V1RunSchema,
    V1RunSchemaFromJSON,
    V1RunSchemaFromJSONTyped,
    V1RunSchemaToJSON,
    V1S3Type,
    V1S3TypeFromJSON,
    V1S3TypeFromJSONTyped,
    V1S3TypeToJSON,
    V1Schedule,
    V1ScheduleFromJSON,
    V1ScheduleFromJSONTyped,
    V1ScheduleToJSON,
    V1ScheduleKind,
    V1ScheduleKindFromJSON,
    V1ScheduleKindFromJSONTyped,
    V1ScheduleKindToJSON,
    V1UriType,
    V1UriTypeFromJSON,
    V1UriTypeFromJSONTyped,
    V1UriTypeToJSON,
    V1WasbType,
    V1WasbTypeFromJSON,
    V1WasbTypeFromJSONTyped,
    V1WasbTypeToJSON,
} from './';

/**
 * 
 * @export
 * @interface V1Schemas
 */
export interface V1Schemas {
    /**
     * 
     * @type {V1EarlyStopping}
     * @memberof V1Schemas
     */
    earlyStopping?: V1EarlyStopping;
    /**
     * 
     * @type {V1Matrix}
     * @memberof V1Schemas
     */
    matrix?: V1Matrix;
    /**
     * 
     * @type {V1RunSchema}
     * @memberof V1Schemas
     */
    run?: V1RunSchema;
    /**
     * 
     * @type {V1Operation}
     * @memberof V1Schemas
     */
    operation?: V1Operation;
    /**
     * 
     * @type {V1CompiledOperation}
     * @memberof V1Schemas
     */
    compiledOperation?: V1CompiledOperation;
    /**
     * 
     * @type {V1Schedule}
     * @memberof V1Schemas
     */
    schedule?: V1Schedule;
    /**
     * 
     * @type {V1ConnectionSchema}
     * @memberof V1Schemas
     */
    connectionSchema?: V1ConnectionSchema;
    /**
     * 
     * @type {V1HpParams}
     * @memberof V1Schemas
     */
    hpParams?: V1HpParams;
    /**
     * 
     * @type {V1Reference}
     * @memberof V1Schemas
     */
    reference?: V1Reference;
    /**
     * 
     * @type {V1ArtifactsMount}
     * @memberof V1Schemas
     */
    artifactsMount?: V1ArtifactsMount;
    /**
     * 
     * @type {V1PolyaxonSidecarContainer}
     * @memberof V1Schemas
     */
    polyaxonSidecarContainer?: V1PolyaxonSidecarContainer;
    /**
     * 
     * @type {V1PolyaxonInitContainer}
     * @memberof V1Schemas
     */
    polyaxonInitContainer?: V1PolyaxonInitContainer;
    /**
     * 
     * @type {V1ArtifactsType}
     * @memberof V1Schemas
     */
    artifacs?: V1ArtifactsType;
    /**
     * 
     * @type {V1WasbType}
     * @memberof V1Schemas
     */
    wasb?: V1WasbType;
    /**
     * 
     * @type {V1GcsType}
     * @memberof V1Schemas
     */
    gcs?: V1GcsType;
    /**
     * 
     * @type {V1S3Type}
     * @memberof V1Schemas
     */
    s3?: V1S3Type;
    /**
     * 
     * @type {V1AuthType}
     * @memberof V1Schemas
     */
    auth?: V1AuthType;
    /**
     * 
     * @type {V1UriType}
     * @memberof V1Schemas
     */
    uri?: V1UriType;
    /**
     * 
     * @type {V1K8sResourceType}
     * @memberof V1Schemas
     */
    k8sResource?: V1K8sResourceType;
    /**
     * 
     * @type {V1ConnectionType}
     * @memberof V1Schemas
     */
    connection?: V1ConnectionType;
    /**
     * 
     * @type {V1EventType}
     * @memberof V1Schemas
     */
    eventType?: V1EventType;
    /**
     * 
     * @type {V1MatrixKind}
     * @memberof V1Schemas
     */
    matrixKind?: V1MatrixKind;
    /**
     * 
     * @type {V1ScheduleKind}
     * @memberof V1Schemas
     */
    scheduleKind?: V1ScheduleKind;
    /**
     * 
     * @type {V1Event}
     * @memberof V1Schemas
     */
    event?: V1Event;
}

export function V1SchemasFromJSON(json: any): V1Schemas {
    return V1SchemasFromJSONTyped(json, false);
}

export function V1SchemasFromJSONTyped(json: any, ignoreDiscriminator: boolean): V1Schemas {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'earlyStopping': !exists(json, 'earlyStopping') ? undefined : V1EarlyStoppingFromJSON(json['earlyStopping']),
        'matrix': !exists(json, 'matrix') ? undefined : V1MatrixFromJSON(json['matrix']),
        'run': !exists(json, 'run') ? undefined : V1RunSchemaFromJSON(json['run']),
        'operation': !exists(json, 'operation') ? undefined : V1OperationFromJSON(json['operation']),
        'compiledOperation': !exists(json, 'compiledOperation') ? undefined : V1CompiledOperationFromJSON(json['compiledOperation']),
        'schedule': !exists(json, 'schedule') ? undefined : V1ScheduleFromJSON(json['schedule']),
        'connectionSchema': !exists(json, 'connectionSchema') ? undefined : V1ConnectionSchemaFromJSON(json['connectionSchema']),
        'hpParams': !exists(json, 'hpParams') ? undefined : V1HpParamsFromJSON(json['hpParams']),
        'reference': !exists(json, 'reference') ? undefined : V1ReferenceFromJSON(json['reference']),
        'artifactsMount': !exists(json, 'artifactsMount') ? undefined : V1ArtifactsMountFromJSON(json['artifactsMount']),
        'polyaxonSidecarContainer': !exists(json, 'polyaxonSidecarContainer') ? undefined : V1PolyaxonSidecarContainerFromJSON(json['polyaxonSidecarContainer']),
        'polyaxonInitContainer': !exists(json, 'polyaxonInitContainer') ? undefined : V1PolyaxonInitContainerFromJSON(json['polyaxonInitContainer']),
        'artifacs': !exists(json, 'artifacs') ? undefined : V1ArtifactsTypeFromJSON(json['artifacs']),
        'wasb': !exists(json, 'wasb') ? undefined : V1WasbTypeFromJSON(json['wasb']),
        'gcs': !exists(json, 'gcs') ? undefined : V1GcsTypeFromJSON(json['gcs']),
        's3': !exists(json, 's3') ? undefined : V1S3TypeFromJSON(json['s3']),
        'auth': !exists(json, 'auth') ? undefined : V1AuthTypeFromJSON(json['auth']),
        'uri': !exists(json, 'uri') ? undefined : V1UriTypeFromJSON(json['uri']),
        'k8sResource': !exists(json, 'k8sResource') ? undefined : V1K8sResourceTypeFromJSON(json['k8sResource']),
        'connection': !exists(json, 'connection') ? undefined : V1ConnectionTypeFromJSON(json['connection']),
        'eventType': !exists(json, 'eventType') ? undefined : V1EventTypeFromJSON(json['eventType']),
        'matrixKind': !exists(json, 'matrixKind') ? undefined : V1MatrixKindFromJSON(json['matrixKind']),
        'scheduleKind': !exists(json, 'scheduleKind') ? undefined : V1ScheduleKindFromJSON(json['scheduleKind']),
        'event': !exists(json, 'event') ? undefined : V1EventFromJSON(json['event']),
    };
}

export function V1SchemasToJSON(value?: V1Schemas | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'earlyStopping': V1EarlyStoppingToJSON(value.earlyStopping),
        'matrix': V1MatrixToJSON(value.matrix),
        'run': V1RunSchemaToJSON(value.run),
        'operation': V1OperationToJSON(value.operation),
        'compiledOperation': V1CompiledOperationToJSON(value.compiledOperation),
        'schedule': V1ScheduleToJSON(value.schedule),
        'connectionSchema': V1ConnectionSchemaToJSON(value.connectionSchema),
        'hpParams': V1HpParamsToJSON(value.hpParams),
        'reference': V1ReferenceToJSON(value.reference),
        'artifactsMount': V1ArtifactsMountToJSON(value.artifactsMount),
        'polyaxonSidecarContainer': V1PolyaxonSidecarContainerToJSON(value.polyaxonSidecarContainer),
        'polyaxonInitContainer': V1PolyaxonInitContainerToJSON(value.polyaxonInitContainer),
        'artifacs': V1ArtifactsTypeToJSON(value.artifacs),
        'wasb': V1WasbTypeToJSON(value.wasb),
        'gcs': V1GcsTypeToJSON(value.gcs),
        's3': V1S3TypeToJSON(value.s3),
        'auth': V1AuthTypeToJSON(value.auth),
        'uri': V1UriTypeToJSON(value.uri),
        'k8sResource': V1K8sResourceTypeToJSON(value.k8sResource),
        'connection': V1ConnectionTypeToJSON(value.connection),
        'eventType': V1EventTypeToJSON(value.eventType),
        'matrixKind': V1MatrixKindToJSON(value.matrixKind),
        'scheduleKind': V1ScheduleKindToJSON(value.scheduleKind),
        'event': V1EventToJSON(value.event),
    };
}


