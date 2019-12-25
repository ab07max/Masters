import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


# Function importing Dataset
def importdata():
    balance_data = pd.read_csv('Bank_Personal_Loan_Modelling.csv', error_bad_lines=False, encoding='utf-8')

    # Printing the dataset shape
    print("Dataset Length: ", len(balance_data))
    print("Dataset Shape: ", balance_data.shape)

    # Printing the dataset obseravtions
    print("Dataset: ", balance_data)
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
def train_using_Gaussian(X_train, X_test, y_train):
    # Creating the classifier object
    clf_gaussian = GaussianNB()
    print(X_train)
    print(y_train)
    # Performing training
    clf_gaussian.fit(X_train, y_train)
    return clf_gaussian


# Function to make predictions
def prediction(X_test, clf_object):
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred


#
#
# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
    print("Confusion Matrix: ",
          confusion_matrix(y_test, y_pred))

    print("Accuracy : ",
          accuracy_score(y_test, y_pred) * 100)

    print("Report : ",
          classification_report(y_test, y_pred))


# Driver code
def main():
    # Building Phase 
    data = importdata()
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    clf_gaussian = train_using_Gaussian(X_train, X_test, y_train)
    print(clf_gaussian)

    y_pred_gaussian = prediction(X_test, clf_gaussian)

    cal_accuracy(y_test, y_pred_gaussian)


# Calling main function
if __name__ == "__main__":
    main()
