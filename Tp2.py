import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm as nr 
import statistics
from scipy.stats import expon as exp
##################  EXO1 #################
f1=np.random.binomial(30, 0.5, 100)
f2=np.random.binomial(30, 0.7, 100)
f3=np.random.binomial(50, 0.4, 100)

plt.hist(f1, color='red')
plt.hist(f2, color= 'yellow')
plt.hist(f3, color='blue')
plt.show()

##################  EXO2 #################

normale1=np.random.normal(0,1,100)
normale2=np.random.normal(2,1.5,100)
normale3=np.random.normal(2,0.6,100)
plt.hist(normale1, color='red')
plt.hist(normale2, color='yellow')
plt.hist(normale3, color='blue')
plt.show()


############### EXO3 #########################
normale_centre_reduite=np.random.normal(0,1,40)
plt.hist(normale_centre_reduite)


X=np.arange(-6,6,0.1)
Y=nr.pdf(X,0,1)
plt.plot(X,Y)
plt.show()


############ EXO4 partie 1 #############################
#generation d'un echantillion de taille N selon N(0,1)
Loi_univar1=np.random.normal(0,1,20)
Loi_univar2=np.random.normal(0,1,80)
Loi_univar3=np.random.normal(0,1,150)

#calcul les esatimations  par MV de u et sigma a partir de l'echantillon generer
esp1 = statistics.mean(Loi_univar1)
esp2 = statistics.mean(Loi_univar2)
esp3 = statistics.mean(Loi_univar3)

variance1=statistics.variance(Loi_univar1)
variance2=statistics.variance(Loi_univar2)
variance3=statistics.variance(Loi_univar3)
#print(esp1,esp2,esp3)
#print(variance1,variance2,variance3)

#pour x calcule de la fonction de densite probabilite theorique et la la fonction de densite probabilite estime pour x

theorique=np.arange(-5,5,0.1)
val1=nr.pdf(theorique,0,1)
plt.plot(theorique,val1, color='red')

estimee1=np.arange(-5,5,0.1)
val2=nr.pdf(estimee1,esp1,variance1)
plt.plot(estimee1,val2,color='yellow')

estimee2=np.arange(-5,5,0.1)
val3=nr.pdf(estimee2,esp2,variance2)
plt.plot(estimee2,val3, color='blue')

estimee3=np.arange(-5,5,0.1)
val4=nr.pdf(estimee3,esp3,variance3)
plt.plot(estimee3,val4, color='green')

#plt.show()


############# EXO4 partie 2####################
#generation d'un echantillon i.i.d de taille n selon la loi exponentielle de parametre l'anda .
Loi_expo1=np.random.exponential(1.5,20)
Loi_expo2=np.random.exponential(1.5,80)
Loi_expo3=np.random.exponential(1.5,150)

#calcule de lestimation par MV de landa a partir de l'echantillon generer
esp_expo_1 = statistics.mean(Loi_expo1)
esp2_expo_2 = statistics.mean(Loi_expo2)
esp3_expo_3 = statistics.mean(Loi_expo3)

variance_expo1=statistics.variance(Loi_expo1)
variance_expo2=statistics.variance(Loi_expo2)
variance_expo3=statistics.variance(Loi_expo3)

print(esp_expo_1,esp2_expo_2,esp3_expo_3)
print(variance_expo1,variance_expo2,variance_expo3)

#pour x, calcule la fonction de densite probabilite theorique
theorique_expo=np.arange(0,8,0.1)
val_expo=exp.cdf(theorique_expo,1.5)
plt.plot(theorique_expo,val_expo, color='red')

#pour x calcule fonction de densite probabilite estimee
estimee_expo1=np.arange(0,8,0.1)
val_expo1=exp.cdf(estimee_expo1,esp_expo_1,variance_expo1)
plt.plot(estimee_expo1,val_expo1,color='yellow')

estimee_expo2=np.arange(0,8,0.1)
val_expo2=exp.cdf(estimee_expo2,esp2_expo_2,variance_expo2)
plt.plot(estimee_expo2,val_expo2, color='blue')

estimee_expo3=np.arange(0,8,0.1)
val_expo3=exp.cdf(estimee_expo3,esp3_expo_3,variance_expo3)
plt.plot(estimee_expo3,val_expo3, color='green')
plt.show()
