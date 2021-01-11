#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

start_experiment_value = {
    "master": {
        "pod": {
            "api_version": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": None,
                "cluster_name": None,
                "deletion_grace_period_seconds": None,
                "deletion_timestamp": None,
                "finalizers": None,
                "generate_name": None,
                "generation": None,
                "initializers": None,
                "labels": {
                    "experiment": "piko/project1/1",
                    "project_name": "piko/project1",
                    "role": "polyaxon-workers",
                    "experiment_uuid": "fa6203c189a855dd977019854a7ffcc3",
                    "project_uuid": "fa6203c189a855dd977019854a7ffcc3",
                    "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
                    "task_idx": "0",
                    "task_type": "master",
                    "type": "polyaxon-experiment",
                },
                "name": "project1-id1-spec1-xp1-master0",
                "namespace": "polyaxon",
                "owner_references": None,
                "resource_version": "204744",
                "self_link": "/api/v1/namespaces/polyaxon/pods/project1-id1-spec1-xp1-master0",
                "uid": "09c436d4-d87b-11e7-8ab8-1273d6911587",
            },
            "spec": {
                "active_deadline_seconds": None,
                "affinity": None,
                "automount_service_account_token": None,
                "containers": [
                    {
                        "args": [
                            'from polyaxon.polyaxonfile.local_runner import start_experiment_run; start_experiment_run(\'{"version": 1, "project": {"name": "project1"}, "params": {"lr": 1.023292992280754}, "environment": {"n_workers": 1, "n_ps": 1, "run_config": {"save_summary_steps": 100, "save_checkpoints_steps": 100}}, "settings": {"logging": {"level": "INFO", "path": "/tmp/plx/logs/project1"}}, "model": {"classifier": {"loss": {"SigmoidCrossEntropy": null}, "optimizer": {"Adam": {"learning_rate": 1.02329299228}}, "metrics": ["Accuracy", "Precision"], "one_hot_encode": true, "n_classes": 10, "graph": {"input_layers": ["image"], "layers": [{"Conv2D": {"filters": 32, "kernel_size": 3, "strides": 1, "activation": "elu", "regularizer": {"L2": {"l": 0.02}}, "name": "Conv2D_1", "inbound_nodes": ["image"]}}, {"MaxPooling2D": {"pool_size": 2, "name": "MaxPooling2D_1", "inbound_nodes": ["Conv2D_1"]}}, {"Conv2D": {"filters": 64, "kernel_size": 3, "activation": "relu", "regularizer": {"L2": {"l": 0.02}}, "name": "Conv2D_2", "inbound_nodes": ["MaxPooling2D_1"]}}, {"MaxPooling2D": {"pool_size": 2, "name": "MaxPooling2D_2", "inbound_nodes": ["Conv2D_2"]}}, {"Flatten": {"name": "Flatten_1", "inbound_nodes": ["MaxPooling2D_2"]}}, {"Dense": {"units": 128, "activation": "tanh", "name": "Dense_1", "inbound_nodes": ["Flatten_1"]}}, {"Dropout": {"rate": 0.8, "name": "Dropout_1", "inbound_nodes": ["Dense_1"]}}, {"Dense": {"units": 256, "activation": "tanh", "name": "Dense_2", "inbound_nodes": ["Dropout_1"]}}, {"Dropout": {"rate": 0.8, "name": "Dropout_2", "inbound_nodes": ["Dense_2"]}}, {"Dense": {"units": 10, "name": "Dense_3", "inbound_nodes": ["Dropout_2"]}}], "output_layers": ["Dense_3"]}}}, "train": {"steps": 1000, "data_pipeline": {"TFRecordImagePipeline": {"batch_size": 64, "num_epochs": 5, "shuffle": true, "data_files": ["/plx/data/mnist/mnist_train.tfrecord"], "meta_data_file": "/plx/data/mnist/meta_data.json", "feature_processors": {"image": {"input_layers": ["image"], "layers": [{"Cast": {"dtype": "float32", "name": "Cast_1", "inbound_nodes": ["image"]}}], "output_layers": ["Cast_1"]}}}}}, "eval": {"data_pipeline": {"TFRecordImagePipeline": {"batch_size": 32, "num_epochs": 1, "shuffle": false, "data_files": ["/plx/data/mnist/mnist_eval.tfrecord"], "meta_data_file": "/plx/data/mnist/meta_data.json", "feature_processors": {"image": {"input_layers": ["image"], "layers": [{"Cast": {"dtype": "float32", "name": "Cast_1", "inbound_nodes": ["image"]}}], "output_layers": ["Cast_1"]}}}}}}\', \'0\', \'master\', 0, \'train_and_evaluate\')'
                        ],
                        "command": ["python3", "-c"],
                        "env": [
                            {
                                "name": "CM_project1_id1_spec1_xp1_cluster_master",
                                "value": None,
                                "value_from": {
                                    "config_map_key_ref": {
                                        "key": "master",
                                        "name": "project1-id1-spec1-xp1-cluster",
                                        "optional": None,
                                    },
                                    "field_ref": None,
                                    "resource_field_ref": None,
                                    "secret_key_ref": None,
                                },
                            },
                            {
                                "name": "CM_project1_id1_spec1_xp1_cluster_worker",
                                "value": None,
                                "value_from": {
                                    "config_map_key_ref": {
                                        "key": "worker",
                                        "name": "project1-id1-spec1-xp1-cluster",
                                        "optional": None,
                                    },
                                    "field_ref": None,
                                    "resource_field_ref": None,
                                    "secret_key_ref": None,
                                },
                            },
                            {
                                "name": "CM_project1_id1_spec1_xp1_cluster_ps",
                                "value": None,
                                "value_from": {
                                    "config_map_key_ref": {
                                        "key": "ps",
                                        "name": "project1-id1-spec1-xp1-cluster",
                                        "optional": None,
                                    },
                                    "field_ref": None,
                                    "resource_field_ref": None,
                                    "secret_key_ref": None,
                                },
                            },
                        ],
                        "env_from": None,
                        "image": "polyaxon/polyaxon-lib:0.0.1",
                        "image_pull_policy": "IfNotPresent",
                        "lifecycle": None,
                        "liveness_probe": None,
                        "name": "polyaxon-experiment-job",
                        "ports": [
                            {
                                "container_port": 2222,
                                "host_ip": None,
                                "host_port": None,
                                "name": None,
                                "protocol": "TCP",
                            }
                        ],
                        "readiness_probe": None,
                        "resources": {"limits": None, "requests": None},
                        "security_context": None,
                        "stdin": None,
                        "stdin_once": None,
                        "termination_message_path": "/dev/termination-log",
                        "termination_message_policy": "File",
                        "tty": None,
                        "volume_mounts": [
                            {
                                "mount_path": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "default-token-28d2n",
                                "read_only": True,
                                "sub_path": None,
                            }
                        ],
                        "working_dir": None,
                    }
                ],
                "dns_policy": "ClusterFirst",
                "host_aliases": None,
                "host_ipc": None,
                "host_network": None,
                "host_pid": None,
                "hostname": None,
                "image_pull_secrets": None,
                "init_containers": None,
                "node_name": None,
                "node_selector": None,
                "restart_policy": "Never",
                "scheduler_name": "default-scheduler",
                "security_context": {
                    "fs_group": None,
                    "run_as_non_root": None,
                    "run_as_user": None,
                    "se_linux_options": None,
                    "supplemental_groups": None,
                },
                "service_account": "default",
                "service_account_name": "default",
                "subdomain": None,
                "termination_grace_period_seconds": 30,
                "tolerations": None,
                "volumes": [
                    {
                        "aws_elastic_block_store": None,
                        "azure_disk": None,
                        "azure_file": None,
                        "cephfs": None,
                        "cinder": None,
                        "config_map": None,
                        "downward_api": None,
                        "empty_dir": None,
                        "fc": None,
                        "flex_volume": None,
                        "flocker": None,
                        "gce_persistent_disk": None,
                        "git_repo": None,
                        "glusterfs": None,
                        "host_path": None,
                        "iscsi": None,
                        "name": "default-token-28d2n",
                        "nfs": None,
                        "persistent_volume_claim": None,
                        "photon_persistent_disk": None,
                        "portworx_volume": None,
                        "projected": None,
                        "quobyte": None,
                        "rbd": None,
                        "scale_io": None,
                        "secret": {
                            "default_mode": 420,
                            "items": None,
                            "optional": None,
                            "secret_name": "default-token-28d2n",
                        },
                        "storageos": None,
                        "vsphere_volume": None,
                    }
                ],
            },
            "status": {
                "conditions": None,
                "container_statuses": None,
                "host_ip": None,
                "init_container_statuses": None,
                "message": None,
                "phase": "Pending",
                "pod_ip": None,
                "qos_class": "BestEffort",
                "reason": None,
                "start_time": None,
            },
        },
        "service": {
            "api_version": "v1",
            "kind": "Service",
            "metadata": {
                "annotations": None,
                "cluster_name": None,
                "deletion_grace_period_seconds": None,
                "deletion_timestamp": None,
                "finalizers": None,
                "generate_name": None,
                "generation": None,
                "initializers": None,
                "labels": {
                    "experiment": "1",
                    "project": "project1-id1-spec1",
                    "role": "polyaxon-workers",
                    "task": "project1-id1-spec1-xp1-master0",
                    "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
                    "task_idx": "0",
                    "task_type": "master",
                    "type": "polyaxon-experiment",
                },
                "name": "project1-id1-spec1-xp1-master0",
                "namespace": "polyaxon",
                "owner_references": None,
                "resource_version": "204749",
                "self_link": "/api/v1/namespaces/polyaxon/services/project1-id1-spec1-xp1-master0",
                "uid": "09d6006c-d87b-11e7-8ab8-1273d6911587",
            },
            "spec": {
                "cluster_ip": "10.0.0.113",
                "external_i_ps": None,
                "external_name": None,
                "external_traffic_policy": None,
                "health_check_node_port": None,
                "load_balancer_ip": None,
                "load_balancer_source_ranges": None,
                "ports": [
                    {
                        "name": None,
                        "node_port": None,
                        "port": 2222,
                        "protocol": "TCP",
                        "target_port": "2222",
                    }
                ],
                "selector": {
                    "experiment": "1",
                    "project": "project1-id1-spec1",
                    "role": "polyaxon-workers",
                    "task": "project1-id1-spec1-xp1-master0",
                    "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
                    "task_idx": "0",
                    "task_type": "master",
                    "type": "polyaxon-experiment",
                },
                "session_affinity": "None",
                "type": "ClusterIP",
            },
            "status": {"load_balancer": {"ingress": None}},
        },
    },
    "worker": [
        {
            "pod": {
                "api_version": "v1",
                "kind": "Pod",
                "metadata": {
                    "labels": {
                        "experiment": "1",
                        "project": "project1-id1-spec1",
                        "role": "polyaxon-workers",
                        "task": "project1-id1-spec1-xp1-worker0",
                        "run_uuid": "3a9c9b0bd56b5e9fbdbd1a3d43d57960",
                        "task_idx": "0",
                        "task_type": "worker",
                        "type": "polyaxon-experiment",
                    },
                    "name": "project1-id1-spec1-xp1-worker0",
                    "namespace": "polyaxon",
                    "owner_references": None,
                    "resource_version": "204751",
                    "self_link": "/api/v1/namespaces/polyaxon/pods/project1-id1-spec1-xp1-worker0",
                    "uid": "09dcf9eb-d87b-11e7-8ab8-1273d6911587",
                },
                "spec": {
                    "active_deadline_seconds": None,
                    "affinity": None,
                    "automount_service_account_token": None,
                    "containers": [
                        {
                            "args": [
                                'from polyaxon.polyaxonfile.local_runner import start_experiment_run; start_experiment_run(\'{"version": 1, "project": {"name": "project1"}, "params": {"lr": 1.023292992280754}, "environment": {"n_workers": 1, "n_ps": 1, "run_config": {"save_summary_steps": 100, "save_checkpoints_steps": 100}}, "settings": {"logging": {"level": "INFO", "path": "/tmp/plx/logs/project1"}}, "model": {"classifier": {"loss": {"SigmoidCrossEntropy": null}, "optimizer": {"Adam": {"learning_rate": 1.02329299228}}, "metrics": ["Accuracy", "Precision"], "one_hot_encode": true, "n_classes": 10, "graph": {"input_layers": ["image"], "layers": [{"Conv2D": {"filters": 32, "kernel_size": 3, "strides": 1, "activation": "elu", "regularizer": {"L2": {"l": 0.02}}, "name": "Conv2D_1", "inbound_nodes": ["image"]}}, {"MaxPooling2D": {"pool_size": 2, "name": "MaxPooling2D_1", "inbound_nodes": ["Conv2D_1"]}}, {"Conv2D": {"filters": 64, "kernel_size": 3, "activation": "relu", "regularizer": {"L2": {"l": 0.02}}, "name": "Conv2D_2", "inbound_nodes": ["MaxPooling2D_1"]}}, {"MaxPooling2D": {"pool_size": 2, "name": "MaxPooling2D_2", "inbound_nodes": ["Conv2D_2"]}}, {"Flatten": {"name": "Flatten_1", "inbound_nodes": ["MaxPooling2D_2"]}}, {"Dense": {"units": 128, "activation": "tanh", "name": "Dense_1", "inbound_nodes": ["Flatten_1"]}}, {"Dropout": {"rate": 0.8, "name": "Dropout_1", "inbound_nodes": ["Dense_1"]}}, {"Dense": {"units": 256, "activation": "tanh", "name": "Dense_2", "inbound_nodes": ["Dropout_1"]}}, {"Dropout": {"rate": 0.8, "name": "Dropout_2", "inbound_nodes": ["Dense_2"]}}, {"Dense": {"units": 10, "name": "Dense_3", "inbound_nodes": ["Dropout_2"]}}], "output_layers": ["Dense_3"]}}}, "train": {"steps": 1000, "data_pipeline": {"TFRecordImagePipeline": {"batch_size": 64, "num_epochs": 5, "shuffle": true, "data_files": ["/plx/data/mnist/mnist_train.tfrecord"], "meta_data_file": "/plx/data/mnist/meta_data.json", "feature_processors": {"image": {"input_layers": ["image"], "layers": [{"Cast": {"dtype": "float32", "name": "Cast_1", "inbound_nodes": ["image"]}}], "output_layers": ["Cast_1"]}}}}}, "eval": {"data_pipeline": {"TFRecordImagePipeline": {"batch_size": 32, "num_epochs": 1, "shuffle": false, "data_files": ["/plx/data/mnist/mnist_eval.tfrecord"], "meta_data_file": "/plx/data/mnist/meta_data.json", "feature_processors": {"image": {"input_layers": ["image"], "layers": [{"Cast": {"dtype": "float32", "name": "Cast_1", "inbound_nodes": ["image"]}}], "output_layers": ["Cast_1"]}}}}}}\', \'0\', \'worker\', 0, \'train\')'
                            ],
                            "command": ["python3", "-c"],
                            "env": [
                                {
                                    "name": "CM_project1_id1_spec1_xp1_cluster_master",
                                    "value": None,
                                    "value_from": {
                                        "config_map_key_ref": {
                                            "key": "master",
                                            "name": "project1-id1-spec1-xp1-cluster",
                                            "optional": None,
                                        },
                                        "field_ref": None,
                                        "resource_field_ref": None,
                                        "secret_key_ref": None,
                                    },
                                },
                                {
                                    "name": "CM_project1_id1_spec1_xp1_cluster_worker",
                                    "value": None,
                                    "value_from": {
                                        "config_map_key_ref": {
                                            "key": "worker",
                                            "name": "project1-id1-spec1-xp1-cluster",
                                            "optional": None,
                                        },
                                        "field_ref": None,
                                        "resource_field_ref": None,
                                        "secret_key_ref": None,
                                    },
                                },
                                {
                                    "name": "CM_project1_id1_spec1_xp1_cluster_ps",
                                    "value": None,
                                    "value_from": {
                                        "config_map_key_ref": {
                                            "key": "ps",
                                            "name": "project1-id1-spec1-xp1-cluster",
                                            "optional": None,
                                        },
                                        "field_ref": None,
                                        "resource_field_ref": None,
                                        "secret_key_ref": None,
                                    },
                                },
                            ],
                            "env_from": None,
                            "image": "polyaxon/polyaxon-lib:0.0.1",
                            "image_pull_policy": "IfNotPresent",
                            "lifecycle": None,
                            "liveness_probe": None,
                            "name": "polyaxon-experiment-job",
                            "ports": [
                                {
                                    "container_port": 2222,
                                    "host_ip": None,
                                    "host_port": None,
                                    "name": None,
                                    "protocol": "TCP",
                                }
                            ],
                            "readiness_probe": None,
                            "resources": {"limits": None, "requests": None},
                            "security_context": None,
                            "stdin": None,
                            "stdin_once": None,
                            "termination_message_path": "/dev/termination-log",
                            "termination_message_policy": "File",
                            "tty": None,
                            "volume_mounts": [
                                {
                                    "mount_path": "/var/run/secrets/kubernetes.io/serviceaccount",
                                    "name": "default-token-28d2n",
                                    "read_only": True,
                                    "sub_path": None,
                                }
                            ],
                            "working_dir": None,
                        }
                    ],
                    "dns_policy": "ClusterFirst",
                    "host_aliases": None,
                    "host_ipc": None,
                    "host_network": None,
                    "host_pid": None,
                    "hostname": None,
                    "image_pull_secrets": None,
                    "init_containers": None,
                    "node_name": None,
                    "node_selector": None,
                    "restart_policy": "Never",
                    "scheduler_name": "default-scheduler",
                    "security_context": {
                        "fs_group": None,
                        "run_as_non_root": None,
                        "run_as_user": None,
                        "se_linux_options": None,
                        "supplemental_groups": None,
                    },
                    "service_account": "default",
                    "service_account_name": "default",
                    "subdomain": None,
                    "termination_grace_period_seconds": 30,
                    "tolerations": None,
                    "volumes": [
                        {
                            "aws_elastic_block_store": None,
                            "azure_disk": None,
                            "azure_file": None,
                            "cephfs": None,
                            "cinder": None,
                            "config_map": None,
                            "downward_api": None,
                            "empty_dir": None,
                            "fc": None,
                            "flex_volume": None,
                            "flocker": None,
                            "gce_persistent_disk": None,
                            "git_repo": None,
                            "glusterfs": None,
                            "host_path": None,
                            "iscsi": None,
                            "name": "default-token-28d2n",
                            "nfs": None,
                            "persistent_volume_claim": None,
                            "photon_persistent_disk": None,
                            "portworx_volume": None,
                            "projected": None,
                            "quobyte": None,
                            "rbd": None,
                            "scale_io": None,
                            "secret": {
                                "default_mode": 420,
                                "items": None,
                                "optional": None,
                                "secret_name": "default-token-28d2n",
                            },
                            "storageos": None,
                            "vsphere_volume": None,
                        }
                    ],
                },
                "status": {
                    "conditions": None,
                    "container_statuses": None,
                    "host_ip": None,
                    "init_container_statuses": None,
                    "message": None,
                    "phase": "Pending",
                    "pod_ip": None,
                    "qos_class": "BestEffort",
                    "reason": None,
                    "start_time": None,
                },
            },
            "service": {
                "api_version": "v1",
                "kind": "Service",
                "metadata": {
                    "annotations": None,
                    "cluster_name": None,
                    "deletion_grace_period_seconds": None,
                    "deletion_timestamp": None,
                    "finalizers": None,
                    "generate_name": None,
                    "generation": None,
                    "initializers": None,
                    "labels": {
                        "experiment": "1",
                        "project": "project1-id1-spec1",
                        "role": "polyaxon-workers",
                        "task": "project1-id1-spec1-xp1-worker0",
                        "run_uuid": "3a9c9b0bd56b5e9fbdbd1a3d43d57960",
                        "task_idx": "0",
                        "task_type": "worker",
                        "type": "polyaxon-experiment",
                    },
                    "name": "project1-id1-spec1-xp1-worker0",
                    "namespace": "polyaxon",
                    "owner_references": None,
                    "resource_version": "204754",
                    "self_link": "/api/v1/namespaces/polyaxon/services/project1-id1-spec1-xp1-worker0",
                    "uid": "09ebb28e-d87b-11e7-8ab8-1273d6911587",
                },
                "spec": {
                    "cluster_ip": "10.0.0.214",
                    "external_i_ps": None,
                    "external_name": None,
                    "external_traffic_policy": None,
                    "health_check_node_port": None,
                    "load_balancer_ip": None,
                    "load_balancer_source_ranges": None,
                    "ports": [
                        {
                            "name": None,
                            "node_port": None,
                            "port": 2222,
                            "protocol": "TCP",
                            "target_port": "2222",
                        }
                    ],
                    "selector": {
                        "experiment": "1",
                        "project": "project1-id1-spec1",
                        "role": "polyaxon-workers",
                        "task": "project1-id1-spec1-xp1-worker0",
                        "run_uuid": "3a9c9b0bd56b5e9fbdbd1a3d43d57960",
                        "task_idx": "0",
                        "task_type": "worker",
                        "type": "polyaxon-experiment",
                    },
                    "session_affinity": "None",
                    "type": "ClusterIP",
                },
                "status": {"load_balancer": {"ingress": None}},
            },
        }
    ],
    "ps": [
        {
            "pod": {
                "api_version": "v1",
                "kind": "Pod",
                "metadata": {
                    "annotations": None,
                    "cluster_name": None,
                    "deletion_grace_period_seconds": None,
                    "deletion_timestamp": None,
                    "finalizers": None,
                    "generate_name": None,
                    "generation": None,
                    "initializers": None,
                    "labels": {
                        "experiment": "1",
                        "project": "project1-id1-spec1",
                        "role": "polyaxon-workers",
                        "task": "project1-id1-spec1-xp1-ps0",
                        "run_uuid": "59e3601232b85a3d8be2511f23a62945",
                        "task_idx": "0",
                        "task_type": "ps",
                        "type": "polyaxon-experiment",
                    },
                    "name": "project1-id1-spec1-xp1-ps0",
                    "namespace": "polyaxon",
                    "owner_references": None,
                    "resource_version": "204758",
                    "self_link": "/api/v1/namespaces/polyaxon/pods/project1-id1-spec1-xp1-ps0",
                    "uid": "09eea5c3-d87b-11e7-8ab8-1273d6911587",
                },
                "spec": {
                    "active_deadline_seconds": None,
                    "affinity": None,
                    "automount_service_account_token": None,
                    "containers": [
                        {
                            "args": [
                                'from polyaxon.polyaxonfile.local_runner import start_experiment_run; start_experiment_run(\'{"version": 1, "project": {"name": "project1"}, "params": {"lr": 1.023292992280754}, "environment": {"n_workers": 1, "n_ps": 1, "run_config": {"save_summary_steps": 100, "save_checkpoints_steps": 100}}, "settings": {"logging": {"level": "INFO", "path": "/tmp/plx/logs/project1"}}, "model": {"classifier": {"loss": {"SigmoidCrossEntropy": null}, "optimizer": {"Adam": {"learning_rate": 1.02329299228}}, "metrics": ["Accuracy", "Precision"], "one_hot_encode": true, "n_classes": 10, "graph": {"input_layers": ["image"], "layers": [{"Conv2D": {"filters": 32, "kernel_size": 3, "strides": 1, "activation": "elu", "regularizer": {"L2": {"l": 0.02}}, "name": "Conv2D_1", "inbound_nodes": ["image"]}}, {"MaxPooling2D": {"pool_size": 2, "name": "MaxPooling2D_1", "inbound_nodes": ["Conv2D_1"]}}, {"Conv2D": {"filters": 64, "kernel_size": 3, "activation": "relu", "regularizer": {"L2": {"l": 0.02}}, "name": "Conv2D_2", "inbound_nodes": ["MaxPooling2D_1"]}}, {"MaxPooling2D": {"pool_size": 2, "name": "MaxPooling2D_2", "inbound_nodes": ["Conv2D_2"]}}, {"Flatten": {"name": "Flatten_1", "inbound_nodes": ["MaxPooling2D_2"]}}, {"Dense": {"units": 128, "activation": "tanh", "name": "Dense_1", "inbound_nodes": ["Flatten_1"]}}, {"Dropout": {"rate": 0.8, "name": "Dropout_1", "inbound_nodes": ["Dense_1"]}}, {"Dense": {"units": 256, "activation": "tanh", "name": "Dense_2", "inbound_nodes": ["Dropout_1"]}}, {"Dropout": {"rate": 0.8, "name": "Dropout_2", "inbound_nodes": ["Dense_2"]}}, {"Dense": {"units": 10, "name": "Dense_3", "inbound_nodes": ["Dropout_2"]}}], "output_layers": ["Dense_3"]}}}, "train": {"steps": 1000, "data_pipeline": {"TFRecordImagePipeline": {"batch_size": 64, "num_epochs": 5, "shuffle": true, "data_files": ["/plx/data/mnist/mnist_train.tfrecord"], "meta_data_file": "/plx/data/mnist/meta_data.json", "feature_processors": {"image": {"input_layers": ["image"], "layers": [{"Cast": {"dtype": "float32", "name": "Cast_1", "inbound_nodes": ["image"]}}], "output_layers": ["Cast_1"]}}}}}, "eval": {"data_pipeline": {"TFRecordImagePipeline": {"batch_size": 32, "num_epochs": 1, "shuffle": false, "data_files": ["/plx/data/mnist/mnist_eval.tfrecord"], "meta_data_file": "/plx/data/mnist/meta_data.json", "feature_processors": {"image": {"input_layers": ["image"], "layers": [{"Cast": {"dtype": "float32", "name": "Cast_1", "inbound_nodes": ["image"]}}], "output_layers": ["Cast_1"]}}}}}}\', \'0\', \'ps\', 0, \'run_std_server\')'
                            ],
                            "command": ["python3", "-c"],
                            "env": [
                                {
                                    "name": "CM_project1_id1_spec1_xp1_cluster_master",
                                    "value": None,
                                    "value_from": {
                                        "config_map_key_ref": {
                                            "key": "master",
                                            "name": "project1-id1-spec1-xp1-cluster",
                                            "optional": None,
                                        },
                                        "field_ref": None,
                                        "resource_field_ref": None,
                                        "secret_key_ref": None,
                                    },
                                },
                                {
                                    "name": "CM_project1_id1_spec1_xp1_cluster_worker",
                                    "value": None,
                                    "value_from": {
                                        "config_map_key_ref": {
                                            "key": "worker",
                                            "name": "project1-id1-spec1-xp1-cluster",
                                            "optional": None,
                                        },
                                        "field_ref": None,
                                        "resource_field_ref": None,
                                        "secret_key_ref": None,
                                    },
                                },
                                {
                                    "name": "CM_project1_id1_spec1_xp1_cluster_ps",
                                    "value": None,
                                    "value_from": {
                                        "config_map_key_ref": {
                                            "key": "ps",
                                            "name": "project1-id1-spec1-xp1-cluster",
                                            "optional": None,
                                        },
                                        "field_ref": None,
                                        "resource_field_ref": None,
                                        "secret_key_ref": None,
                                    },
                                },
                            ],
                            "env_from": None,
                            "image": "polyaxon/polyaxon-lib:0.0.1",
                            "image_pull_policy": "IfNotPresent",
                            "lifecycle": None,
                            "liveness_probe": None,
                            "name": "polyaxon-experiment-job",
                            "ports": [
                                {
                                    "container_port": 2222,
                                    "host_ip": None,
                                    "host_port": None,
                                    "name": None,
                                    "protocol": "TCP",
                                }
                            ],
                            "readiness_probe": None,
                            "resources": {"limits": None, "requests": None},
                            "security_context": None,
                            "stdin": None,
                            "stdin_once": None,
                            "termination_message_path": "/dev/termination-log",
                            "termination_message_policy": "File",
                            "tty": None,
                            "volume_mounts": [
                                {
                                    "mount_path": "/var/run/secrets/kubernetes.io/serviceaccount",
                                    "name": "default-token-28d2n",
                                    "read_only": True,
                                    "sub_path": None,
                                }
                            ],
                            "working_dir": None,
                        }
                    ],
                    "dns_policy": "ClusterFirst",
                    "host_aliases": None,
                    "host_ipc": None,
                    "host_network": None,
                    "host_pid": None,
                    "hostname": None,
                    "image_pull_secrets": None,
                    "init_containers": None,
                    "node_name": None,
                    "node_selector": None,
                    "restart_policy": "Never",
                    "scheduler_name": "default-scheduler",
                    "security_context": {
                        "fs_group": None,
                        "run_as_non_root": None,
                        "run_as_user": None,
                        "se_linux_options": None,
                        "supplemental_groups": None,
                    },
                    "service_account": "default",
                    "service_account_name": "default",
                    "subdomain": None,
                    "termination_grace_period_seconds": 30,
                    "tolerations": None,
                    "volumes": [
                        {
                            "aws_elastic_block_store": None,
                            "azure_disk": None,
                            "azure_file": None,
                            "cephfs": None,
                            "cinder": None,
                            "config_map": None,
                            "downward_api": None,
                            "empty_dir": None,
                            "fc": None,
                            "flex_volume": None,
                            "flocker": None,
                            "gce_persistent_disk": None,
                            "git_repo": None,
                            "glusterfs": None,
                            "host_path": None,
                            "iscsi": None,
                            "name": "default-token-28d2n",
                            "nfs": None,
                            "persistent_volume_claim": None,
                            "photon_persistent_disk": None,
                            "portworx_volume": None,
                            "projected": None,
                            "quobyte": None,
                            "rbd": None,
                            "scale_io": None,
                            "secret": {
                                "default_mode": 420,
                                "items": None,
                                "optional": None,
                                "secret_name": "default-token-28d2n",
                            },
                            "storageos": None,
                            "vsphere_volume": None,
                        }
                    ],
                },
                "status": {
                    "conditions": None,
                    "container_statuses": None,
                    "host_ip": None,
                    "init_container_statuses": None,
                    "message": None,
                    "phase": "Pending",
                    "pod_ip": None,
                    "qos_class": "BestEffort",
                    "reason": None,
                    "start_time": None,
                },
            },
            "service": {
                "api_version": "v1",
                "kind": "Service",
                "metadata": {
                    "annotations": None,
                    "cluster_name": None,
                    "deletion_grace_period_seconds": None,
                    "deletion_timestamp": None,
                    "finalizers": None,
                    "generate_name": None,
                    "generation": None,
                    "initializers": None,
                    "labels": {
                        "experiment": "1",
                        "project": "project1-id1-spec1",
                        "role": "polyaxon-workers",
                        "task": "project1-id1-spec1-xp1-ps0",
                        "run_uuid": "59e3601232b85a3d8be2511f23a62945",
                        "task_idx": "0",
                        "task_type": "ps",
                        "type": "polyaxon-experiment",
                    },
                    "name": "project1-id1-spec1-xp1-ps0",
                    "namespace": "polyaxon",
                    "owner_references": None,
                    "resource_version": "204760",
                    "self_link": "/api/v1/namespaces/polyaxon/services/project1-id1-spec1-xp1-ps0",
                    "uid": "0a03b8bd-d87b-11e7-8ab8-1273d6911587",
                },
                "spec": {
                    "cluster_ip": "10.0.0.79",
                    "external_i_ps": None,
                    "external_name": None,
                    "external_traffic_policy": None,
                    "health_check_node_port": None,
                    "load_balancer_ip": None,
                    "load_balancer_source_ranges": None,
                    "ports": [
                        {
                            "name": None,
                            "node_port": None,
                            "port": 2222,
                            "protocol": "TCP",
                            "target_port": "2222",
                        }
                    ],
                    "selector": {
                        "experiment": "1",
                        "project": "project1-id1-spec1",
                        "role": "polyaxon-workers",
                        "task": "project1-id1-spec1-xp1-ps0",
                        "run_uuid": "59e3601232b85a3d8be2511f23a62945",
                        "task_idx": "0",
                        "task_type": "ps",
                        "type": "polyaxon-experiment",
                    },
                    "session_affinity": "None",
                    "type": "ClusterIP",
                },
                "status": {"load_balancer": {"ingress": None}},
            },
        }
    ],
}


