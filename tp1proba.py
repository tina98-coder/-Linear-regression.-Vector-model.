from __future__ import division
# -*- coding: utf-8 -*-
from numpy import *
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.animation as animation


def calculer_cost_function(theta_0, theta_1):
    global_cost  = 0
    for i in range(len(X)):
        cost_i = ((theta_0 + (theta_1 * X[i])) - Y[i]) * ((theta_0 + (theta_1 * X[i])) - Y[i]) 
        global_cost+= cost_i
    return (1/ (2 * len(X))) * global_cost

# X = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
# Y =[43, 45, 48, 51, 55, 57, 59, 63, 66, 68]  

# changer par votre chemin de fichier local
df = pd.read_csv("D:\L3clermont\TpProba\TP01\val.csv")

X =  df.iloc[0:len(df),0]#une seule variable predictive car regression univarie
Y =  df.iloc[0:len(df),1]#Valeurs observees (a predire)


#un tableau pour stocker les valeurs d'erreurs global a chaque tour d'iteration
COST_RECORDER = []

# la taille de notre ensemble de donnees d'apprentissage
M = len(X)

learning_rate_ALPHA = float(0.0001)
initial_theta_0 = float(0)
initial_theta_1 = float(0)
nombre_iterations = 2000


def calculer_derivees_partielles(ancien_theta_0, ancien_theta_1):
    derivee_theta_0 = float(0)
    derivee_theta_1 = float(0)
    for i in range(0, len(X)):
        derivee_theta_0 += float(((ancien_theta_0 + (ancien_theta_1 * X[i])) - float(Y[i])))
        derivee_theta_1 += (((ancien_theta_0 + (ancien_theta_1 * X[i]))) - float(Y[i])) * float(X[i])  
    derivee_theta_0 = (1/M) * derivee_theta_0
    derivee_theta_1 = (1/M) * derivee_theta_1
    return [derivee_theta_0, derivee_theta_1]

def calculer_nouvelles_theta(ancien_theta_0, ancien_theta_1):
    [derivee_theta_0, derivee_theta_1] = calculer_derivees_partielles(ancien_theta_0,ancien_theta_1)
    nouvelle_theta_0 = ancien_theta_0 - (learning_rate_ALPHA * derivee_theta_0)
    nouvelle_theta_1 = ancien_theta_1 - (learning_rate_ALPHA * derivee_theta_1)
    COST_RECORDER.append(calculer_cost_function(nouvelle_theta_0, nouvelle_theta_1))
    return [nouvelle_theta_0,nouvelle_theta_1]


def lancer_gradient_descent():
    tmp_theta_0 = initial_theta_0
    tmp_theta_1 = initial_theta_1   
    for i in range(nombre_iterations):
        [nouvelle_theta_0, nouvelle_theta_1] = calculer_nouvelles_theta(tmp_theta_0, tmp_theta_1)
        tmp_theta_0 = nouvelle_theta_0
        tmp_theta_1 = nouvelle_theta_1
    return [tmp_theta_0, tmp_theta_1]         

[final_theta_0, final_theta_1] = lancer_gradient_descent()
print(final_theta_0, final_theta_1)

# print "After {0} iterations theta_0 = {1}, theta_1 = {2}".format(nombre_iterations, final_theta_0, final_theta_1)


#print COST_RECORDER

xx = []; yy=[]

#dessiner l'avancer des differents de J(theta_0, theta_1)
for i in range(len(COST_RECORDER)):
   xx.append(i)
   yy.append(COST_RECORDER[i])

axes = plt.axes()
axes.grid()
plt.xlabel('Axe des X')
plt.ylabel('Axe des Y')
plt.scatter(X,Y)
plt.show()

