#neuroverkon toiminta

import numpy as np

# yksi neuroni
def neuroverkko(syotteet, painot):
    tulos = syotteet.dot(painot)
    return tulos

# 1 syöte ja 1 neuroni (1 X 1 painokerrointa) -> 1 tulos
x=np.array([3.6])
w=np.array([0.15])
tulos1=neuroverkko(x,w)

# 3 syötettä ja 1 neuroni
x=np.array([3.6,0.65,7])
w=np.array([0.1,0.2,0.05])
tulos2=neuroverkko(x,w)


# monta neuroverkkoa
def neuroverkko(syotteet, painot):
    tulos = syotteet.dot(painot.T)
    return tulos

# 3 syötettä ja 3 neuronia (3 X 3 painokerrointa) -> 3 tulosta
x=np.array([3.6,0.65,7])
w=np.array([[0.15,0.1,0.05],
            [0.1,0.2,0.05],
            [0.1,0.3,0.1]])
tulos3=neuroverkko(x,w)


# monta neuronia + piilokerros
def neuroverkko(syotteet, painot):
    piilo = syotteet.dot(painot[0].T)
    tulos = piilo.dot(painot[1].T)
    return tulos

# 3 syötettä ja 3 neuronia (piilokerros) (3 X 3 painokerrointa) ->
# 3 tulosta, jotka syötteinä 2 neuronin tuloskerrokseen (3 X 2 painokerrointa) ->
# 2 tulosta
x = np.array([3.6,0.65,7])
w1 = np.array([[0.15,0.1,0.05],
               [0.1,0.2,0.05],
               [0.1,0.3,0.1]])
w2 = np.array([[0.2,0.2,0.2],
               [0.4,0.3,0.2]])
w = np.array([w1,w2])

tulos4 = neuroverkko(x,w)


























