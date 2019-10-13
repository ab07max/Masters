# The purpose of this program is to implement linear regression model
import pandas as pan  # used to import CSV file and read it
from sklearn import metrics  # used to calculate the accuracy of linear regression model through mean_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split  # used to generate a random split of training and test set
import matplotlib.pyplot as plt  # used for visualizing the actual and predicted values as bar graphs
import numpy as np  # used for implement numpy arrays


class linearRegression:
    # initialization constructor
    # holds paramValues, testData, modelData at class level
    def __init__(self):
        self.paramValues = []
        self.testData = []
        self.modelData = None
        self.A1error = None
        self.A2error = None
        self.B1error = None
        self.B2error = None
        self.betweenAsValue = None
        self.betweenBsValue = None
        self.betweenAsModel = None
        self.betweenBsModel = None

    # To read the CSV data using pandas
    def retrieveModelData(self):
        modelData = pan.read_csv('ModelData.csv')
        self.modelData = modelData
        return modelData

    # Get the parameter values based on the features selected
    # The features are defined in the params variable
    # The else part is for multi variate linear regression
    # Also reshape the model data according to the input standard of linear regression
    def getRequiredParamValues(self, modelData, param1, param2, param3):
        if param3 is None:
            x = modelData[param1].values.reshape(-1, 1)
            y = modelData[param2].values.reshape(-1, 1)
        else:
            x = modelData[[param1, param2]].values
            y = modelData[param3].values.reshape(-1, 1)
        return [x, y]

    # To generate a random training and test data based ont he split specified
    # A test_size of 0.5 means that our entire model data is split as 50% training and 50% test data
    # paramValues[0] is the X-Axis values, paramValues[1] is the Y-Axis values
    # trainTestData Structure is X_train, X_test, y_train, y_test
    def getTrainingTestData(self, paramValues):
        trainTestData = train_test_split(paramValues[0], paramValues[1], test_size=0.5)
        return trainTestData

    # To define the accuracy of the linear regression model we used mean absolute error as indicator
    def meanError(self, TestData, predictedValues):
        return metrics.mean_absolute_error(TestData, predictedValues)

    # To apply regression to data we fit the X-Axis values and Y-Axis
    # We get Regression coefficients and Regression Intercept
    # Regression Coefficients is a list (W0, W1, W2,...) for a Multi-Variate Regression
    # Returns the predicted values from the model
    def applyRegressionForData(self, trainData, testData):
        regressor = LinearRegression()
        regressor.fit(trainData[0], trainData[1])
        print("Equation of line is Y = " + str(regressor.coef_) + " * X" + " + " + str(regressor.intercept_))
        predictionValues = regressor.predict(testData[0])
        return predictionValues

    # Used to plot the bar graph against predicted and actual values for the model
    # plt is import of matplotlib.pyplot
    def plotGraph(self, predictedValues, testData):
        df = pan.DataFrame({'Actual': testData[1].flatten(), 'Predicted': predictedValues.flatten()})
        df.plot(kind='bar', figsize=(8, 6))
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.show()

    # A1B1 involves a single training/test set
    # params is used to differentiate problems A1 and B1 specified by solutionCode
    def solutionToA1B1(self, modelData, params, solutionCode):
        print(solutionCode + " Solution is: ")
        if len(params) == 2:
            paramValues = self.getRequiredParamValues(modelData, params[0], params[1], None)
        else:
            paramValues = self.getRequiredParamValues(modelData, params[0], params[1], params[2])
        self.paramValues = paramValues
        TrainingData = [paramValues[0][0:10], paramValues[1][0:10]]
        TestData = [paramValues[0][10:20], paramValues[1][10:20]]
        self.testData = TestData
        predictedValues = self.applyRegressionForData(TrainingData, TestData)
        self.plotGraph(predictedValues, TestData)
        if solutionCode == "A1":
            self.A1error = self.meanError(TestData[1], predictedValues)
            print(solutionCode + "error is " + str(self.A1error))
        else:
            self.B1error = self.meanError(TestData[1], predictedValues)
            print(solutionCode + "error is " + str(self.B1error))

    # A2B2 involves multiple training/test set
    # params is used to differentiate problems A2 and B2 specified by solutionCode
    # avgPredictedValues specifies the average of all the predicted values of 20 observations
    def solutionToA2B2(self, modelData, params, solutionCode):
        print(solutionCode + " Solution is: ")
        if len(params) == 2:
            paramValues = self.getRequiredParamValues(modelData, params[0], params[1], None)
        else:
            paramValues = self.getRequiredParamValues(modelData, params[0], params[1], params[2])
        previousPredictedValues = []
        i = 1
        while i <= 20:
            trainingTestData = self.getTrainingTestData(paramValues)
            trainingData = [trainingTestData[0], trainingTestData[2]]
            testingData = [trainingTestData[1], trainingTestData[3]]
            predictedValues = self.applyRegressionForData(trainingData, testingData)
            if i == 1:
                previousPredictedValues = predictedValues
            else:
                previousPredictedValues = np.add(previousPredictedValues, predictedValues)
            i += 1
        avgPredictedValues = np.true_divide(previousPredictedValues, i - 1)
        print(avgPredictedValues)
        self.plotGraph(avgPredictedValues, self.testData)
        if solutionCode == "A2":
            self.A2error = self.meanError(self.testData[1], avgPredictedValues)
            print(solutionCode + "error is " + str(self.A2error))
        else:
            self.B2error = self.meanError(self.testData[1], avgPredictedValues)
            print(solutionCode + "error is " + str(self.B2error))


# The approach is as follows
# --------------------------
# import required packages namely pandas, sci-kit <-> sklearn, numpy, pyplot
# provide the model data obtained from CSV using pandas
# Get the training and test sets
# Approximate a line by fitting plots using linear regression
# Predict the goal values(Y) based on the features selected (X)
# Plot a bar graph between predicted and actual values
# Estimate the accuracy using mean absolute error as an estimator. Lesser the value better is the classifier.
def main():
    regressionObj = linearRegression()
    modelData = regressionObj.retrieveModelData()
    AParams = ['market value', 'Total Points']
    regressionObj.solutionToA1B1(modelData, AParams, "A1")
    BParams = ['age', 'Players playing abroad', 'Total Points']
    regressionObj.solutionToA1B1(modelData, BParams, "B1")
    regressionObj.solutionToA2B2(modelData, AParams, "A2")
    regressionObj.solutionToA2B2(modelData, BParams, "B2")
    if regressionObj.A1error > regressionObj.A2error:
        print("A2 is better")
        regressionObj.betweenAsValue = regressionObj.A2error
        regressionObj.betweenAsModel = "A2"
    else:
        print("A1 is better")
        regressionObj.betweenAsValue = regressionObj.A1error
        regressionObj.betweenAsModel = "A1"
    if regressionObj.B1error > regressionObj.B2error:
        print("B2 is better")
        regressionObj.betweenBsValue = regressionObj.B2error
        regressionObj.betweenBsModel = "B2"
    else:
        print("B1 is better")
        regressionObj.betweenBsValue = regressionObj.B1error
        regressionObj.betweenAsModel = "B1"
    if min(regressionObj.betweenAsValue, regressionObj.betweenBsValue) == regressionObj.betweenAsValue:
        print(regressionObj.betweenAsModel + " is Best")
    else:
        print(regressionObj.betweenBsModel + " is Best")


# Driver Code
main()
