# THE PURPOSE OF THIS PYTHON PROGRAM IS TO CREATE A DATA SET IN THE DATABASE

"""
The approach is as follows:
1. Establish a Connection to the database
2. Create a Database for our data set
3. Create a table structure that holds our data set
4. From the trainingSet.json calculate the word frequencies based on the featureSet.json
5. Insert all the frequency values into the database which primarily becomes our data set
"""

# import the mysql client for python
import mysql.connector as sqlConn
import json
import re

# ***********************ESTABLISHING A CONNECTION***********************
with open('database_configuration.json') as db_file:
    dbConfig = json.load(db_file)
    # print(dbConfig)
conn = sqlConn.connect(host=dbConfig['databaseServer'], port=dbConfig['databasePort'],
                       user=dbConfig['databaseUsername'], password=dbConfig['databasePassword'])
# print(conn)


myCursor = conn.cursor()

# ***********************CREATING A DATABASE******************************
myCursor.execute("CREATE DATABASE IF NOT EXISTS " + dbConfig['databaseName'])
myCursor.execute("USE " + dbConfig['databaseName'])

with open('featureSet.json') as features_file:
    featureSet = json.load(features_file)


# print(featureSet)
# ***************APPENDING THE FEATURES TO SQL STATEMENT******************
def appendFeatureSetToStatement(operation):
    statement = ""
    for feature in featureSet:
        # print(featureSet[feature])
        if operation == "create":
            statement += featureSet[feature] + " INT, "
        else:
            statement += featureSet[feature] + ", "
    return statement


# ***********************CREATING A TABLE*********************************
createStatement = "CREATE TABLE IF NOT EXISTS trainingSet (reviewID INT AUTO_INCREMENT PRIMARY KEY, "
createFeatures = appendFeatureSetToStatement("create")
createStatement += "" + createFeatures + "reviewType VARCHAR(255))"
# print("Executing..." + createStatement)
myCursor.execute(createStatement)

# *****************FUNCTION CHECKING FOR CHARACTERS**********************
character_count = {}

definedFeatureList = []


def refreshCharacterCount():
    for feature in featureSet:
        character_count[featureSet[feature]] = 0
        definedFeatureList.append(featureSet[feature])


refreshCharacterCount()

# print(definedFeatureList)


# print(character_count)
# print(character_count.__getitem__('great'))
def characterFrequency(character):
    character_count[character] += 1


def characterCheck(review):
    for char in review:
        if char in definedFeatureList:
            characterFrequency(char)
        else:
            pass


# **********************INSERTING INTO TABLE*****************************
insertStatement = "INSERT INTO trainingSet ("
insertFeatures = appendFeatureSetToStatement("insert")
insertStatement += "" + insertFeatures + "reviewType) VALUES ("

# ************FROM TRAINING SET COUNT THE FEATURE OCCURRENCE*************
with open('trainingSet.json') as training_file:
    trainingData = json.load(training_file)
# print(trainingData['reviews']['positive'])

positive_reviews = trainingData['reviews']['positive']
negative_reviews = trainingData['reviews']['negative']


def examineAndInsertReview(reviews, reviewType):
    i = 1
    featureFrequencies = ""
    for review in reviews:
        # print(review[i.__str__()])
        review = re.sub("[^a-zA-Z]", " ", str(review[i.__str__()]))
        review = review.lower().split()
        # print(review)
        characterCheck(review)
        i += 1
        for item in character_count:
            featureFrequencies += "" + str(character_count[item]) + ", "
        # print(character_count)
        # print(featureFrequencies)
        if reviewType == "positive":
            # statement = insertStatement + featureFrequencies + "\"positive\"" + ")"
            myCursor.execute(insertStatement + featureFrequencies + "\"positive\"" + ")")
        else:
            # statement = insertStatement + featureFrequencies + "\"negative\"" + ")"
            myCursor.execute(insertStatement + featureFrequencies + "\"negative\"" + ")")
        conn.commit()
        featureFrequencies = ""
        refreshCharacterCount()


examineAndInsertReview(positive_reviews, "positive")
examineAndInsertReview(negative_reviews, "negative")
print("***********************DATA SET CREATED SUCCESSFULLY!***********************")
conn.close()

# for positive_review in positive_reviews:
#     print(positive_review)
