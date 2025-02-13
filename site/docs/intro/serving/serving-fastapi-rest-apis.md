---
title: "Serving REST APIs with FastAPI"
sub_link: "serving/serving-fastapi-rest-apis"
meta_title: "Serving REST APIs with FastAPI - Polyaxon quick start tutorial - Core Concepts"
meta_description: "Serving REST APIs with FastAPI - Become familiar with the ecosystem of Polyaxon tools with a top-level overview and useful links to get you started."
visibility: public
status: published
tags:
  - tutorials
  - concepts
  - notebook
  - quick-start
sidebar: "intro"
---

## Overview

In the previous guide we trained several models. In this section we will learn how to deploy a serving REST API with FastAPI.
This is an example of creating a REST API that you can host using Polyaxon, this type of APIs are intended for internal use or for testing purposes 
before moving to a platform that specializes in serving or inference. 

The same principles in this guides can be used to deploy similar REST APIs using any other framework of your choice.

All code and manifests used in this tutorial can be found in this [github repo](https://github.com/polyaxon/polyaxon-ml-serving).

> **Note**: On Polyaxon EE or Polyaxon Cloud, the REST APIs will be protected and can only be accessed by users who have access to your organization following the permissions defined for each member. 

## Logged model

In our training script we used Polyaxon to log a model every time we run an experiment:

```python
# Logging the model
tracking.log_model(model_path, name="iris-model", framework="scikit-learn", versioned=False)
```

## Deploying a serving REST API

We will deploy a simple FastAPI service that will load the best model based on accuracy as an Iris classification RESt API.
Our service will expose two API endpoints, one for returning predictions and one for returning probabilities.


```python
from typing import Dict

import joblib
import numpy as np
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

IRIS_CLASS_MAPPING = {0: "setosa", 1: "versicolor", 2: "virginica"}


def load_model(model_path: str):
    model = open(model_path, "rb")
    return joblib.load(model)


app = FastAPI()
classifier = load_model("./model.joblib")


class DataFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


def get_features(data: DataFeatures) -> np.ndarray:
    return np.array(
        [data.sepal_length, data.sepal_width, data.petal_length, data.petal_width],
        ndmin=2,
    )


def predict(features: np.ndarray, proba: bool = False) -> Dict:
    if proba:
        probabilities = {
            k: float(v)
            for k, v in zip(
                IRIS_CLASS_MAPPING.values(), classifier.predict_proba(features)[0]
            )
        }
        return {"probabilities": probabilities}

    prediction = int(classifier.predict(features)[0])
    return {
        "prediction": {"value": prediction, "class": IRIS_CLASS_MAPPING[prediction]}
    }


@app.post("/api/v1/predict")
async def get_prediction(data: DataFeatures):
    features = get_features(data)
    return predict(features)


@app.post("/api/v1/proba")
async def get_probabilities(data: DataFeatures):
    features = get_features(data)
    return predict(features, proba=True)


@app.get("/", response_class=HTMLResponse)
def index():
    return (
        "<p>Hello, This is a REST API used for Polyaxon ML Serving examples!</p>"
        "<p>Click the fullscreen button the get the URL of your serving API!<p/>"
    )
```

The custom component has a single input, it expects a run uuid, it then loads the model and copy it under the path `polyaxon-ml-serving/fastapi-serving/model.joblib`.

```yaml
version: 1.1
kind: component
name: fastapi-iris-classification
tags: ["fastapi", "api"]

inputs:
- name: uuid
  type: str

run:
  kind: service
  ports: [8000]
  rewritePath: true
  init:
  - git: {"url": "https://github.com/polyaxon/polyaxon-ml-serving"}
  - artifacts: {"files": [["{{ uuid }}/outputs/model/model.joblib", "{{ globals.artifacts_path }}/polyaxon-ml-serving/fastapi-serving/model.joblib"]]}
  container:
    image: polyaxon/polyaxon-examples:ml-serving
    workingDir: "{{ globals.artifacts_path }}/polyaxon-ml-serving/fastapi-serving"
    command: ["sh", "-c"]
    args: ["uvicorn app:app --host 0.0.0.0 --port 8000"]
```

## Scheduling the service

To schedule this REST API with Polyaxon: 

```bash
polyaxon run -f fastapi-serving/polyaxonfile.yaml -P uuid=f8176c9463a345908ce6865c9c7894a9
```

> Note that the uuid `f8176c9463a345908ce6865c9c7894a9` will be different in your use case.

You can now interact with the service using Python or curl. You can get the serving endpoint using the CLI:

```bash
polyaxon ops service --external --url
``` 

You can also retrieve the URL by going to the service tab and click fullscreen:

![serving-api-fullscreen](../../../../content/images/dashboard/runs/serving-api-fullscreen.png)

## Testing the Service

Testing the predictions endpoint:

```bash
curl HOST:PORT/rewrite-services/v1/NAMESPACE/ORG/PROJECT/runs/UUID/api/v1/predict --request POST \
    --header "Content-Type: application/json" \
    --data '{"sepal_length": 2, "sepal_width": 2.5, "petal_length": 2, "petal_width": 0.5}'

{"prediction":{"class":"setosa","value":0}}
```

Testing the probabilities endpoint:

```bash
curl HOST:PORT/rewrite-services/v1/NAMESPACE/ORG/PROJECT/runs/UUID/api/v1/proba \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'

{"prediction":{"class":"setosa","value":0}}
```

Please note that if you are using Polyaxon Cloud or Polyaxon EE you will need to add a header with a [valid auth token](/docs/management/organizations/user-profile/#token-management):

```bash
--header "Authorization: token API_TOKEN"
```

## Saving the custom REST API in the component hub

By adding more parameters to this Rest API, users can save this component to their private hub and allow users to easily schedule the custom API using the CLI/UI.
