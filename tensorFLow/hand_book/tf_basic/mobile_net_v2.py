import tensorflow as tf
import tensorflow_datasets as tfds

num_batchs = 1000
batch_size = 50
learning_rate = 0.001

dataset = tfds.load("tf_flowers",split = tfds.Split.TRAIN,as_supervised=True)

