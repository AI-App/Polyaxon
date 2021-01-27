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

/*
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


package org.openapitools.client.model;

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
import org.threeten.bp.OffsetDateTime;

/**
 * V1Activity
 */

public class V1Activity {
  public static final String SERIALIZED_NAME_ACTOR = "actor";
  @SerializedName(SERIALIZED_NAME_ACTOR)
  private String actor;

  public static final String SERIALIZED_NAME_OWNER = "owner";
  @SerializedName(SERIALIZED_NAME_OWNER)
  private String owner;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_EVENT_ACTION = "event_action";
  @SerializedName(SERIALIZED_NAME_EVENT_ACTION)
  private String eventAction;

  public static final String SERIALIZED_NAME_EVENT_SUBJECT = "event_subject";
  @SerializedName(SERIALIZED_NAME_EVENT_SUBJECT)
  private String eventSubject;

  public static final String SERIALIZED_NAME_OBJECT_NAME = "object_name";
  @SerializedName(SERIALIZED_NAME_OBJECT_NAME)
  private String objectName;

  public static final String SERIALIZED_NAME_OBJECT_UUID = "object_uuid";
  @SerializedName(SERIALIZED_NAME_OBJECT_UUID)
  private String objectUuid;

  public static final String SERIALIZED_NAME_OBJECT_PARENT = "object_parent";
  @SerializedName(SERIALIZED_NAME_OBJECT_PARENT)
  private String objectParent;


  public V1Activity actor(String actor) {
    
    this.actor = actor;
    return this;
  }

   /**
   * Get actor
   * @return actor
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getActor() {
    return actor;
  }


  public void setActor(String actor) {
    this.actor = actor;
  }


  public V1Activity owner(String owner) {
    
    this.owner = owner;
    return this;
  }

   /**
   * Get owner
   * @return owner
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getOwner() {
    return owner;
  }


  public void setOwner(String owner) {
    this.owner = owner;
  }


  public V1Activity createdAt(OffsetDateTime createdAt) {
    
    this.createdAt = createdAt;
    return this;
  }

   /**
   * Get createdAt
   * @return createdAt
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }


  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public V1Activity eventAction(String eventAction) {
    
    this.eventAction = eventAction;
    return this;
  }

   /**
   * Get eventAction
   * @return eventAction
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getEventAction() {
    return eventAction;
  }


  public void setEventAction(String eventAction) {
    this.eventAction = eventAction;
  }


  public V1Activity eventSubject(String eventSubject) {
    
    this.eventSubject = eventSubject;
    return this;
  }

   /**
   * Get eventSubject
   * @return eventSubject
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getEventSubject() {
    return eventSubject;
  }


  public void setEventSubject(String eventSubject) {
    this.eventSubject = eventSubject;
  }


  public V1Activity objectName(String objectName) {
    
    this.objectName = objectName;
    return this;
  }

   /**
   * Get objectName
   * @return objectName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getObjectName() {
    return objectName;
  }


  public void setObjectName(String objectName) {
    this.objectName = objectName;
  }


  public V1Activity objectUuid(String objectUuid) {
    
    this.objectUuid = objectUuid;
    return this;
  }

   /**
   * Get objectUuid
   * @return objectUuid
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getObjectUuid() {
    return objectUuid;
  }


  public void setObjectUuid(String objectUuid) {
    this.objectUuid = objectUuid;
  }


  public V1Activity objectParent(String objectParent) {
    
    this.objectParent = objectParent;
    return this;
  }

   /**
   * Get objectParent
   * @return objectParent
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getObjectParent() {
    return objectParent;
  }


  public void setObjectParent(String objectParent) {
    this.objectParent = objectParent;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1Activity v1Activity = (V1Activity) o;
    return Objects.equals(this.actor, v1Activity.actor) &&
        Objects.equals(this.owner, v1Activity.owner) &&
        Objects.equals(this.createdAt, v1Activity.createdAt) &&
        Objects.equals(this.eventAction, v1Activity.eventAction) &&
        Objects.equals(this.eventSubject, v1Activity.eventSubject) &&
        Objects.equals(this.objectName, v1Activity.objectName) &&
        Objects.equals(this.objectUuid, v1Activity.objectUuid) &&
        Objects.equals(this.objectParent, v1Activity.objectParent);
  }

  @Override
  public int hashCode() {
    return Objects.hash(actor, owner, createdAt, eventAction, eventSubject, objectName, objectUuid, objectParent);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1Activity {\n");
    sb.append("    actor: ").append(toIndentedString(actor)).append("\n");
    sb.append("    owner: ").append(toIndentedString(owner)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    eventAction: ").append(toIndentedString(eventAction)).append("\n");
    sb.append("    eventSubject: ").append(toIndentedString(eventSubject)).append("\n");
    sb.append("    objectName: ").append(toIndentedString(objectName)).append("\n");
    sb.append("    objectUuid: ").append(toIndentedString(objectUuid)).append("\n");
    sb.append("    objectParent: ").append(toIndentedString(objectParent)).append("\n");
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

