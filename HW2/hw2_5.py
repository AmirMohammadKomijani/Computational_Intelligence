# -*- coding: utf-8 -*-
"""HW2_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pBm7p7HewuY9DbCq2x7_Ad4Ubuoe-r5Q

*italicized text*
"""

sources = "https://www.youtube.com/watch?v=tUoUdOdTkRw" , "https://pyimagesearch.com/2021/05/06/backpropagation-from-scratch-with-python/",

import numpy as np

"""Variables"""

alpha = 0.1 # learning rate
epochs = 10000 # number of steps
input_size = 2
hidden_size = 4
output_size = 1

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[1], [0], [0], [1]])

"""Initialize weights"""

np.random.seed(0)
input_layer_weights = np.random.uniform(size=(input_size, hidden_size))
output_layer_weights = np.random.uniform(size=(hidden_size, output_size))

"""Sigmoid Function"""

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

"""Backpropagation Algorithm


> Forward Pass


> Backward Pass






"""

input_layer_weights = np.random.uniform(size=(input_size, hidden_size))
output_layer_weights = np.random.uniform(size=(hidden_size, output_size))

# Training the neural network
for epoch in range(epochs):
    # Forward pass
    hidden_layer_input = np.dot(X, input_layer_weights)
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, output_layer_weights)
    output_layer_output = sigmoid(output_layer_input)

    # Calculate the error
    error = Y - output_layer_output

    # Backpropagation
    delta_output = error * sigmoid_derivative(output_layer_output)
    error_hidden_layer = delta_output.dot(output_layer_weights.T)
    delta_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Update the weights and biases
    output_layer_weights += hidden_layer_output.T.dot(delta_output) * alpha
    input_layer_weights += X.T.dot(delta_hidden_layer) * alpha

hidden_layer_output = sigmoid(np.dot(X, input_layer_weights))
hidden_layer_output = sigmoid(np.dot(hidden_layer_output, output_layer_weights))

predictions = np.round(hidden_layer_output)

print("XNOR predictions:")
for i in range(len(X)):
    print(f"Input: {X[i]}, Predicted: {predictions[i][0]}")