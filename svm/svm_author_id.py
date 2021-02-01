#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import metrics  # accuracy_score
from sklearn import svm  # GaussianNB


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
clf = svm.SVC(kernel='rbf', C=10000)
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]
clf.fit(features_train, labels_train)
prediction = clf.predict(features_test)
# print prediction[50]
chris = 0
sara = 0
for i in prediction:
    if i == 1:
        chris = chris + 1
    else:
        sara = sara + 1
print 'chris: ' + str(chris) + ' sara: ' + str(sara)
# accuracy = metrics.accuracy_score(prediction, labels_test)
# print accuracy
#########################################################


