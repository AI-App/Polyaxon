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
    define(['ApiClient', 'model/V1OptimizationMetric', 'model/V1OptimizationResource'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./V1OptimizationMetric'), require('./V1OptimizationResource'));
  } else {
    // Browser globals (root is window)
    if (!root.PolyaxonSdk) {
      root.PolyaxonSdk = {};
    }
    root.PolyaxonSdk.V1Hyperband = factory(root.PolyaxonSdk.ApiClient, root.PolyaxonSdk.V1OptimizationMetric, root.PolyaxonSdk.V1OptimizationResource);
  }
}(this, function(ApiClient, V1OptimizationMetric, V1OptimizationResource) {
  'use strict';

  /**
   * The V1Hyperband model module.
   * @module model/V1Hyperband
   * @version 1.0.7
   */

  /**
   * Constructs a new <code>V1Hyperband</code>.
   * @alias module:model/V1Hyperband
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>V1Hyperband</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/V1Hyperband} obj Optional instance to populate.
   * @return {module:model/V1Hyperband} The populated <code>V1Hyperband</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('kind'))
        obj.kind = ApiClient.convertToType(data['kind'], 'String');
      if (data.hasOwnProperty('params'))
        obj.params = ApiClient.convertToType(data['params'], {'String': Object});
      if (data.hasOwnProperty('max_iterations'))
        obj.max_iterations = ApiClient.convertToType(data['max_iterations'], 'Number');
      if (data.hasOwnProperty('eta'))
        obj.eta = ApiClient.convertToType(data['eta'], 'Number');
      if (data.hasOwnProperty('resource'))
        obj.resource = V1OptimizationResource.constructFromObject(data['resource']);
      if (data.hasOwnProperty('metric'))
        obj.metric = V1OptimizationMetric.constructFromObject(data['metric']);
      if (data.hasOwnProperty('resume'))
        obj.resume = ApiClient.convertToType(data['resume'], 'Boolean');
      if (data.hasOwnProperty('seed'))
        obj.seed = ApiClient.convertToType(data['seed'], 'Number');
      if (data.hasOwnProperty('concurrency'))
        obj.concurrency = ApiClient.convertToType(data['concurrency'], 'Number');
      if (data.hasOwnProperty('early_stopping'))
        obj.early_stopping = ApiClient.convertToType(data['early_stopping'], [Object]);
    }
    return obj;
  }

  /**
   * @member {String} kind
   * @default 'hyperband'
   */
  exports.prototype.kind = 'hyperband';

  /**
   * @member {Object.<String, Object>} params
   */
  exports.prototype.params = undefined;

  /**
   * @member {Number} max_iterations
   */
  exports.prototype.max_iterations = undefined;

  /**
   * @member {Number} eta
   */
  exports.prototype.eta = undefined;

  /**
   * @member {module:model/V1OptimizationResource} resource
   */
  exports.prototype.resource = undefined;

  /**
   * @member {module:model/V1OptimizationMetric} metric
   */
  exports.prototype.metric = undefined;

  /**
   * @member {Boolean} resume
   */
  exports.prototype.resume = undefined;

  /**
   * @member {Number} seed
   */
  exports.prototype.seed = undefined;

  /**
   * @member {Number} concurrency
   */
  exports.prototype.concurrency = undefined;

  /**
   * @member {Array.<Object>} early_stopping
   */
  exports.prototype.early_stopping = undefined;

  return exports;

}));
