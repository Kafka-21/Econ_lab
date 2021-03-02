# Tensors and operations 

# creating a tensor 

import tensorflow as tf 

t = tf.constant([[1., 2., 3.], [4., 5., 6.]])
print(t)
print(t.shape)
print(t.dtype)
print(tf.constant(42))

# indexing 
print(t[:, 1:])
print(t[..., 1, tf.newaxis])

print(t+10)
print(tf.square(t))
print(t@tf.transpose(t))

# Keras Low level API

from tensorflow import keras
K = keras.backend
print(K.square(K.transpose(t)) + 10)

# creating tensor from numpy
import numpy as np
a = np.array([2., 4., 5.])
print(tf.constant(a))

print(t.numpy())
print(tf.square(a))
print(np.square(t))

# Numpy uses 64 bit precision by default, while Tensor flow uses 32 bit - because 32 bit precision is genearlly more than enough for neural network and runs faster and uses less ram

# Type conversion - no automatic type conversion in tensorflow - error 
print(tf.constant(2) + tf.constant(4))

t2 = tf.constant(40., dtype = tf.float64)
print(tf.constant(2.0) + tf.cast(t2, tf.float32))

# tf.Tensore values are immutable and cannot be modified, hence regular tensors cannot be used for backpropogation 

v = tf.Variable([[1., 2., 3.], [4., 5., 6.]])
print(v)

# using assign to update 
print(v.assign(2 * v))
print(v[0, 1].assign(42))
print(v[:, 2].assign([0., 1.]))
print(v.scatter_nd_update(indices = [[0, 0], [1, 2]], updates = [100., 200.]))











