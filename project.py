# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:06:10 2019

@author: bxt40
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


df = pd.read_csv("./data/kickstarter_small_data.csv")

useful = df[['category', 'main_category' ,'usd_goal_real','days_elapsed', 'state']]

useful.category = pd.Categorical(useful.category)
useful['category_index'] = useful.category.cat.codes
useful.category.astype('category').cat.codes

useful.state = pd.Categorical(useful.state)
useful['state_index'] = useful.state.cat.codes
useful.state.astype('category').cat.codes

factor = useful[['category_index', 'usd_goal_real', 'days_elapsed']]
outcome = useful[['state_index']]

X_train, X_test, y_train, y_test = train_test_split(factor, outcome, test_size=.30)

k = 3
# train model
neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train, y_train)

result = neigh.predict(X_test)

train_compare = metrics.accuracy_score(y_train, neigh.predict(X_train))
test_compare = metrics.accuracy_score(y_test, result)
print('Train accuracy = ', train_compare)
print('Test accuracy = ', test_compare)