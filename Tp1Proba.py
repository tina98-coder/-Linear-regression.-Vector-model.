import math
import statistics
import numpy as np
import matplotlib.pyplot as plt

def Reg_linaire_simple(X,Y):
    espx = statistics.mean(X)
    espy = statistics.mean(Y)
    sumxy=0
    sumxx=0
    for i,j in zip(X,Y):
        a=(i-espx)
        b=(j-espx)
        covxy=(a*b)
        covxx=(a*a)
        sumxy=sumxy+covxy
        sumxx=sumxx+covxx
        
    alpha1=sumxy/sumxx
    alpha0=espy - (alpha1*espx)
    return(alpha1,alpha0)

def Model_vetoriel(X,Y):
    a=np.array([[1]*len(X),X]) #matrice transposer
    y=np.transpose(a)#matrice normal
    ATA= a.dot(y)#produit matrice transposer et lamatrice nrml
    inv_ATA=np.linalg.inv(ATA)#inverse de la matrice transposer
    beta=inv_ATA.dot(a.dot(Y))#produit de la matrice inverse et matrice transposeret la la liste Y
    return beta

X=[45,50,55,60,65,70,75,80,85,90]
Y=[43,45,48,51,55,57,59,63,66,68]
beta0,beta1=Reg_linaire_simple(X,Y)
X1=[20,82]
Y1=[(X1[0]*beta1)+beta0,(X1[1]*beta1)+beta0]
print(Y1)
Reg_linaire_simple(X,Y)
X2=[50,55]
Y2=[45,60]
P = Model_vetoriel(X2,Y2)

plt.plot(X,Y,"b:o")
plt.plot(X1,Y1,"r--")
plt.plot(P,"r--")
plt.show()

           
            
      
        
        
