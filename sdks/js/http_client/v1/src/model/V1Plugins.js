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
import V1Notification from './V1Notification';
import V1PolyaxonSidecarContainer from './V1PolyaxonSidecarContainer';

/**
 * The V1Plugins model module.
 * @module model/V1Plugins
 * @version 1.10.1
 */
class V1Plugins {
    /**
     * Constructs a new <code>V1Plugins</code>.
     * @alias module:model/V1Plugins
     */
    constructor() { 
        
        V1Plugins.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>V1Plugins</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/V1Plugins} obj Optional instance to populate.
     * @return {module:model/V1Plugins} The populated <code>V1Plugins</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new V1Plugins();

            if (data.hasOwnProperty('auth')) {
                obj['auth'] = ApiClient.convertToType(data['auth'], 'Boolean');
            }
            if (data.hasOwnProperty('docker')) {
                obj['docker'] = ApiClient.convertToType(data['docker'], 'Boolean');
            }
            if (data.hasOwnProperty('shm')) {
                obj['shm'] = ApiClient.convertToType(data['shm'], 'Boolean');
            }
            if (data.hasOwnProperty('mountArtifactsStore')) {
                obj['mountArtifactsStore'] = ApiClient.convertToType(data['mountArtifactsStore'], 'Boolean');
            }
            if (data.hasOwnProperty('collectArtifacts')) {
                obj['collectArtifacts'] = ApiClient.convertToType(data['collectArtifacts'], 'Boolean');
            }
            if (data.hasOwnProperty('collectLogs')) {
                obj['collectLogs'] = ApiClient.convertToType(data['collectLogs'], 'Boolean');
            }
            if (data.hasOwnProperty('collectResources')) {
                obj['collectResources'] = ApiClient.convertToType(data['collectResources'], 'String');
            }
            if (data.hasOwnProperty('syncStatuses')) {
                obj['syncStatuses'] = ApiClient.convertToType(data['syncStatuses'], 'Boolean');
            }
            if (data.hasOwnProperty('autoResume')) {
                obj['autoResume'] = ApiClient.convertToType(data['autoResume'], 'Boolean');
            }
            if (data.hasOwnProperty('logLevel')) {
                obj['logLevel'] = ApiClient.convertToType(data['logLevel'], 'String');
            }
            if (data.hasOwnProperty('externalHost')) {
                obj['externalHost'] = ApiClient.convertToType(data['externalHost'], 'Boolean');
            }
            if (data.hasOwnProperty('sidecar')) {
                obj['sidecar'] = V1PolyaxonSidecarContainer.constructFromObject(data['sidecar']);
            }
            if (data.hasOwnProperty('notifications')) {
                obj['notifications'] = ApiClient.convertToType(data['notifications'], [V1Notification]);
            }
        }
        return obj;
    }


}

/**
 * @member {Boolean} auth
 */
V1Plugins.prototype['auth'] = undefined;

/**
 * @member {Boolean} docker
 */
V1Plugins.prototype['docker'] = undefined;

/**
 * @member {Boolean} shm
 */
V1Plugins.prototype['shm'] = undefined;

/**
 * @member {Boolean} mountArtifactsStore
 */
V1Plugins.prototype['mountArtifactsStore'] = undefined;

/**
 * @member {Boolean} collectArtifacts
 */
V1Plugins.prototype['collectArtifacts'] = undefined;

/**
 * @member {Boolean} collectLogs
 */
V1Plugins.prototype['collectLogs'] = undefined;

/**
 * @member {String} collectResources
 */
V1Plugins.prototype['collectResources'] = undefined;

/**
 * @member {Boolean} syncStatuses
 */
V1Plugins.prototype['syncStatuses'] = undefined;

/**
 * @member {Boolean} autoResume
 */
V1Plugins.prototype['autoResume'] = undefined;

/**
 * @member {String} logLevel
 */
V1Plugins.prototype['logLevel'] = undefined;

/**
 * @member {Boolean} externalHost
 */
V1Plugins.prototype['externalHost'] = undefined;

/**
 * @member {module:model/V1PolyaxonSidecarContainer} sidecar
 */
V1Plugins.prototype['sidecar'] = undefined;

/**
 * @member {Array.<module:model/V1Notification>} notifications
 */
V1Plugins.prototype['notifications'] = undefined;






export default V1Plugins;

