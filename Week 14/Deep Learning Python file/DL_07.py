# Convultional LSTM 

model = tf.keras.models.Sequential([
	    tf.keras.layers.Conv1D(filters=32, kernel_size=5,
	    	                   strides=1, padding="casual",
	    	                   activation="relu"
	    	                   input_shape=[None,1]),
	    tf.keras.layers.LSTM(32, return_sequences=True),
	    tf.keras.layers.LSTM(32, return_sequences=True),
	    tf.keras.layers.Dense(1),
	    tf.keras.layers.Lambda(lambda x: x * 200)
	    ])

optimizer = tf.keras.optimizers.SGD(1r=1e-5, momentum=0.9)
model.compile(loss=tf.keras.losses.Huber(),optimizer= optimizer, metrics=["mae"])
model.fit(dataset, epochs=500)


