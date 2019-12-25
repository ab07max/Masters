import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class NeuralNetwork:

    def __init__(self):
        # Seed the random number generator
        np.random.seed(1)

        # Set synaptic weights to a 4x1 matrix as we are considering 4 features,
        # with values from -1 to 1 and mean 0
        # self.synaptic_weights = 2 * np.random.random((4, 1)) - 1
        # self.synaptic_weights = 2 * np.random.random((4, 1)) - 1
        self.synaptic_weightsW = 2 * np.random.random((1, 2)) - 1
        self.synaptic_weightsV = 2 * np.random.random((2, 1)) - 1

    def sigmoid(self, x):
        """
        Takes in weighted sum of the inputs and normalizes
        them through between 0 and 1 through a sigmoid function 1 / (1 + e^-x)
        """
        return 1 / (1 + np.exp(-x))

    def calculateHiddenLayerDeltas(self, errorY, W_outputs):
        errorZ = errorY * self.synaptic_weightsV.T
        deltasZ1 = errorY * W_outputs[:, 0]
        deltasZ2 = errorY * W_outputs[:, 1]
        return errorZ, deltasZ1, deltasZ2

    def sigmoid_derivative(self, x):
        """
        The derivative of the sigmoid function used to
        calculate necessary weight adjustments
        The derivative is observed as sigmoid fn * (1 - sigmoid fn)
        """
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        """
        We train the model through trial and error, adjusting the
        synaptic weights each time to get a better result
        The training_iterations specify the number of times we want to iterate the
        model to train better
        """
        for iteration in range(training_iterations):
            # Pass training set through the neural network
            # print(iteration)
            W_output = self.think(training_inputs)

            V_output = np.dot(W_output, self.synaptic_weightsV)

            # Calculate the error rate
            errorY = training_outputs - V_output
            # error = 0.5 * pow(training_outputs - output, 2)

            # Multiply error by input and gradient of the sigmoid function
            # Less confident weights are adjusted more through the nature of the function

            errorZ, deltasZ1, deltasZ2 = self. calculateHiddenLayerDeltas(errorY, W_output)

            self.calculateInputLayerDeltas(errorZ, training_inputs)

            calculateAdjustedWeights()
            W_adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(W_output))
            V_adjustme

            # update synaptic weights by adding the error adjustments
            self.synaptic_weightsW += adjustments
            self.synaptic_weightsV += adjustments

    def think(self, inputs):
        """
        Pass inputs through the neural network to get output
        """

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weightsW))
        return output

    def calculateInputLayerDeltas(self, errorZ, training_inputs):
        # deltaX1 = errorZ[]
        pass


def importDataset():
    # data = pd.read_csv('temp.csv', error_bad_lines=False, encoding='utf-8',
    #                    delimiter=',')
    # data = pd.read_csv('Bank_Personal_Loan_Modelling_less_rec.csv', error_bad_lines=False, encoding='utf-8',
    #                    delimiter=',')
    data = pd.read_csv('inputHW_ExtraCredit.csv', error_bad_lines=False, encoding='utf-8',
                       delimiter=',')
    return data


if __name__ == "__main__":
    # Initialize the single neuron neural network
    neural_network = NeuralNetwork()

    print("Random starting synaptic weights: ")
    print(neural_network.synaptic_weightsW)

    # The training set, with 4500 examples consisting of 4
    # input values and 1 output value
    balance_data = importDataset()
    # X = balance_data.values[:, 1:5]
    # Y = balance_data.values[:, 5]

    X = balance_data.values[:, 0]
    Y = balance_data.values[:, 1]

    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.1, random_state=100)

    training_inputs = np.array([X_train]).T
    training_outputs = np.array([y_train]).T

    print(training_inputs.shape)

    # Train the neural network
    neural_network.train(training_inputs, training_outputs, 100)

    print("Synaptic weights W after training: ")
    print(neural_network.synaptic_weightsW)

    print("Synaptic weights V after training: ")
    print(neural_network.synaptic_weightsV)

    testSize = y_test.size
    # print(testSize)
    count = 0
    for test_input, test_output in zip(X_test, y_test):
        predictedValue = neural_network.think(np.array([test_input]).T)
        print(int(np.round(predictedValue[0])))
        print("actual:" + str(test_output))
        if int(np.round(predictedValue[0])) == int(test_output):
            count += 1
    print("Accuracy of the perceptron is " + str((count / testSize) * 100))
