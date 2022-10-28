"""
Crear los siguientes vectores, matrices y tensores

vector1= 1,2,3,4,5
vector2=10,20,30,40,50

matriz1= [1 1 1
          1 1 1
          1 1 1]

matriz2= [1 2 3
          4 5 6
          7 8 9]

tensor1=[[1 1 1
          1 1 1
          1 1 1]
         [2 2 2
          2 2 2
          2 2 2]]

tensor2=[[1 2 3
          4 5 6
          7 8 9]
        [10 11 12
         13 14 15
         16 17 18]]
"""

# Cómo crear los vectores
from numpy import array, arange, ones,hstack, vstack

vector1= array([1,2,3,4,5])
vector2= array([10,20,30,40,50])

# Cómo crear matrices numpy

matriz1= array([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])

matriz2= array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

sumaMatrices=matriz1+matriz2 

tensor1=array([[[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]],

                [[2, 2, 2],
                 [2, 2, 2],
                 [2, 2, 2]]])

tensor2=array([[[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]],

               [[10, 11, 12],
                [13, 14, 15],
                [16, 17, 18]]])

"""
Ejemplos: como crear los anteriores elementos de manera rápida.
"""
vector1=arange(1,6,1)   #Inicio, fin, salto
vector2=arange(10,51,10)

matriz1=ones((3,3))   #Tamaño (filas,columnas)
matriz2=arange(1,10).reshape((3,3)) #Redimensionar

tensor2=arange(1,19).reshape((2,3,3))

"""
Ejemplos: cómo apilar vector 1 y 2 y formar vector más grande
          cómo apilar vector 1 y 2 y formar una matriz
          Cómo apilar matriz1 y matriz1 y formar matriz más grande
          Cómo apilar matriz1 y matriz1 y formar un tensor 
"""

vectorResultante=hstack((vector1,vector2))

matrizResultante= vstack((vector1,vector2))

matrizAncha=hstack((matriz1,matriz2))
matrizAncha=vstack((matriz1,matriz2))

"""
Ejercicio: como apilar un vector con una matriz horizontal y verticalmente.
"""


