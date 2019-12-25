import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import graphviz
import os

os.environ["PATH"] += os.pathsep + 'F:/PycharmProjects/Decision_Intelligence/venv/Lib/site-packages/release/bin/'


# Function importing Dataset
def importdata():
    balance_data = pd.read_csv('Bank_Personal_Loan_Modelling.csv', error_bad_lines=False, encoding='utf-8')

    # Printing the dataset shape
    print("Dataset Length: ", len(balance_data))
    print("Dataset Shape: ", balance_data.shape)

    # Printing the dataset obseravtions
    # print("Dataset: ", balance_data)
    return balance_data


# Function to split the dataset
def splitdataset(balance_data):
    # Seperating the target variable
    X = balance_data.values[:, 1:12]
    Y = balance_data.values[:, 12]

    # print(X)
    # print(Y)
    # # Spliting the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.1, random_state=100)

    return X, Y, X_train, X_test, y_train, y_test


# Function to perform training with giniIndex.
def train_using_gini(X_train, X_test, y_train):
    # Creating the classifier object
    clf_gini = RandomForestClassifier(criterion="gini", n_estimators=11,
                                      random_state=100, max_depth=None, min_samples_leaf=5)

    # Performing training
    clf_gini.fit(X_train, y_train)
    return clf_gini


# Function to perform training with entropy.
def train_using_entropy(X_train, X_test, y_train):
    # Decision tree with entropy
    clf_entropy = RandomForestClassifier(
        criterion="entropy", n_estimators=16, random_state=100,
        max_depth=None, min_samples_leaf=5)

    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy


# Function to make predictions
def prediction(X_test, clf_object):
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred


# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
    print("Confusion Matrix: ",
          confusion_matrix(y_test, y_pred))

    print("Accuracy : ",
          accuracy_score(y_test, y_pred) * 100)

    print("Report : ",
          classification_report(y_test, y_pred))


# Function to Visualise the decision trees
def visualizer(clf, name):
    feature_names = ['Age', 'Experience', 'Income', 'Family', 'CCAvg', 'Education', 'Mortgage',
                     'Securities Account', 'CD Account', 'Online', 'CreditCard']
    class_names = ['0', '1']
    dot_data = tree.export_graphviz(clf, out_file=None, feature_names=feature_names,
                                    class_names=class_names, filled=True, rounded=True,
                                    special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render(name)


# Driver code
def main():
    # Building Phase
    data = importdata()
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    # clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
    # clf.fit(X_train, y_train)
    # print(clf.feature_importances_)

    clf_gini = train_using_gini(X_train, X_test, y_train)
    clf_entropy = train_using_entropy(X_train, X_test, y_train)
    print("Results Using Gini Index:")

    y_pred_gini = prediction(X_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)

    print("Results Using Entropy:")
    # Prediction using entropy
    y_pred_entropy = prediction(X_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)

    # visualizer(clf_gini, "gini")
    # visualizer(clf_entropy, "entropy")


# Calling main function
if __name__ == "__main__":
    main()
