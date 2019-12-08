# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:03:41 2019

@author: jrg5701
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


df = pd.read_csv("kickstarter_2018_clean.csv")

useful = df[['category', 'main_category' ,'usd_goal_real','days_elapsed', 'state','country','month_launched']]

mainFact,main = pd.factorize(useful.main_category)
subFact,sub = pd.factorize(useful.category)

for x in range(331674):
    subFact[x]= subFact[x] + mainFact[x]*200

# useful.main_category = pd.Categorical(useful.main_category)
useful['main_category_index'] = mainFact
useful.main_category.astype('category').cat.codes
 
# useful.category = pd.Categorical(useful.category)
useful['category_index'] = subFact
useful.category.astype('category').cat.codes

useful.state = pd.Categorical(useful.state)
useful['state_index'] = useful.state.cat.codes
useful.state.astype('category').cat.codes

useful.country = pd.Categorical(useful.country)
useful['country_index'] = useful.country.cat.codes
useful.country.astype('category').cat.codes



factor = useful[['usd_goal_real', 'days_elapsed','country_index','month_launched','main_category_index','category_index']]
outcome = useful[['state_index']]

X_train, X_test, y_train, y_test = train_test_split(factor, outcome, test_size=.30)

k = 9
# train model
neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train, y_train)

result = neigh.predict(X_test)

train_compare = metrics.accuracy_score(y_train, neigh.predict(X_train))
test_compare = metrics.accuracy_score(y_test, result)
print('Train accuracy = ', train_compare)
print('Test accuracy = ', test_compare)