def get_status_event(name, container_name, labels):
    event = {
        "type": "ADDED",
        "object": {
            "api_version": "v1",
            "kind": "Pod",
            "metadata": {
                "deletion_timestamp": None,
                "name": name,
                "namespace": "polyaxon",
                "owner_references": None,
                "resource_version": "277329",
                "self_link": "/api/v1/namespaces/polyaxon/pods/project1-id1-spec1-xp1-master0",
                "uid": "05062d42-d915-11e7-8ab8-1273d6911587",
                "labels": labels,
            },
            "spec": {
                "containers": [
                    {
                        "command": ["python3", "-c"],
                        "env": [],
                        "image": "busybox/busybox",
                        "image_pull_policy": "IfNotPresent",
                        "lifecycle": None,
                        "liveness_probe": None,
                        "name": container_name,
                        "ports": [
                            {
                                "container_port": 2222,
                                "host_ip": None,
                                "host_port": None,
                                "name": None,
                                "protocol": "TCP",
                            }
                        ],
                        "readiness_probe": None,
                    }
                ],
                "volumes": [],
                "node_name": None,
            },
            "status": {
                "conditions": None,
                "container_statuses": None,
                "host_ip": None,
                "init_container_statuses": None,
                "message": None,
                "phase": "Pending",
                "pod_ip": None,
                "qos_class": "BestEffort",
                "reason": None,
                "start_time": None,
            },
        },
    }
    return event


