# Imperative Programming style - subclassing API for loops, varying shapes, conditional branching and dynamic behaviour 

class WideAndDeepModel(keras.Model):
	def __init__(self, units = 30, activation = "relu", **kwargs):
		super().__init__(**kwargs) # handles standard args( e.g. name)
		self.hidder1     = keras.layers.Dense(units, activation = activation)
		self.hidder2     = keras.layers.Dense(units, activation = activation)
		self.main_output = keras.layers.Dense(1)
		self.aux_output  = keras.layers.Dense(1)

	def call(self, inputs):
		input_A, input_B = inputs
		hidder1 = self.hidder1(input_B)
		hidder2 = self.hidder2(hidder1)
		concat  = keras.layers.concatenate([input_A, hidder2])
		main_output = self.main_output(concat)
		aux_output = self.aux_output(hidder2)
		return main_output, aux_output

	model = WideAndDeepModel()

# can do pretty much anything in call() method - for loops, if statements, low-level TensorFlow
 
