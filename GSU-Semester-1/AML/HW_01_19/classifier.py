# *****************CALCULATE P(Wk|CLASS) = (Nk + 1)/(N + Total words) FOR THE FEATURE SET ********************
# Nk = number of times word occurs in a class (either positive or negative)
# N = number of words in a class (either positive or negative)
# Total words = Number of features = 10 (for our program)

"""
The Approach is as follows:
1. Establish a connection to the database
2. From the Database collect the frequencies (Nk and n) into positive/negative dictionaries
3. For each review build a feature list containing the some of the defined feature set
4. For the feature list calculate the probabilities for every list item and multiply them together
5. Follow the same procedure for positive and negative reviews
6. The review is classified accordingly whichever probability value is greater
7. Accuracy of the classifier is calculated based on the testing_validator.json
8. Accuracy is displayed marking the END OF PROGRAM!
"""

import json
import mysql.connector as sqlConn

# ***********************ESTABLISHING A CONNECTION***********************
with open('database_configuration.json') as db_file:
    dbConfig = json.load(db_file)
    # print(dbConfig)
conn = sqlConn.connect(host=dbConfig['databaseServer'], port=dbConfig['databasePort'],
                       user=dbConfig['databaseUsername'], password=dbConfig['databasePassword'])
# print(conn)


myCursor = conn.cursor()
myCursor.execute("USE " + dbConfig['databaseName'])

with open('testingSet.json') as testing_file:
    testData = json.load(testing_file)
# print(testData)

with open('featureSet.json') as feature_file:
    featureData = json.load(feature_file)
# print(featureData)

# List to store the features
definedFeatureList = []
# dictionaries to store values from sql into a python dictionary
definedFeatureDict_positive = {}
definedFeatureDict_negative = {}

sqlStatement = "SELECT * from dataset.commentfrequencies"
myCursor.execute(sqlStatement)
commentFrequencies = myCursor.fetchall()
# print(commentFrequencies)
definedFeatureDict_positive["commentType"] = "positive"
definedFeatureDict_negative["commentType"] = "negative"
# define index variable to access feature values from database
index = 1
for feature in featureData:
    definedFeatureList.append(featureData[feature])
    definedFeatureDict_negative[featureData[feature]] = commentFrequencies[0][index]
    definedFeatureDict_positive[featureData[feature]] = commentFrequencies[1][index]
    index += 1
definedFeatureDict_negative["totalWordCount"] = commentFrequencies[0][index]
definedFeatureDict_positive["totalWordCount"] = commentFrequencies[1][index]


# print(definedFeatureDict_negative)
# print(definedFeatureDict_positive)


def characterCheck(review, definedFeatureList):
    reviewFeatureList = []
    for word in review:
        if word in definedFeatureList:
            reviewFeatureList.append(word)
        else:
            pass
    return reviewFeatureList


totalFeatures = len(featureData)
# print(totalFeatures)


# **************FROM THE TESTING SET CONSIDER THE REVIEWS TO BE PREDICTED ****************
# define lists holding the probability values of a feature in review


def probabilityCalculator(Nk, n, totalNoFeatures):
    return (Nk + 1) / (n + totalNoFeatures)


def classProbability(featureList, featureDict_positive, featureDict_negative, featuresNumber):
    totalPositiveFeatureProbability = 1
    totalNegativeFeatureProbability = 1
    for eachFeature in featureList:
        Nkp = featureDict_positive[eachFeature]
        Nkn = featureDict_negative[eachFeature]
        Np = featureDict_positive["totalWordCount"]
        Nn = featureDict_negative["totalWordCount"]
        featureProbability_positive = probabilityCalculator(Nkp, Np, featuresNumber)
        featureProbability_negative = probabilityCalculator(Nkn, Nn, featuresNumber)
        totalPositiveFeatureProbability *= featureProbability_positive
        totalNegativeFeatureProbability *= featureProbability_negative
        # print(probability_positive)
        # print(probability_negative)
    if totalPositiveFeatureProbability > totalNegativeFeatureProbability:
        return "positive"
    elif totalNegativeFeatureProbability > totalPositiveFeatureProbability:
        return "negative"
    else:
        return "unknown"


with open('testing_validation.json') as validator_file:
    validationResults = json.load(validator_file)
noOfTestReviews = len(validationResults)
# print(validationResults)
key = 1
counter = 0
for review in testData:
    review = testData[review].lower().split()
    reviewFeatures = characterCheck(review, definedFeatureList)
    # print(reviewFeatures)
    reviewType = classProbability(reviewFeatures, definedFeatureDict_positive,
                                  definedFeatureDict_negative, totalFeatures)
    # print(reviewType)
    # print(validationResults[str(key)])
    if reviewType == validationResults[str(key)]:
        counter += 1
    else:
        pass
    key += 1
# print(counter)
accuracy = float(counter / noOfTestReviews) * 100
accuracy = format(round(accuracy, 2))
print("CLASSIFIER HAS COMPLETED PROCESSING. HERE ARE THE RESULTS...")
print("ACCURACY OF TRAINING MODEL IS:", accuracy, "%")
# CALCULATE THE ACCURACY OF THE CLASSIFIER
