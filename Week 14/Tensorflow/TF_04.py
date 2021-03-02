from sklearn.datasets import fetch_california_housing 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from tensorflow import keras

housing = fetch_california_housing()

X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_valid = scaler.transform(X_valid)
X_test = scaler.transform(X_test)


# subset of the features through the wide path and a different subset (possibly overlapping) through the deep path 
# sending 5 features through the wide path(features 0 to 4) and 6 features through the deepth path )features 2 to 7

input_A = keras.layers.Input(shape=[5], name="wide_input")
input_B = keras.layers.Input(shape=[6], name="deep_input")
hidden1 = keras.layers.Dense(30, activation="relu")(input_B)
hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)
concat  = keras.layers.concatenate([input_A, hidden2])
output  = keras.layers.Dense(1, name="output")(concat)
model   = keras.Model(inputs=[input_A, input_B], outputs=[output])

model.compile(loss = "mse", optimizer = keras.optimizers.SGD(lr = 1e-3))

X_train_A, X_train_B = X_train[:, :5], X_train[:, 2:]
X_valid_A, X_valid_B = X_valid[:, :5], X_valid[:, 2:]
X_test_A, X_test_B = X_test[:, :5], X_test[:, 2:]
X_new_A, X_new_B = X_test_A[:3], X_test_B[:3]

history  = model.fit((X_train_A, X_train_B), y_train, epochs = 10, validation_data = ((X_valid_A, X_valid_B), y_valid))
mse_test = model.evaluate((X_test_A, X_test_B), y_test)
y_pred   = model.predict((X_new_A, X_new_B))

# mutliple outputs - regression and classification task, mutlitask classification, regularization 

ouput      = keras.layers.Dense(1, name = "main_output")(concat)
aux_output = keras.layers.Dense(1, name = "aux_output")(hidden2)
model 	   = keras.Model(inputs = [input_A, input_B], outputs = [output, aux_output])

# setting loss weight for main output and auxiliary output
model.compile(loss = ["mse", "mse"], loss_weights = [0.9, 0.1], optimizer = "sgd")


# providing labelled output 
history = model.fit(
					[X_train_A, X_train_B], [y_train, y_train], epochs = 20,
					validation_data = ([X_valid_A, X_valid_B], [y_valid, y_valid]))

# losses 

total_loss, main_loss, aux_loss = model.evaluate([X_test_A, X_test_B], [y_test, y_test])
y_pred_main, y_pred_aux = model.predict([X_new_A, X_new_B])


print(y_pred_main)
print(y_pred_aux)

"""
# Saving and Restoring a model

model = keras.models.Sequential([...]) # or keras.Model([...])
model.compile([...])
model.fit([...])
model.save("my_keras_model.h5")

Keras use th HDF5 format - to save both the model's architecture(including every layer's hyperparameters) and the values of all the model parameters for every layer (e.g. connection weights and biases)

# loading a model

model = keras.models.load_model("my_keras_model.h5")

works on Sequential API and functional API, use save_weights() and load_weights() to at least save and restore the model parameters

# callbacks function 

To save model at end of training and save checkpoints at regular intervals during training to avoid losing everything if your computer crashes
ModelCheckpoint callback saves checkpoints of model at regular intervals during training, by default at the end of each epoch
checkpoints_cb = keras.callbacks.ModelCheckpoint("my_keras_model.h5")
history = model.fit(X_train, y_train, epochs = 10, callbacks = [checkpoints_cb])

# saving best only during validation - need not to worry about training for too long and overfitting the training 

checkpoint_cb = keras.callbacks.ModelCheckpint("my_keras_model.h5", save_best_only = True)
history = model.fit(X_Train, y_train, epochs = 10,
					validation_data = (X_valid, y_valid),
					callbacks = [checkpoint_cb])
model = keras.models.load_model("my_keras_model.h5") # roll back to best model

"""
# EarlyStopping callback - interrupt training when it measures no progress on the validation set for a number of epochs
# patince argument - optionall roll back to the best model

early_stopping_cb = keras.callbacks.EarlyStopping(patience = 10, restore_best_weights = True)
history = model.fit(X_train, y_train, epochs = 100,
					validation_data = (X_valid, y_valid),
					callbacks = [checkpoint_cb, early_stopping_cb])

# custom callback to display ratio between validation loss and training loss(to detect overfitting)

class PrintValTrainRatioCallback(keras.callbacks.Callback):
	def on_epoch_end(self, epoch, logs):
		print("\nval/train: {:.2f".format(logs["val_loss"] / logs["loss"]))

























































