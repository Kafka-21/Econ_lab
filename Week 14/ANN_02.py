# importing the library
import numpy as np

# creating the input array
X=np.array([[1,0,1,0],[1,0,1,1],[0,1,0,1]])
# print ('\n Input:')
# print(X)

# creating the output array
y=np.array([[1],[1],[0]])
# print ('\n Actual Output:')
# print(y)

# defining the Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))

# derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)

# initializing the variables
epoch=5 # number of training iterations
lr=0.1 # learning rate
inputlayer_neurons = X.shape[1] # number of features in data set
hiddenlayer_neurons = 3 # number of hidden layers neurons
output_neurons = 1 # number of neurons at output layer

# initializing weight and bias
np.random.seed(1)
wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bout=np.random.uniform(size=(1,output_neurons))

# training the model
for i in range(epoch):

    #Forward Propogation
    hidden_layer_input=np.dot(X,wh) + bh 
    # print("hidden_layer_input: ", hidden_layer_input)
    hiddenlayer_activations = sigmoid(hidden_layer_input)
    # print("hiddenlayer_activations: ", hiddenlayer_activations)
    output_layer_input=np.dot(hiddenlayer_activations,wout) + bout
    output = sigmoid(output_layer_input)

    #Backpropagation
    E = y-output
    slope_output_layer = derivatives_sigmoid(output)
    print("slope_output_layer: ", slope_output_layer)
    slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
    print("slope_hidden_layer: ", slope_output_layer)
    d_output = E * slope_output_layer
    Error_at_hidden_layer = d_output.dot(wout.T)
    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
    wout += hiddenlayer_activations.T.dot(d_output) *lr
    bout += np.sum(d_output, axis=0,keepdims=True) *lr
    wh += X.T.dot(d_hiddenlayer) *lr
    bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *lr

print ('\n Output from the model:')
print (output)