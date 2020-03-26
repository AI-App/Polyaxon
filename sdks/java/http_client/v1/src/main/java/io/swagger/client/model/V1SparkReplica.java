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
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.kubernetes.client.openapi.models.V1Container;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.client.model.V1Environment;
import io.swagger.client.model.V1Init;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * V1SparkReplica
 */

public class V1SparkReplica {
  @SerializedName("replicas")
  private Integer replicas = null;

  @SerializedName("environment")
  private V1Environment environment = null;

  @SerializedName("init")
  private List<V1Init> init = null;

  @SerializedName("sidecars")
  private List<V1Container> sidecars = null;

  @SerializedName("container")
  private V1Container container = null;

  public V1SparkReplica replicas(Integer replicas) {
    this.replicas = replicas;
    return this;
  }

   /**
   * Get replicas
   * @return replicas
  **/
  @ApiModelProperty(value = "")
  public Integer getReplicas() {
    return replicas;
  }

  public void setReplicas(Integer replicas) {
    this.replicas = replicas;
  }

  public V1SparkReplica environment(V1Environment environment) {
    this.environment = environment;
    return this;
  }

   /**
   * Get environment
   * @return environment
  **/
  @ApiModelProperty(value = "")
  public V1Environment getEnvironment() {
    return environment;
  }

  public void setEnvironment(V1Environment environment) {
    this.environment = environment;
  }

  public V1SparkReplica init(List<V1Init> init) {
    this.init = init;
    return this;
  }

  public V1SparkReplica addInitItem(V1Init initItem) {
    if (this.init == null) {
      this.init = new ArrayList<V1Init>();
    }
    this.init.add(initItem);
    return this;
  }

   /**
   * Get init
   * @return init
  **/
  @ApiModelProperty(value = "")
  public List<V1Init> getInit() {
    return init;
  }

  public void setInit(List<V1Init> init) {
    this.init = init;
  }

  public V1SparkReplica sidecars(List<V1Container> sidecars) {
    this.sidecars = sidecars;
    return this;
  }

  public V1SparkReplica addSidecarsItem(V1Container sidecarsItem) {
    if (this.sidecars == null) {
      this.sidecars = new ArrayList<V1Container>();
    }
    this.sidecars.add(sidecarsItem);
    return this;
  }

   /**
   * Get sidecars
   * @return sidecars
  **/
  @ApiModelProperty(value = "")
  public List<V1Container> getSidecars() {
    return sidecars;
  }

  public void setSidecars(List<V1Container> sidecars) {
    this.sidecars = sidecars;
  }

  public V1SparkReplica container(V1Container container) {
    this.container = container;
    return this;
  }

   /**
   * Get container
   * @return container
  **/
  @ApiModelProperty(value = "")
  public V1Container getContainer() {
    return container;
  }

  public void setContainer(V1Container container) {
    this.container = container;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1SparkReplica v1SparkReplica = (V1SparkReplica) o;
    return Objects.equals(this.replicas, v1SparkReplica.replicas) &&
        Objects.equals(this.environment, v1SparkReplica.environment) &&
        Objects.equals(this.init, v1SparkReplica.init) &&
        Objects.equals(this.sidecars, v1SparkReplica.sidecars) &&
        Objects.equals(this.container, v1SparkReplica.container);
  }

  @Override
  public int hashCode() {
    return Objects.hash(replicas, environment, init, sidecars, container);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1SparkReplica {\n");
    
    sb.append("    replicas: ").append(toIndentedString(replicas)).append("\n");
    sb.append("    environment: ").append(toIndentedString(environment)).append("\n");
    sb.append("    init: ").append(toIndentedString(init)).append("\n");
    sb.append("    sidecars: ").append(toIndentedString(sidecars)).append("\n");
    sb.append("    container: ").append(toIndentedString(container)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

