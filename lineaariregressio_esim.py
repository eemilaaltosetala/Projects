#Lineaariregressio esimerkkejä

import lineaariregressio   
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Esim 1: X on 1D
X = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]).reshape((-1, 1))
y = np.array([5, 12, 20, 22, 14, 26, 32, 44, 22, 47, 38])

malli = lineaariregressio.teeLineaariRegressio(X, y)

#ennustaminen mallin avulla
y_pred = malli.predict(X)
#visualisointi
plt.scatter(X, y, color="black")
plt.plot(X,y_pred, color="blue", linewidth=3)
plt.xticks()
plt.yticks()
plt.show()

#Esim 2: X on 2D
data = pd.DataFrame([[aseta,tänne],[jotain,arvoja],[poo,hoo],[1,2]],
                    columns=['Nimi','toinen'])
data['sarake'] = pd.series([1,2,3,4...])

data_y = data['sarake']
data_X = data.loc[:, data.columns != 'sarake']

malli = lineaariregressio.teeLineaariRegressio(data_X, data_y)

print(f'Hinta {} + mainoskulut {} --> Myynti {malli.predict(pd.DataFrame({}"sarake":[220], "mainoskulut:[150]"))}')
#puutteellinen


#Esim 3: X on ?D
data = pd.read_csv('diabetes_scaled.csv', index_col=0)
print(data.columns)
data_y = data['target']
data_for_X = data.loc[:, data.columns != 'target'] #näistä valitaan X:n sarakkeet

#Testataan sarake kerrallaan 
for i in range(0,len(data_for_X.columns)):
    data_X = data_for_X.iloc[:, [i]]
    print('\nX = ', data_X.columns.values)
    lineaariregressio.teeLineaariRegressio(data_X, data_y)
#tutkii RMSE ja R2

#Testataan 2 saraketta kerrallaan
for i in range(0,len(data_for_X.columns)):
    for j in range(i,len(data_for_X.columns)):
        if i!=j:
            data_X = data_for_X.iloc[:, [i,j]]
            print('\nX = ', data_X.columns.values)
            lineaariregressio.teeLineaariRegressio(data_X, data_y)

#Edellisen perusteella valitaan kaksi: bmi + s5 (R2=0.46 eli suurin)

#Testataan bmi + s5 + kolmas
for i in range(0,len(data_for_X.columns)):
    if((data_for_X.columns.values[i] != 'bmi') and
       (data_for_X.columns.values[i] != 's5')):
        data_X = data_for_X.loc[:, ['bmi','s5',data_for_X.columns.values[i]]]
        print('\nX = ', data_X.columns.values)
        lineaariregressio.teeLineaariRegressio(data_X, data_y)

#Testataan bmi + s5 + bp + neljäs
for i in range(0,len(data_for_X.columns)):
    if((data_for_X.columns.values[i] != 'bmi') and
       (data_for_X.columns.values[i] != 's5') and
       (data_for_X.columns.values[i] != 'bp')):
        data_X = data_for_X.loc[:, ['bmi','s5','bp',data_for_X.columns.values[i]]]
        print('\nX = ', data_X.columns.values)
        lineaariregressio.teeLineaariRegressio(data_X, data_y)

#Testataan bmi + s5 + bp + s3 + joku viides --> paraneeko R2 vieläkin?
for i in range(0,len(data_for_X.columns)):
    if((data_for_X.columns.values[i] != 'bmi') and
       (data_for_X.columns.values[i] != 's5') and
       (data_for_X.columns.values[i] != 'bp') and
       (data_for_X.columns.values[i] != 's3')):
        data_X = data_for_X.loc[:, ['bmi','s5','bp','s3',data_for_X.columns.values[i]]]
        print('\nX = ', data_X.columns.values)
        lineaariregressio.teeLineaariRegressio(data_X, data_y)

#Testataan edelliset + sex + joku kuudes --> paraneeko?
for i in range(0,len(data_for_X.columns)):
    if((data_for_X.columns.values[i] != 'bmi') and
       (data_for_X.columns.values[i] != 's5') and
       (data_for_X.columns.values[i] != 'bp') and
       (data_for_X.columns.values[i] != 's3') and
       (data_for_X.columns.values[i] != 'sex')):
        data_X = data_for_X.loc[:, ['bmi','s5','bp','s3','sex',data_for_X.columns.values[i]]]
        print('\nX = ', data_X.columns.values)
        lineaariregressio.teeLineaariRegressio(data_X, data_y)
        
#Testataan edelliset + s6 + seitsemäs
for i in range(0,len(data_for_X.columns)):
    if((data_for_X.columns.values[i] != 'bmi') and
       (data_for_X.columns.values[i] != 's5') and
       (data_for_X.columns.values[i] != 'bp') and
       (data_for_X.columns.values[i] != 's3') and
       (data_for_X.columns.values[i] != 'sex') and
       (data_for_X.columns.values[i] != 's6')):
        data_X = data_for_X.loc[:, ['bmi','s5','bp','s3','sex','s6',data_for_X.columns.values[i]]]
        print('\nX = ', data_X.columns.values)
        lineaariregressio.teeLineaariRegressio(data_X, data_y)

#Ei tullut enää parannuksia R2:seen, joten valitaan muuttujiksi (bmi, s5, bp, s3, sex, s6)
data_X = data_for_X.loc[:, ['bmi','s5','bp','s3','sex','s6']]
print('\nX = ', data_X.columns.values)
malli = lineaariregressio.teeLineaariRegressio(data_X, data_y)



        
        
        
        
        
        
        
            










