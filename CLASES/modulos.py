# 26 de octubre 2022

import math 
"""
Imprimir las variables pi y euler, ejecutar al menos una función
de ese módulo. 
"""
print(dir(math))    #saber las funciones que contiene un módulo
print('pi =>',math.pi)
print('euler =>',math.e)
print('seno(pi/2) =>',math.sin(math.pi/2))

import random 
""" 
Imprimir 10 números aleatorios. Opciones: flotante del 0 al 1
Imprimir un número aleatorio entre:1,2,3,4,5
Imprimir un caracter aleatorio. Opciones: 'a','b','c'
"""

numeroAleatorio=random.random()
print('numeroAleatorio [0,1]')
for i in range(10):
    numeroAleatorio= random.random()
    print(numeroAleatorio)

print('numero aleatorio [1,2,3,4,5]')
for i in range(10):
    numeroAleatorio=random.choice([1,2,3,4,5])
    print(numeroAleatorio)

print('Caracter aleatorio a,b,c')
for i in range(10):
    caracterAleatorio=random.choice(['a','b','c'])
    print(caracterAleatorio)

import tqdm
"""
Ejecutar un for con una barra de progreso.
"""
# para descargar una librería, escribir en la terminal: pip install tqdm
# tqdm es el nombre de la librería.

for i in tqdm.tqdm(range(20000)):
    10*5
print('proceso terminado')

import calendar 
"""
Imprimir un calendario
"""
print(calendar.calendar(2022))

import numpy 
import matplotlib.pyplot as plt

"""
Utilizar la estructura básica de numpy: un arreglo luego
graficar usando matplotlib la función x**2+1
"""

arreglo1=numpy.array([1,2,3,4,5])
arreglo2=numpy.linspace(1,50,100)
arreglo3=arreglo2**2

plt.figure()
plt.plot(arreglo2,arreglo3)
plt.show()