def get_status_event_with_conditions(name, container_name, labels):
    event = get_status_event(name, container_name, labels)
    event["object"]["status"] = {
        "conditions": [
            {
                "last_probe_time": None,
                "message": None,
                "reason": None,
                "status": "True",
                "type": "Initialized",
            },
            {
                "last_probe_time": None,
                "message": "containers with unready status: [{}]".format(
                    container_name
                ),
                "reason": "ContainersNotReady",
                "status": "False",
                "type": "Ready",
            },
            {
                "last_probe_time": None,
                "message": None,
                "reason": None,
                "status": "True",
                "type": "PodScheduled",
            },
        ],
        "container_statuses": [
            {
                "container_id": "docker://539e6a6f4209997094802b0657f90576fe129b7f81697120172836073d9bbd75",
                "image": "busybox/busybox",
                "image_id": "docker://sha256:c66a51ffd71e2ec0cb0699dba06283bce9d254e2833a84ce7378298b04297ba3",
                "last_state": {"running": None, "terminated": None, "waiting": None},
                "name": container_name,
                "ready": False,
                "restart_count": 0,
                "state": {
                    "running": 1,  # This is changed to get the test to check container monitoring
                    "terminated": {
                        "container_id": "docker://539e6a6f4209997094802b0657f90576fe129b7f81697120172836073d9bbd75",
                        "exit_code": 1,
                        "message": None,
                        "reason": "Error",
                        "signal": None,
                    },
                    "waiting": None,
                },
            }
        ],
        "host_ip": "192.168.64.4",
        "init_container_statuses": None,
        "message": None,
        "phase": "Failed",
        "pod_ip": "172.17.0.2",
        "qos_class": "BestEffort",
        "reason": None,
    }
    return event


