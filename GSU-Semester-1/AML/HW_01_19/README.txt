REQUIREMENTS:
-------------
1. Python installed on the machine
2. Mysql set up and running
3. Recommended to configure an instance of mysql with following credentials:
    a) database server as '127.0.0.1' or localhost
    b) port as '3306'
    c) username as 'root'
    d) password as 'root'

CONSIDERATIONS:
---------------
1. Database configurations are configured in 'database_configuration.json'
    a) For development purpose, I have worked on the local instance of mysql.
    b) Any changes must be done in 'database_configuration.json' in order to successfully connect and communicate with the database
2. Training data is considered on 30 positive reviews and 30 negative reviews
    a) If reviews are to be added/removed, please visit 'trainingSet.json'
3. feature data consists of 15 features to be run against the training set
    a) In case of addition/removal of features please visit 'featureSet.json'
4. Test data is considered randomly with 18 reviews
    a) If the test data has to be changed, do it at 'testingSet.json'
    b) Also, make changes to 'testing_validation.json' accordingly(addition or removal) based on the review type

STEPS TO RUN THE CLASSIFIER:
----------------------------
1. Make sure that all the files are placed in the single folder after unzipping as there is a dependency on json files
2. First run the 'dataset_creation.py'
    a) This will create the structure of our data set in the database and insert values
3. Next run the 'trainingModel.py'
    a) This python file will train our data set by calculating nk and n values
4. Finally, run the classifier.py which gives the accuracy of Training Model

NOTE:
-----
1. Lookout for libraries used in the project python files. If they're not present please install the libraries first
2. Database credentials must be set up accordingly before running the project