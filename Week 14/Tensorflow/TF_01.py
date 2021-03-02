# Deep learning libraries - TensorFlow, Microsoft Cognitive Toolkit(CNTK), Theano
# Mutlibackend Keras - Theano, Tensorflow, mxnet
# Keras can be run on Apache MXNet, Apple Core ML, JavaSciprt, Typesciprt - run keras code in web browser, PlaidML (GPU)
# Tensoflow comes bundled with its own Keras implementation tf.keras 
# Keras > Tensorflow > Pytorch (API inspired by Scikit-Learner and Chainer)

import tensorflow as tf
from tensorflow import keras

print(tf.__version__)
print(keras.__version__)

# Load fashion MNIST datasets

fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data() # pixel densities as integers rather than float - different from scikit

print(X_train_full.shape)
print(X_train_full.dtype)

# creating validation set and training neural network using Gradient Descent 

X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:]/ 255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

# MNIST labe = 5 while in Fashin MNIST name them
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

print(class_names[y_train[0]])

# creating the model using Sequential API

model = keras.models.Sequential() # single stack of layers connected sequentially
model.add(keras.layers.Flatten(input_shape=[28, 28])) 
model.add(keras.layers.Dense(300, activation = "relu")) # 300 neuron and ReLU activation functions - other way kers.activation.relu
model.add(keras.layers.Dense(100, activation = "relu")) # 100 neuron and ReLU activation function 
model.add(keras.layers.Dense( 10, activation = "softmax")) # 10 neurson (one per class) and using softmax activation function

""" 
model = keras.models.Sequential([
								 keras.layers.Flatten(input_shape = [28, 28]),
								 keras.layers.Dense(300, activation = "relu"),
								 keras.layers.Dense(100, activation = "relu"),
								 keras.layers.Dense( 10, activation = "softmax")
								 ])
"""

# model summary 
print(model.summary())
print(model.layers)

hidden1 = model.layers[1]
print(hidden1.name)
print(model.get_layer('dense') is hidden1)

# getting parameters of a layer get_weights() and set_weights()

weights, biases = hidden1.get_weights()
print(weights)
print(weights.shape)
print(biases)
print(biases.shape)

# compiling the model 

model.compile(loss = "sparse_categorical_crossentropy",
			  optimizer = "sgd",
			  metrics = ["accuracy"]
			  )
# sigmoid activation if binary classification 

# sgd means simple Stochastic Gradient Descent - keras will perform the backpropagation algorithm i.e. reverse-mode autodiff plus Gradient Descent
# default learning rate lr = 0.01

# Training and evaluating the model
history = model.fit(X_train, y_train, epochs = 5,
					validation_data = (X_valid, y_valid))

import pandas as pd
import matplotlib.pyplot as plt

pd.DataFrame(history.history).plot(figsize = (8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 1) # set the vertical range [0-1]
plt.show()

# tune model hyperparameters /layers, activation function, loss function , learning rate, batch size to increase accuracy of model
print(model.evaluate(X_test, y_test))

X_new = X_test[:3]
y_proba = model.predict(X_new)
print(y_proba.round(2))

y_pred = model.predict_classes(X_new)
print(y_pred)
print(np.array(class_names[y_pred]))

y_new = y_test[:3]
print(y_new)









































