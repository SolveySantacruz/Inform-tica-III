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

# 02-noviembre-2022

#------Indexado y slicing de arreglos numpy-----------

# vector[columna]
# Matriz [fila, columna]
# Tensor [profundidad, fila, columna]


"""
Ejemplo: Acceder a 3 columnas distintas del vector 1
"""
value1=vector1[0] #primer elemento
value1=vector1[-1] #último elemento

"""
Ejemplo: Acceder al valor ubicado en la fila 1, columna 3 de una matriz
"""
value1=matriz2[0,2] 

"""
Ejemplo: Acceder a toda la fila2 de la matriz 2
          acceder a toda la columna 3 de la matriz 2
"""

filaEx=matriz2[1,:]
columnaEx=matriz2[2,:]

"""
Ejemplo: extraer la sección 4 5 a partir de la mattriz 2
                            7 8
"""
seccion=matriz2[1:,0:2]

"""
Cree la siguiente matriz y el siguiente vector

matriz= 1   2   3   4   5
        5   7   8   9  10
        11  12  13 14  15

vector= 1 2 3

Apile el vector a la matriz y luego extraiga una sección
compuesta por la filas 2(índice1) y la fila 3 (índice2)
"""

matriz=arange(1,16).reshape((3,5))

vector=array([1,2,3]).reshape((3,1))

matrizResultante = hstack((matriz, vector))
seccion1=matrizResultante[1:4,:]

print(seccion1)


#--------Funciones estadísticas mean, std, min, max--------------------

"""
Calcular la media del vector 1 y vector 2
"""

from numpy import mean, std,sum, savetxt

media1=mean(vector1) #también se puede vector1.mean
media2=mean(vector2) #también se puede vector1.mean

"""
Calcular la media de matriz 2
por fila, por columna y la  media de medias
"""
# axis=0 => es por columna
# axis=1 => es por fila

print(matriz2.mean(axis=0))
print(matriz2.mean(axis=1))
print(matriz2.mean()) #calcula la media total

"""
Ejemplo: determinar la desviación estándar por fila, columna, total
         determinar el máximo por fila, columna, total => max
         determinar el mínimo por fila, columna, total => min
"""

print(matriz2.std(axis=0))
print(matriz2.std(axis=1))
print(matriz2.std())

print(matriz2.max(axis=0))
print(matriz2.max(axis=1))
print(matriz2.max())

print(matriz2.min(axis=0))
print(matriz2.min(axis=1))
print(matriz2.min())


"""
Ejemplo: determine la media de productos vendidos por trabajador
determine la cantidad vendida por cada producto
determine el producto más vendido 
determine los dos producto menos vendidos
determine la cantidad de productos vendidos por trabajador

                                UNIDADES VENDIDAS        
CODIGO_EMPLEADO |  zapatos tenis camisas corbatas pantalones blusas vestidos 
     001        |    20      22     30      2        40        20      3    
     002        |    31      14     32      15       13        20      11   
     010        |    24      32     40      9        12        50      13   
     020        |    42      12     33      24       22        32      23   
     021        |    51      21     25      10       19        14      2    
     022        |    22      31     51      21       35        15      11   
     023        |    21      36     22      32       39        32      15   
     024        |    22      33     41      21       43        31      36   
     025        |    33      31     20      42       33        42      35   
     031        |    22      47     5       28       37        31      32   
     032        |    24      38     33      21       41        31      16   
     033        |    21      18     32      37       39        22      12   
     041        |    33      31     21      21       33        39      25   
     042        |    25      39     20      48       15        30      32   
     043        |    27      32     29      28       37        35      16   
     121        |    24      12     31      21       39        32      13   
     122        |    31      31     50      22       13        30      21   
     123        |    23      35     35      39       31        19      19   
     351        |    26      36     39      27       35        32      16   
     352        |    25      31     21      21       25        37      15   
     353        |    23      34     35      32       37        20      49   
     368        |    31      14     29      39       25        37      16   
     369        |    26      31     31      27       37        32      41   
     461        |    40      42     23      11       21        15      19   
     466        |    27      31     39   ,   21   ,    31 ,       3,2      25,   
     4,69       , |    38      32     19      29       35        50      16


"""


unidades= [[20,      22,     30,      2 ,       40,        20,      3 ],
           [31,      14,     32,      15,       13,        20,      11],
           [24,      32,     40,      9 ,       12,        50,      13],
           [42,      12,     33,      24,       22,        32,      23],
           [51,      21,     25,      10,       19,        14,      2 ],
           [22,      31,     51,      21,       35,        15,      11],
           [21,      36,     22,      32,       39,        32,      15],
           [22,      33,     41,      21,       43,        31,      36],
           [33,      31,     20,      42,       33,        42,      35],
           [22,      47,     5 ,      28,       37,        31,      32],
           [24,      38,     33,      21,       41,        31,      16],
           [21,      18,     32,      37,       39,        22,      12],
           [33,      31,     21,      21,       33,        39,      25],
           [25,      39,     20,      48,       15,        30,      32],
           [27,      32,     29,      28,       37,        35,      16],
           [24,      12,     31,      21,       39,        32,      13],
           [31,      31,     50,      22,       13,        30,      21],
           [23,      35,     35,      39,       31,        19,      19],
           [26,      36,     39,      27,       35,        32,      16],
           [25,      31,     21,      21,       25,        37,      15],
           [23,      34,     35,      32,       37,        20,      49],
           [31,      14,     29,      39,       25,        37,      16],
           [26,      31,     31,      27,       37,        32,      41],
           [40,      42,     23,      11,       21,        15,      19],
           [27,      31,     39,      21,       31,        32,      25],
           [38,     32,     19,      29,       35,        50,      16]] 

dataArray=array(unidades)

medias=dataArray.std(axis=1)
Cantidad=dataArray.std(axis=0)

print('producto menos vendido => ')

print('Cantidad por trabajador',dataArray.sum(axis=1))

# where(dataArray)

"""
Ejemplo: Como guardar un arreglo 
"""

savetxt('ventasTrabajadores.cvs',dataArray)