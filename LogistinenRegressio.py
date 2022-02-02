#luokittelu
#logistinen regressio

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

data = pd.read_csv('C:/Users/eemil/Desktop/samk/data-analytics/koneoppiminen(3)/koneoppiminen1(py)/framingham.csv')

#tutkitaan onko puuttuvia tietoja
print('Datan puuttuvat arvot:\n', data.isnull().sum())

#poistetaan puuttuvaa tietoa sisältävät rivit
data = data.dropna()

data_y = data['TenYearCHD']
data_X = data.loc[:, data.columns != 'TenYearCHD']

X_train, X_test, Y_train, Y_test = train_test_split(data_X,
                                                    data_y,
                                                    test_size=0.25,
                                                    random_state=72)


#tehdään malli opetustataa käyttäen
malli = LogisticRegression(random_state=123, solver='lbfgs', multi_class='ovr').fit(X_train, Y_train)

#tehdään ennusteet testidatalle
Y_pred = malli.predict(X_test)

#ennusteen tarkkuus ja luokkamatriisi
print("Tarkkuus: ", end='')
print(round(accuracy_score(Y_test, Y_pred),4))
print(classification_report(Y_test, Y_pred, target_names=['Ei sairastu','Sairastuu']))


#tehdään malli opetusdataa käyttäen - X:ssä vain sarakkeet sysBP + male + age + cigsPerDay
X_train = X_train[['sysBP','male','age','cigsPerDay']]
X_test = X_test[['sysBP','male','age','cigsPerDay']]
malli2 = LogisticRegression(random_state=123, solver='lbfgs', multi_class='ovr').fit(X_train, Y_train)

#ennusteet testidatalle
Y_pred2 = malli2.predict(X_test)

#ennusteen tarkkuus ja luokkamatriisi
print("Tarkkuus: ", end='')
print(round(accuracy_score(Y_test, Y_pred2),4))
print(classification_report(Y_test, Y_pred2, target_names=['Ei sairastu','Sairastuu']))



