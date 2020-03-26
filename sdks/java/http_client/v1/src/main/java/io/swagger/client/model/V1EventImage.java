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
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * V1EventImage
 */

public class V1EventImage {
  @SerializedName("height")
  private Integer height = null;

  @SerializedName("width")
  private Integer width = null;

  @SerializedName("colorspace")
  private Integer colorspace = null;

  @SerializedName("path")
  private String path = null;

  public V1EventImage height(Integer height) {
    this.height = height;
    return this;
  }

   /**
   * Height of the image.
   * @return height
  **/
  @ApiModelProperty(value = "Height of the image.")
  public Integer getHeight() {
    return height;
  }

  public void setHeight(Integer height) {
    this.height = height;
  }

  public V1EventImage width(Integer width) {
    this.width = width;
    return this;
  }

   /**
   * Width of the image.
   * @return width
  **/
  @ApiModelProperty(value = "Width of the image.")
  public Integer getWidth() {
    return width;
  }

  public void setWidth(Integer width) {
    this.width = width;
  }

  public V1EventImage colorspace(Integer colorspace) {
    this.colorspace = colorspace;
    return this;
  }

   /**
   * Get colorspace
   * @return colorspace
  **/
  @ApiModelProperty(value = "")
  public Integer getColorspace() {
    return colorspace;
  }

  public void setColorspace(Integer colorspace) {
    this.colorspace = colorspace;
  }

  public V1EventImage path(String path) {
    this.path = path;
    return this;
  }

   /**
   * Get path
   * @return path
  **/
  @ApiModelProperty(value = "")
  public String getPath() {
    return path;
  }

  public void setPath(String path) {
    this.path = path;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1EventImage v1EventImage = (V1EventImage) o;
    return Objects.equals(this.height, v1EventImage.height) &&
        Objects.equals(this.width, v1EventImage.width) &&
        Objects.equals(this.colorspace, v1EventImage.colorspace) &&
        Objects.equals(this.path, v1EventImage.path);
  }

  @Override
  public int hashCode() {
    return Objects.hash(height, width, colorspace, path);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1EventImage {\n");
    
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    width: ").append(toIndentedString(width)).append("\n");
    sb.append("    colorspace: ").append(toIndentedString(colorspace)).append("\n");
    sb.append("    path: ").append(toIndentedString(path)).append("\n");
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

