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
import com.google.gson.annotations.SerializedName;

import java.io.IOException;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;

/**
 * Gets or Sets v1CloningKind
 */
@JsonAdapter(V1CloningKind.Adapter.class)
public enum V1CloningKind {
  
  COPY("copy"),
  
  RESTART("restart"),
  
  CACHE("cache"),
  
  SCHEDULE("schedule");

  private String value;

  V1CloningKind(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static V1CloningKind fromValue(String text) {
    for (V1CloningKind b : V1CloningKind.values()) {
      if (String.valueOf(b.value).equals(text)) {
        return b;
      }
    }
    return null;
  }

  public static class Adapter extends TypeAdapter<V1CloningKind> {
    @Override
    public void write(final JsonWriter jsonWriter, final V1CloningKind enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public V1CloningKind read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return V1CloningKind.fromValue(String.valueOf(value));
    }
  }
}

