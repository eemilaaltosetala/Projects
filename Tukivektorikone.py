#luokittelu
#tukivektorikone

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

data = pd.read_csv("C:/framingham.csv")

#poistetaan puuttuvaa tietoa sis. rivit
data = data.dropna()

data_y = data['TenYearCHD']
data_X = data.loc[:, data.columns != 'TenYearCHD']

#jaetaan data opetus ja testidataan
X_train, X_test, Y_train, Y_test = train_test_split(data_X,
                                                    data_y,
                                                    test_size=0.25,
                                                    random_state=72)

#luodaan mallit ja opetetaan ne
malli1 = svm.SVC(kernel='linear', C=1.0)
malli2 = svm.SVC(kernel='poly', gamma='scale', C=1.0, coef0=0)
malli3 = svm.SVC(kernel='poly', gamma='scale', C=1.5, coef0=0)
malli4 = svm.SVC(kernel='poly', gamma='scale', C=0.01, coef0=0)

malli1.fit(X_train, Y_train)
malli2.fit(X_train, Y_train)
malli3.fit(X_train, Y_train)
malli4.fit(X_train, Y_train)

#ennusteet testidatalle
y_pred1 = malli1.predict(X_test)
y_pred2 = malli2.predict(X_test)
y_pred3 = malli3.predict(X_test)
y_pred4 = malli4.predict(X_test)


#ennusteen tarkkuus ja luokittelumatriisi
print("linear - tarkkuus: ", end='')
print(round(accuracy_score(Y_test, y_pred1),4))
print(confusion_matrix(Y_test, y_pred1))

print("poly / C=1.0 - tarkkuus: ", end='')
print(round(accuracy_score(Y_test, y_pred2),4))
print(confusion_matrix(Y_test, y_pred2))

print("poly / C=1.5 - tarkkuus: ", end='')
print(round(accuracy_score(Y_test, y_pred3),4))
print(confusion_matrix(Y_test, y_pred3))

print("poly / C=0.01 - tarkkuus: ", end='')
print(round(accuracy_score(Y_test, y_pred4),4))
print(confusion_matrix(Y_test, y_pred4))

























