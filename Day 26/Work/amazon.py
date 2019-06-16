# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:43:27 2019

@author: TAPAN
"""

import pandas as pd

# Importing the dataset
# Ignore double qoutes, use 3 
label=['text','ratings']
amz_df = pd.read_csv('amazon_cells_labelled.txt', delimiter = '\t',names=label)

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []
#perform row wise noise removal and stemming

for i in range(0, 1000):
    text = re.sub('[^a-zA-Z]', ' ', amz_df['text'][i])
    text = text.lower()
    text = text.split()
    text = [word for word in text if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    text = [ps.stem(word) for word in text]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    text = ' '.join(text)
    corpus.append(text)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = amz_df.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)


# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_nb = confusion_matrix(labels_test, labels_pred)


# Fitting Knn to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)


rv='this is a very good product,i would definetely recommand it.'

rv = [rv for rv in rv 
          if not rv 
          in set(stopwords.words('english'))]
    
#lem = WordNetLemmatizer() #Another way of finding root word
ps = PorterStemmer()
rv = [ps.stem(rv) for rv in rv]
#review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
rv = ' '.join(rv)
corpus.append(rv)
