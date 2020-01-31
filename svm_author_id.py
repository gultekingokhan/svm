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

features_train, features_test, labels_train, labels_test = preprocess()

features_train = features_train[:len(features_train)/100] # To decrease the size of the training set.
labels_train = labels_train[:len(labels_train)/100]

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

classifier = SVC(C=10000.0, kernel='rbf', gamma='auto', verbose=True)

t0 = time()

classifier.fit(features_train, labels_train)

print "training time: ", round(time()-t0, 3), "s"

t1 = time()

labels_predicted = classifier.predict(features_test)

print "Prediction time: ", round(time()-t1, 3), "s"

print "Accuracy: ", accuracy_score(labels_test, labels_predicted)

print "PREDICTIONS: ", labels_predicted[10], labels_predicted[26], labels_predicted[50]