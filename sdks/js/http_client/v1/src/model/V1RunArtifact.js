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
 *
 * Swagger Codegen version: 2.4.10
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/V1ArtifactKind'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./V1ArtifactKind'));
  } else {
    // Browser globals (root is window)
    if (!root.PolyaxonSdk) {
      root.PolyaxonSdk = {};
    }
    root.PolyaxonSdk.V1RunArtifact = factory(root.PolyaxonSdk.ApiClient, root.PolyaxonSdk.V1ArtifactKind);
  }
}(this, function(ApiClient, V1ArtifactKind) {
  'use strict';

  /**
   * The V1RunArtifact model module.
   * @module model/V1RunArtifact
   * @version 1.0.7
   */

  /**
   * Constructs a new <code>V1RunArtifact</code>.
   * @alias module:model/V1RunArtifact
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>V1RunArtifact</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/V1RunArtifact} obj Optional instance to populate.
   * @return {module:model/V1RunArtifact} The populated <code>V1RunArtifact</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('name'))
        obj.name = ApiClient.convertToType(data['name'], 'String');
      if (data.hasOwnProperty('state'))
        obj.state = ApiClient.convertToType(data['state'], 'String');
      if (data.hasOwnProperty('kind'))
        obj.kind = V1ArtifactKind.constructFromObject(data['kind']);
      if (data.hasOwnProperty('path'))
        obj.path = ApiClient.convertToType(data['path'], 'String');
      if (data.hasOwnProperty('connection'))
        obj.connection = ApiClient.convertToType(data['connection'], 'String');
      if (data.hasOwnProperty('summary'))
        obj.summary = ApiClient.convertToType(data['summary'], Object);
      if (data.hasOwnProperty('is_input'))
        obj.is_input = ApiClient.convertToType(data['is_input'], 'Boolean');
    }
    return obj;
  }

  /**
   * @member {String} name
   */
  exports.prototype.name = undefined;

  /**
   * @member {String} state
   */
  exports.prototype.state = undefined;

  /**
   * @member {module:model/V1ArtifactKind} kind
   */
  exports.prototype.kind = undefined;

  /**
   * @member {String} path
   */
  exports.prototype.path = undefined;

  /**
   * @member {String} connection
   */
  exports.prototype.connection = undefined;

  /**
   * @member {Object} summary
   */
  exports.prototype.summary = undefined;

  /**
   * @member {Boolean} is_input
   */
  exports.prototype.is_input = undefined;

  return exports;

}));
