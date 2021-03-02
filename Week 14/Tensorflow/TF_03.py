# Building Complex Models using the Functional API

# model connects all or part of inputs directly to the output layer 
# This architecture makes it possible for the neural network to learn both deep patterns(using the deep path) and simples rules (through short path)
# simple patterns in the data end up being distorted by this sequence of transformation 

from tensorflow import keras
from sklearn.datasets import fetch_california_housing 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler

housing = fetch_california_housing()

X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_valid = scaler.transform(X_valid)
X_test = scaler.transform(X_test)

# build neural network

input_  = keras.layers.Input(shape = X_train.shape[1:])
hidden1 = keras.layers.Dense(30, activation = "relu")(input_) # calling like function hence functional API
hidden2 = keras.layers.Dense(30, activation = "relu")(hidden1)
concat  = keras.layers.Concatenate()([input_, hidden2])
output  = keras.layers.Dense(1)(concat) # single layer without any activation function
model   = keras.Model(inputs = [input_], output =[output])

model.compile(loss = "mean_squared_error", optimizer = "sgd")
history = model.fit(X_train, y_train, epochs = 10, validation_data = (X_valid, y_valid))
mse_test = model.evaluate(X_test, y_test)
X_new = X_test[:3] # pretend these are new instances 
y_pred = model.predict(X_new)


print(y_pred)




















