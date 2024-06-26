# -*- coding: utf-8 -*-
"""bhavani.rainfallprediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1irfjAMrCTq42n3bWeusSh8t7_hxO1Kq6
"""

import numpy as np
import pandas as pd
import os
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from scipy import stats
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
from collections import Counter
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, f1_score
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestRegressor
import warnings

warnings.filterwarnings("ignore")

rain = pd.read_csv('/content/weatherAUS.csv')
rain.head(10)

print(f'The number of rows are {rain.shape[0] } and the number of columns are {rain.shape[1]}')

rain.info()

categorical_col, contin_val=[],[]

for i in rain.columns:

    if rain[i].dtype == 'object':
        categorical_col.append(i)
    else:
        contin_val.append(i)

print(categorical_col)
print(contin_val)

rain.nunique()

rain.isnull().sum()

msno.matrix(rain)

msno.bar(rain, sort='ascending')

msno.heatmap(rain)

rain.head()

fig, ax =plt.subplots(3,1)
plt.figure(figsize=(10,10))

sns.countplot(data=rain,x='WindDir9am',ax=ax[0])
sns.countplot(data=rain,x='WindDir3pm',ax=ax[1])
sns.countplot(data=rain,x='WindGustDir',ax=ax[2])
fig.tight_layout()

#Dropping date column
rain=rain.iloc[:,1:]
rain

le = preprocessing.LabelEncoder()

rain['WindDir9am'] = le.fit_transform(rain['WindDir9am'])
rain['WindDir3pm'] = le.fit_transform(rain['WindDir3pm'])
rain['WindGustDir'] = le.fit_transform(rain['WindGustDir'])

rain.head()

fig, ax =plt.subplots(2,1)
plt.figure(figsize=(10,10))
sns.boxplot(rain['Pressure3pm'],orient='v',color='c',ax=ax[0])
sns.boxplot(rain['Pressure9am'],orient='v',color='c',ax=ax[1])
fig.tight_layout()

sns.violinplot(x='RainToday',y='MaxTemp',data=rain,hue='RainTomorrow')

sns.violinplot(x='RainToday',y='MinTemp',data=rain,hue='RainTomorrow')