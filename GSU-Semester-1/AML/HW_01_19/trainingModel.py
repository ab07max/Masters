# THE PURPOSE OF THIS PYTHON PROGRAM IS TO TRAIN THE CLASSIFIER FOR DATA SET

"""
The approach is as follows:
1. Establish a Database connection to interact with the Database
2. Calculate the frequencies pertaining to Nk and n values of positive and negative reviews
3. Create a table that holds these frequencies (used for probability calculation)
4. Model is said to be trained once the frequency values (Nk and n) are inserted
"""

import mysql.connector as sqlConn
import json

# ************************ESTABLISHING A CONNECTION*****************************
with open('database_configuration.json') as db_file:
    dbConfig = json.load(db_file)
    # print(dbConfig)
conn = sqlConn.connect(host=dbConfig['databaseServer'], port=dbConfig['databasePort'],
                       user=dbConfig['databaseUsername'], password=dbConfig['databasePassword'])
# print(conn)


myCursor = conn.cursor()
myCursor.execute("USE " + dbConfig['databaseName'])

# *****************P(Wk|CLASS) = (Nk + 1)/(N + Total words)********************
# Nk = number of times word occurs in a class (either positive or negative)
# N = number of words in a class (either positive or negative)
# Total words = Number of features = 10 (for our program)
# firstly calculate dictionaries for Nks
with open('featureSet.json') as featureSet:
    features = json.load(featureSet)
totalFeatures = len(features)
# print(totalFeatures)
positiveFrequencyDict = {}
negativeFrequencyDict = {}
sqlStatement = "SELECT SUM("
for feature in features:
    # Prepare SQL Statement
    positiveFeatureStatement = features[feature] + ") FROM trainingset where reviewType = \"positive\""
    negativeFeatureStatement = features[feature] + ") FROM trainingset where reviewType = \"negative\""
    myCursor.execute(sqlStatement + positiveFeatureStatement)
    positiveResult = myCursor.fetchall()
    for rows in positiveResult:
        positiveFrequencyDict[features[feature]] = int(float(rows[0]))
    myCursor.execute(sqlStatement + negativeFeatureStatement)
    negativeResult = myCursor.fetchall()
    for rows in negativeResult:
        negativeFrequencyDict[features[feature]] = int(float(rows[0]))

# print(positiveFrequencyDict)
# print(negativeFrequencyDict)

# Create two new tables and enter the frequencies
createStatement = "CREATE TABLE IF NOT EXISTS commentFrequencies " \
                  "(commentType VARCHAR(255) PRIMARY KEY, "


def prepareFeatureStatement(operation):
    featuresStatement = ""
    for featureElement in features:
        if operation == "create":
            featuresStatement += features[featureElement] + " INT, "
        else:
            featuresStatement += features[featureElement] + ", "
    return featuresStatement


featureStatement = prepareFeatureStatement("create")

createStatement += featureStatement + "totalWordCount INT)"
# print(createStatement)
myCursor.execute(createStatement)

# Insert frequency values into the table
insertStatement = "INSERT INTO commentFrequencies (commentType, "
insertFeatureStatement = prepareFeatureStatement("insert")
insertStatement += insertFeatureStatement + "totalWordCount) VALUES ("
positiveInsertStatement = insertStatement + "\"positive\", "
negativeInsertStatement = insertStatement + "\"negative\", "

# Secondly calculate n for positive and negative cases
positiveWordCount = 0
positiveFeatureValues = ""
negativeFeatureValues = ""
for feature in positiveFrequencyDict:
    positiveWordCount += positiveFrequencyDict[feature]
    positiveFeatureValues += str(positiveFrequencyDict[feature]) + ", "
negativeWordCount = 0
for feature in negativeFrequencyDict:
    negativeWordCount += negativeFrequencyDict[feature]
    negativeFeatureValues += str(negativeFrequencyDict[feature]) + ", "

positiveInsertStatement += positiveFeatureValues + str(positiveWordCount) + ")"
negativeInsertStatement += negativeFeatureValues + str(negativeWordCount) + ")"

# print(positiveInsertStatement)
# print(negativeInsertStatement)
# print(positiveWordCount)
# print(negativeWordCount)
myCursor.execute(positiveInsertStatement)
myCursor.execute(negativeInsertStatement)
conn.commit()
print("********************MODEL TRAINED SUCCESSFULLY!*********************")
conn.close()