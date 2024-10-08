# -*- coding: utf-8 -*-
"""Fake news.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wP6F5ANJA7s2F0QhFsxjbv5n_veA79KU
"""

import numpy as np
import pandas as pd
import re
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

nltk.download('stopwords')

print(stopwords.words('english'))

data=pd.read_csv('/content/train.csv')
data.head()
data.isna().sum()
data=data.fillna('')
data['content']=data['author']+' '+data['title']
X=data['content'].values
Y=data['label'].values
print(X)
print(Y)

port_stem = PorterStemmer()

def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '+ ' '.join(stemmed_content)+' '
    return stemmed_content

data['content']=data['content'].apply(stemming)
print(data['content'])

X=data['content'].values
Y=data['label'].values
print(X)

vectorizer = TfidfVectorizer()
vectorizer.fit(X)


X_transformed = vectorizer.transform(X)

print(X_transformed)

X_train, X_test, Y_train, Y_test = train_test_split(X_transformed, Y, test_size=0.2, stratify=Y, random_state=2)

model=LogisticRegression()
model.fit(X_train,Y_train)
model.predict(X_test)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

test_data_accuracy

