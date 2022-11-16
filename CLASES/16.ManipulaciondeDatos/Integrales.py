# 16 de noviembre

#---------Integrales numéricas-----------

"""
Se resuelve utilizando el método del trapecio (calculando áreas).
"""
"""
Ejemplo: calcular la integral para f(x)= 2X^2, en los límites x=[0,5].
La integral debe dar (2/3)X^3 = 83.33
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def graficaGenerica(x,y):
    plt.figure()
    plt.plot(x,y,'o')
    plt.show()

x= np.arange(0,5.0001,0.0001)
y=2*x**2

integralNumerica= np.trapz(y,x)

print('Integral numérica => ',integralNumerica)


"""
Ejercicio:
Calcular las integrales f1,f2 y f3 del siguiente DataFrame
Graficar las f1,f2,f3 en un mismo lienzo
"""

x = np.arange(0, 6.28, 0.01)
columna1 = x * np.sin(x) + 0.005 * np.random.rand(628)
columna2 = np.cos(x) + 0.005 * np.random.rand(628)
columna3 = x * 1/2
data = np.hstack((columna1.reshape(628,1), columna2.reshape(628,1), columna3.reshape(628,1)))
hoja1 = pd.DataFrame(data= data,
                     index= x,
                     columns= ["f1", "f2", "f3"])

def graficaGenerica(x,y,marca):
    plt.figure() #Para crear lienzo vacío
    plt.plot(x,y,marca)
    plt.show() #Para mostrar la figura


plt.figure(figsize=(12,4)) #Para crear lienzo vacío
for i in range(1,4):

    plt.subplot(1,3,i)
    x= hoja1.index
    y=hoja1.iloc[:,i-1]
    plt.plot(x,y,'--')
    plt.savefig('lienzo')   
plt.show() #Para mostrar la figura

for i in range(0,3):
    x= hoja1.index
    y=hoja1.iloc[:,i]
    integral_numerica=np.trapz(y,x)
    print('Integral f{}'.format (i+1), integral_numerica)







