import numpy as np
import math
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
def moy_emp(X):
    sum=0
    for i in X:
        sum = sum + i
    X_bar = sum / len(X)

    return X_bar

X=[0.499 ,0.509, 0.501 ,0.494 ,0.498 ,0.497 ,0.504 ,0.506, 0.502,
0.496 ,0.495 ,0.493, 0.507, 0.505 ,0.503 ,0.491] 
#Calcule de la moyenne empirique
X_n=moy_emp(X)

plt.hist(X, density = True)
plt.show()


#4/Determinisation dun intervalle de confiance pour u au niveau 95 sur 100 et 99 sur 100
variance = np.var(X)




alpha1 = 0.05/2
alpha2 = 0.01/2
u1 = 1 - alpha1
u2 = 1 -  alpha2
print(u1)
print(u2)

u1_1 = 1.96  # 1.9 +0.06 
u1_2 = 2.6 # 2.6 + 0

racine_n = math.sqrt(len(X))
var_sur_racine_n = variance / racine_n
u_var_sur_racine_n = u1_1 * var_sur_racine_n

I1 = X_n - u_var_sur_racine_n
I2 = X_n + u_var_sur_racine_n

Interval = [I1, I2]

u1_2_var_sur_racine_n = u1_2 * var_sur_racine_n

I1_2 = X_n - u1_2_var_sur_racine_n
I2_2 = X_n + u1_2_var_sur_racine_n

Interval2 = [I1_2, I2_2]

print(Interval)
print(Interval2)

# Question2
X2=[85.06 ,91.44, 87.93 ,89.02 ,87.28 ,82.34 ,86.23, 84.16,
88.56, 90.45, 84.91, 89.90, 85.52, 86.75 ,88.54 ,87.90]

X_n2=moy_emp(X2)




variance2 = np.var(X2)




alpha = 0.05/2

u11 = 1 - alpha

print(u11)


u = 1.96  # 1.9 +0.06 


racine_n2 = math.sqrt(len(X2))
var_sur_racine_n2 = variance2 / racine_n2
u_var_sur_racine_n2 = u * var_sur_racine_n2

I11 = X_n2 - u_var_sur_racine_n2
I21 = X_n2 + u_var_sur_racine_n2





Interval22 = [I11, I21]

print(Interval22)


# EXO3
def loi_bin_normal():
    n1 = 500

    p1 = float(95 / 500)

    X_n1 = 95



    un_moin_p = 1 - p1 
    un_moin_p_fois_xn= X_n1 * un_moin_p
    varinc = math.sqrt(un_moin_p_fois_xn)
    alpha1 = 0.05/2

    val_u1 = 1 - alpha1


    val_u = 1.96  # 1.9 +0.06 

    racine_n = math.sqrt(n1)
    var_sur_racine_n = varinc / racine_n
    u_var_sur_racine_n = val_u * var_sur_racine_n

    I1 = X_n1 - u_var_sur_racine_n
    I2 = X_n1 + u_var_sur_racine_n

    Interval = [I1, I2] 
    print(Interval)

loi_bin_normal()


# EXO4
def loi_bin_normal2(n):
    
    p1 = 0.5

    X_n1 = n * p1

    print(X_n1)

    un_moin_p = 1 - p1 
    un_moin_p_fois_xn= X_n1 * un_moin_p
    varinc = math.sqrt(un_moin_p_fois_xn)
    alpha1 = 0.05/2

    val_u1 = 1 - alpha1


    val_u = 1.96  # 1.9 +0.06 

    racine_n = math.sqrt(n)
    var_sur_racine_n = varinc / racine_n
    u_var_sur_racine_n = val_u * var_sur_racine_n

    I1 = X_n1 - u_var_sur_racine_n
    I2 = X_n1 + u_var_sur_racine_n

    Interval = [I1, I2] 
    print(Interval)

loi_bin_normal2(500)
