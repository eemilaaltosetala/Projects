# neuroverkon opettaminen

import numpy as np

# yksi neuroni
def neuroverkko(syotteet, painot):
    tulos = syotteet.dot(painot)
    return tulos

def opeta(syotteet, painot, tulos, toistolkm=4):
    print("Syöte:", syotteet, "Oikea tulos:", tulos)
    for i in range(toistolkm):
        print("-----\nPaino:", str(painot))
        ennuste = neuroverkko(syotteet, painot)
        virhe = (ennuste - tulos)**2
        delta = ennuste - tulos
        paino_deltat = delta*syotteet
        painot = painot - paino_deltat
        print("Ennuste:", str(round(ennuste,2)),
              "MSE:", str(round(virhe,6)))
        print("Painonmuutos:", str(paino_deltat))
    return painot

# esimerkki: 1 syöte ja 1 neuroni (1 X 1 painokerrointa) -> 1 tulos
x=np.array([3.6])
w=np.array([0.15])
y=0.8

w = opeta(x,w,y,5)

print(w)

# lisätään alfa
def opeta(syotteet, painot, tulos, alfa, toistolkm=4):
    print("Syöte:", syotteet, "Oikea tulos:", tulos)
    for i in range(toistolkm):
        print("-----\nPaino:", str(painot))
        ennuste = neuroverkko(syotteet, painot)
        virhe = (ennuste - tulos)**2
        delta = ennuste - tulos
        paino_deltat = delta*syotteet
        painot = painot - alfa*paino_deltat
        print("Ennuste:", str(round(ennuste,2)),
              "MSE:", str(round(virhe,6)))
        print("Painonmuutos:", str(alfa*paino_deltat))
    return painot

x=np.array([3.6])
w=np.array([0.15])
y=0.8
alfa=0.012

w = opeta(x,w,y,alfa,5)
w = opeta(x,w,y,alfa,15)  
print(w)                


# monta neuronia
def opeta(syotteet, painot, tulokset, alfa, toistolkm=4):
    print("Syöte:", syotteet, "Oikea tulos:", tulokset)
    for i in range(toistolkm):
        print("------------------------\nPaino:", str(painot))
        ennusteet = neuroverkko(syotteet, painot)
        virheet = (ennusteet - tulokset)**2
        deltat = ennusteet - tulokset
        paino_deltat = np.outer(deltat,syotteet)  #np.outer tekee vektorien elementtien kertolaskuista matriisin
        painot = painot - alfa*paino_deltat
        print("Ennuste:", str(ennusteet),
              "MSE:", str(virheet))
        print("Painonmuutos:", str(alfa*paino_deltat))
    return painot

# esimerkki: 3 syötettä ja 3 neuronia ( 3 X 3 painokerrointa) -> 3 tulosta
x=np.array([3.6,0.65,7])
w=np.array([[0.0,0.0,0.0],
            [0.0,0.0,0.0],
            [0.0,0.0,0.0]])
y=np.array([0.9,0.84,1.2])
alfa=0.01
w=opeta(x,w,y,alfa,8)
w=opeta(x,w,y,alfa,30)
print(w)              # painokertoimet


# monta neuronia + piilokerros + aktivointifunktio
# lisätään aktivointifunktio ReLU
def reLu(x):
    return (x > 0) * x     # palauttaa x:n, jos x on positiivinen, muuten 0
def reLu_derivaatta(x):
    return x > 0           # palauttaa 1, jos positiivinen, muuten 0

def opeta(syotteet, painot1, painot2, tulokset, alfa, toistolkm=4):
        print("Syöte:", syotteet, "Oikea tulos:", tulokset)
        for toisto in range(toistolkm):
            virhe = 0
            for i in range(len(syotteet)):
                syote_kerros = syotteet[i:i+1]
                piilo_kerros = reLu(np.dot(syote_kerros,painot1))
                tulos_kerros = np.dot(piilo_kerros,painot2)
                virhe += np.sum((tulos_kerros-tulokset[i:i+1])**2)
                delta_tulos = tulokset[i:i+1]-tulos_kerros
                delta_piilo = delta_tulos.dot(painot2.T)*reLu_derivaatta(piilo_kerros)
                painot2  += alfa * piilo_kerros.T.dot(delta_tulos)
                painot1  += alfa * syote_kerros.T.dot(delta_piilo)
            # näytetään virheen suuruus vain joka kymmenes toistokerta
            if (toisto%10 ==9):
                print("Virhe:", str(virhe))
        return(painot1, painot2)
    
x = np.array([[1,0,1],
              [0,1,1],
              [0,0,1],
              [1,1,1]])
y = np.array([[1,1,0,0]]).T

alfa = 0.2
piilo_koko = 4

# asetetaan painot alussa satunnaisiksi
np.random.seed(1)
# painot syöte- vs. piilokerros
w1 = 2*np.random.random((3,piilo_koko)) - 1
# painot piilo- vs. tuloskerros
w2 = 2*np.random.random((piilo_koko,1)) - 1

w1, w2 = opeta(x,w1,w2,y,alfa,60)

print(w1)
print(w2)
















    
    
    
    
    
    
    
    
    
    
    
    