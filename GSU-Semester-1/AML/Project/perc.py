# Perceptron Algorithm on the Sonar Dataset
from random import seed
from random import randrange
from csv import reader


# Load a CSV file
def load_csv(filename):
    dataset = list()
    # encoding has to be specified as utf-8-sig as reading csv may give some junk characters
    with open(filename, 'r', encoding='utf-8-sig') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup


# Working of the k-fold cross validation algorithm
# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split


# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0


# Evaluate the perceptron algorithm using a cross validation split
def evaluate_perceptronAlgorithm(dataset, algorithm, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = list()
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
    return scores


# Make a prediction with weights
def predict(row, weights):
    activation = weights[0]
    for i in range(len(row) - 1):
        # the Perceptron receives input signals from examples of training data
        # that we weight and combined in a linear equation called the activation.
        activation += weights[i + 1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0


# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch):
    weights = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        for row in train:
            prediction = predict(row, weights)
            error = row[-1] - prediction
            weights[0] = weights[0] + l_rate * error
            for i in range(len(row) - 1):
                weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
    return weights


# Perceptron Algorithm With Stochastic Gradient Descent
def perceptron(train, test, l_rate, n_epoch):
    predictions = list()
    weights = train_weights(train, l_rate, n_epoch)
    for row in test:
        prediction = predict(row, weights)
        predictions.append(prediction)
    return (predictions)


# Test the Perceptron algorithm on the Bank personal loan modelling dataset
seed(1)
# load and prepare data
filename = 'Perceptron_Dataset.csv'
dataset = load_csv(filename)
# print(dataset)

'''
    Dataset may contain some string values and so
    we have to remove them and present it to perceptron
'''
for i in range(len(dataset[1]) - 1):
    str_column_to_float(dataset, i)
# convert string class to integers
str_column_to_int(dataset, len(dataset[0]) - 1)
# # evaluate algorithm

'''
    Using the k-fold cross validation
    Once we are done with training our model, we just can’t assume 
    that it is going to work well on data that it has not seen before.
    We need some kind of assurance of the accuracy of the predictions that our model is putting out. 
    The number of epoch determines the number of iterations that we carry for the perceptron 
'''
n_folds = 3
l_rate = 0.01
n_epoch = 500


scores = evaluate_perceptronAlgorithm(dataset, perceptron, n_folds, l_rate, n_epoch)

# for every k-fold validation the model returns an accuracy
# The average of all the accuracies will be the mean accuracy of the model
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
