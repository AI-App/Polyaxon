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
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.PolyaxonSdk);
  }
}(this, function(expect, PolyaxonSdk) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('V1Dag', function() {
      beforeEach(function() {
        instance = new PolyaxonSdk.V1Dag();
      });

      it('should create an instance of V1Dag', function() {
        // TODO: update the code to test V1Dag
        expect(instance).to.be.a(PolyaxonSdk.V1Dag);
      });

      it('should have the property kind (base name: "kind")', function() {
        // TODO: update the code to test the property kind
        expect(instance).to.have.property('kind');
        // expect(instance.kind).to.be(expectedValueLiteral);
      });

      it('should have the property operations (base name: "operations")', function() {
        // TODO: update the code to test the property operations
        expect(instance).to.have.property('operations');
        // expect(instance.operations).to.be(expectedValueLiteral);
      });

      it('should have the property components (base name: "components")', function() {
        // TODO: update the code to test the property components
        expect(instance).to.have.property('components');
        // expect(instance.components).to.be(expectedValueLiteral);
      });

      it('should have the property concurrency (base name: "concurrency")', function() {
        // TODO: update the code to test the property concurrency
        expect(instance).to.have.property('concurrency');
        // expect(instance.concurrency).to.be(expectedValueLiteral);
      });

      it('should have the property early_stopping (base name: "early_stopping")', function() {
        // TODO: update the code to test the property early_stopping
        expect(instance).to.have.property('early_stopping');
        // expect(instance.early_stopping).to.be(expectedValueLiteral);
      });

      it('should have the property environment (base name: "environment")', function() {
        // TODO: update the code to test the property environment
        expect(instance).to.have.property('environment');
        // expect(instance.environment).to.be(expectedValueLiteral);
      });

      it('should have the property connections (base name: "connections")', function() {
        // TODO: update the code to test the property connections
        expect(instance).to.have.property('connections');
        // expect(instance.connections).to.be(expectedValueLiteral);
      });

      it('should have the property volumes (base name: "volumes")', function() {
        // TODO: update the code to test the property volumes
        expect(instance).to.have.property('volumes');
        // expect(instance.volumes).to.be(expectedValueLiteral);
      });

    });
  });

}));