status_experiment_job_event = get_status_event(
    name="project1-id1-spec1-xp1-master0",
    container_name="polyaxon-experiment-job",
    labels={
        "app": "polyaxon-experiment",
        "project_name": "mike/project1",
        "experiment_name": "mike/project1/1",
        "project_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "experiment_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "task_idx": "0",
        "task_type": "master",
        "role": "polyaxon-workers",
        "type": "polyaxon-runner",
    },
)

status_experiment_job_event_with_conditions = get_status_event_with_conditions(
    name="project1-id1-spec1-xp1-master0",
    container_name="polyaxon-experiment-job",
    labels={
        "app": "polyaxon-experiment",
        "project_name": "mike/project1",
        "experiment_name": "mike/project1/1",
        "project_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "experiment_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "task_idx": "0",
        "task_type": "master",
        "role": "polyaxon-workers",
        "type": "polyaxon-runner",
    },
)

status_job_event = get_status_event(
    name="plxproject-project_uuid-notebook",
    container_name="polyaxon-job",
    labels={
        "app": "polyaxon-job",
        "project_name": "mike/project1",
        "project_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "run_name": "mike/project1/jobs/1",
        "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "role": "polyaxon-workers",
        "type": "polyaxon-runner",
    },
)

status_notebook_job_event = get_status_event(
    name="plxproject-project_uuid-notebook",
    container_name="polyaxon-plugin-job",
    labels={
        "app": "polyaxon-notebook",
        "project_name": "mike/project1",
        "project_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "run_name": "mike/project1/notebook/1",
        "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "role": "polyaxon-dashboard",
        "type": "polyaxon-runner",
    },
)

