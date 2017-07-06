from __future__ import absolute_import, division, print_function

from sklearn import datasets
from sklearn import model_selection
from sklearn import preprocessing
from tensorflow.python.estimator.inputs.numpy_io import numpy_input_fn

import numpy as np
import polyaxon as plx
import tensorflow as tf


def main(*args):
    """Creates an dqn agent for the openai gym CartPole environment."""

    env = plx.envs.GymEnvironment('CartPole-v0')

    def graph_fn(mode, inputs):
        return plx.layers.FullyConnected(mode, num_units=32)(inputs['state'])

    def model_fn(features, labels, mode):
        model = plx.models.DQNModel(
            mode, graph_fn=graph_fn, loss_config=plx.configs.LossConfig(module='mean_squared_error'),
            num_states=env.num_states, num_actions=env.num_actions,
            optimizer_config=plx.configs.OptimizerConfig(module='sgd', learning_rate=0.01),
            exploration_config=plx.configs.ExplorationConfig(module='random'),
            summaries='all')
        return model(features, labels)

    estimator = plx.estimators.Agent(model_fn=model_fn, memory_config=None, model_dir="/tmp/polyaxon_logs/dqn")

    # Fit
    estimator.train(env)


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run()
