from random import seed
from random import random
from csv import reader
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt


# Load a CSV file from the system
def load_csv(filename):
    data = list()
    # encoding has to be specified as utf-8-sig as reading csv may give some junk characters
    with open(filename, 'r', encoding='utf-8-sig') as file:
        csv_read = reader(file)
        for row in csv_read:
            if not row:
                continue
            data.append(row)
    return data


# Convert string column to a floating point value in the column
def str_columnValue_to_floatValue(data, column):
    for row in data:
        row[column] = float(row[column].strip())


# Convert string column to an integer value in the column
def str_columnValue_to_intValue(data, column):
    class_value = [row[column] for row in data]
    uni = set(class_value)
    look = dict()
    for i, value in enumerate(uni):
        look[value] = i
    for row in data:
        row[column] = look[row[column]]
    return look


# The Sigmoid activation function as it generates a simple boolean classified value as output
def activateHidden(weight, input):
    activat = weight[-1]
    for i in range(len(weight) - 1):
        activat += weight[i] * input[i]
    return 1 / (1 + np.exp(-activat))


# Forward propagate input to a network output to calculate error of the network
def forward_propagation(network, row):
    input = row
    for layer in network:
        new_input = []
        for neuron in layer:
            neuron['output'] = activateHidden(neuron['weights'], input)
            new_input.append(neuron['output'])
        input = new_input
    return input


# Calculate the derivative of an neuron output
def activate_derivative(out):
    return out * (1.0 - out)


# Back propagate error and store in neurons
# we back propagate to calculate the error at every layer
# Then evaluate the weights of every input
def backward_propagate_errorValue(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network) - 1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * activate_derivative(neuron['output'])


# Update network weights with error to evolve the network
# we update the weights to get the newer layer values thus the output
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        input = row[:-1]
        if i != 0:
            input = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(input)):
                neuron['weights'][j] += l_rate * neuron['delta'] * input[j]
            neuron['weights'][-1] += l_rate * neuron['delta']


# Initialize a network by building a neural network from scratch
def initialize_network(n_input, n_hidden, n_output):
    network = list()
    hidden_layer = [{'weights': [random() for i in range(n_input + 1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights': [random() for i in range(n_hidden + 1)]} for i in range(n_output)]
    network.append(output_layer)
    return network


# Make a prediction with a network to give the predicted values
def predict(network, row):
    outputs = forward_propagation(network, row)
    return outputs.index(max(outputs))


# Train a network for certain epochs
# epoch determines the iterations of backward and forward propagations
def train_neural_network(network, train, l_rate, n_epoch, n_output):
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            outputs = forward_propagation(network, row)
            expect = [0 for i in range(n_output)]
            expect[row[-1]] = 1
            sum_error += sum([(expect[i] - outputs[i]) ** 2 for i in range(len(expect))])
            backward_propagate_errorValue(network, expect)
            update_weights(network, row, l_rate)
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))


# Test the Perceptron algorithm on the Bank personal loan modelling dataset
seed(1)
# load and prepare data
filename = 'inputHW_ExtraCredit.csv'
data = load_csv(filename)
for i in range(len(data[1]) - 1):
    str_columnValue_to_floatValue(data, i)
# convert string class to integers value
str_columnValue_to_intValue(data, len(data[0]) - 1)

n_input = len(data[0]) - 1
n_output = len(set([row[-1] for row in data]))

# initialising the neural network with required configurations
# First parameter specifies the number of inputs
# Second parameter is the number of hidden layers
# Third parameter represents the number of outputs
network = initialize_network(n_input, 8, n_output)
train_neural_network(network, data, 0.1, 200, n_output)
for layer in network:
    print(layer)
for row in data:
    prediction = predict(network, row)
    print('Expected=%d, Got=%d' % (row[-1], prediction))
    plt.scatter(row[-1], prediction)
plt.show()