status_notebook_job_event_with_conditions = get_status_event_with_conditions(
    name="plxproject-project_uuid-notebook",
    container_name="polyaxon-plugin-job",
    labels={
        "app": "polyaxon-notebook",
        "project_name": "mike/project1",
        "project_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "run_name": "mike/project1/notebook/1",
        "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "role": "polyaxon-dashboard",
        "type": "polyaxon-runner",
    },
)

status_tensorboard_job_event = get_status_event(
    name="plxproject-project_uuid-tensroboard",
    container_name="polyaxon-plugin-job",
    labels={
        "app": "polyaxon-tensorboard",
        "project_name": "mike/project1",
        "project_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "run_name": "mike/project1/tensorboards/1",
        "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "role": "polyaxon-dashboard",
        "type": "polyaxon-runner",
    },
)

status_job_event_with_conditions = get_status_event_with_conditions(
    name="plxproject-project_uuid-job",
    container_name="polyaxon-job",
    labels={
        "app": "polyaxon-job",
        "project_name": "mike/project1",
        "project_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "run_name": "mike/project1/jobs/1",
        "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "role": "polyaxon-workers",
        "type": "polyaxon-runner",
    },
)

status_tensorboard_job_event_with_conditions = get_status_event_with_conditions(
    name="plxproject-project_uuid-tensroboard",
    container_name="polyaxon-plugin-job",
    labels={
        "app": "polyaxon-tensorboard",
        "project_name": "mike/project1",
        "project_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "run_name": "mike/project1/tensorboards/1",
        "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "role": "polyaxon-dashboard",
        "type": "polyaxon-runner",
    },
)

status_build_job_event = get_status_event(
    name="plxproject-project_uuid-build",
    container_name="polyaxon-dockerizer-job",
    labels={
        "app": "polyaxon-dockerizer",
        "project_name": "mike/project1",
        "project_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "run_name": "mike/project1/builds/1",
        "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "role": "polyaxon-dashboard",
        "type": "polyaxon-runner",
    },
)

status_build_job_event_with_conditions = get_status_event_with_conditions(
    name="plxproject-project_uuid-build",
    container_name="polyaxon-dockerizer-job",
    labels={
        "app": "polyaxon-dockerizer",
        "project_name": "mike/project1",
        "project_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "run_name": "mike/project1/builds/1",
        "run_uuid": "fa6203c189a855dd977019854a7ffcc3",
        "role": "polyaxon-dashboard",
        "type": "polyaxon-runner",
    },
)
