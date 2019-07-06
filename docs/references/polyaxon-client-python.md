---
title: "Polyaxon Client Python"
sub_link: "polyaxon-client-python"
meta_title: "Polyaxon Client Python Specification - Polyaxon References"
meta_description: "Polyaxon client is python module that can be used to interact with Polyaxon API in a programmatic way."
visibility: public
status: published
tags:
    - client
    - specifications
    - polyaxon
    - sdk
    - python
sidebar: "polyaxon-client-python"
---

Polyaxon client is python module that can be used to interact with Polyaxon API in a programmatic way.

## Install

```bash
$ pip install -U polyaxon-client
```

for python3

```bash
$ pip3 install -U polyaxon-client
```

## Clients

This module includes a client that can be used to interact with Polyaxon API in a programmatic way.


 * [Auth](/references/polyaxon-client-python/auth/): A client for handling authentication and user information.
 * [Cluster](/references/polyaxon-client-python/cluster/): A client for getting cluster and cluster nodes information.
 * [User](/references/polyaxon-client-python/user/): A client to manage users and superuser roles.
 * [Project](/references/polyaxon-client-python/project/): A client for doing CRUD operations on projects, as well as getting and creating experiments and experiment groups, creating and stopping tensorboard/notebook, and uploading code.
 * [Experiment group](/references/polyaxon-client-python/experiment-group/): A client for doing CRUD operations on experiment groups, as well as fetching experiments per group.
 * [Experiment](/references/polyaxon-client-python/experiment/): A client for doing CRUD operations on experiments, as well as statuses, jobs, resources, and logs.
 * [Experiment Job](/references/polyaxon-client-python/experiment-job/): A client for getting information, resources, and logs of experiment jobs.
 * [Job](/references/polyaxon-client-python/job/): A client for getting information, resources, and logs of jobs.
 * [Build Job](/references/polyaxon-client-python/build-job/): A client for getting information, resources, and logs of build jobs.
 * [Bookmark](/references/polyaxon-client-python/bookmark/): A client for getting bookmarks.
 * [Version](/references/polyaxon-client-python/version/): A client to get current and supported versions of several Polyaxon component.


## Usage

```python
from polyaxon_client.client import PolyaxonClient

polyaxon_client = PolyaxonClient(
    host=POLYAXON_IP,
    token=MY_TOKEN, 
    port=POLYAXON_PORT)

polyaxon_client.auth
polyaxon_client.cluster
polyaxon_client.user
polyaxon_client.project
polyaxon_client.experiment
polyaxon_client.experiment_group
polyaxon_client.experiment_job
polyaxon_client.job
polyaxon_client.build_job
polyaxon_client.bookmark
polyaxon_client.version
```

## Authentication

### In-cluster

You can create an instance of `PolyaxonClient` in your code when running a job or experiment in-cluster simply by running:

```python
client = PolyaxonClient()
``` 

Polyaxon provides a context for all its runs enabling users to access scoped token to communicate with the API.

### Locally with an authenticated Polyaxon CLI

If your Polyaxon CLI is authenticated, you can create an instance of `PolyaxonClient` with the CLI authentication information.

e.g.

```python
client = PolyaxonClient()
```

The client will check for the current authenticated user and raise if non found.

### Not in-cluster and no authenticated CLI

When you need to  authenticate a client in an environment outside of a Polyaxon cluster and no authenticated CLI, Polyaxon provides several option:

 * Authenticating with Environment variables:
    
    You can set environment variables containing:
        
        * `POLYAXON_SECRET_USER_TOKEN`
        * `POLYAXON_API_HOST`
        * `POLYAXON_HTTP_PORT`
    
    Once these environment variables are set, you can run:
    
    ```python
    client = PolyaxonClient()
    ```
    
    Authentication using environment variables could be useful to keep you code behave similarly on different environment.
    
 * Provide authentication params:
 
    ```python
    client = PolyaxonClient(token=MY_TOKEN, host=HOST_IP, port=HTTP_PORT, use_https=None, verify_ssl=None)
    ```
 
 * Provide an `ApiConfig` instance:
        
    ```python
    api_config = ApiConfig(token=MY_TOKEN, host=HOST_IP, port=HTTP_PORT, use_https=None, verify_ssl=None)
    client = PolyaxonClient(api_config=api_config)
    ```
