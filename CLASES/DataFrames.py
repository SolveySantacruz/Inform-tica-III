# 09 de noviembre 2022

"""crear un dataFrame compuesto por la siguiente informacion =>
codigo   tamaño   precio  
  001      1       12000   
  002      2       15000 
  003      3       21000
  004      2       32000
  005      1       11000
  006      2       90000"""

import numpy as np
import pandas as pd

data = np.array([[1, 12000],   
                 [2, 15000], 
                 [3, 21000],
                 [2, 32000],
                 [1, 11000],
                 [2, 90000]])

hoja1 = pd.DataFrame( data = data,
                      columns = ["tamaño", "precio"],
                      index = ["001","002","003","004","005","006"])

print(hoja1)

"""
Crear un DataFrame que cumpla con lo siguiente:
Cada columna va a ser 5 funciones: ['f1','f2','f3','f4','f5']
los índices van a ser la variable independiente: [0, 0.5, 1, 1.5, 200]

f1(x)= 3x+5
f2(x)=x+random
f3(x)=sin(x)
f4(x)=e^x
f5(x)= x*sin(x)+random
  |  f1     f2      f3     f4     f5
----------------------------------------
0   |  5    | 0.3  |   0  |  2.71 |  0
0.5 |  6.5  | 0.7  |   .  |   .   |  .
1   |  8    | 1.2  |   .  |   .   |  .
1.5 |  9.5  | 1.6  |   .  |   .   |  .
.   |  .    | .    |   .  |   .   |  .
.   |  .    | .    |   .  |   .   |  .
.   |  .    | .    |   .  |   .   |  .
200 |  605  | 200.2|   .  |   .   |  .
"""

x = np.arange(0,200.5, 0.5)
f1 = 3 * x + 5
f2 = x + np.random.rand(401)
f3 = np.sin(x)
f4 = np.exp(x)
f5 = x * np.sin(x) + np.random.rand(401)

f1 = f1.reshape((401,1))
f2 = f2.reshape((401,1))
f3 = f3.reshape((401,1))
f4 = f4.reshape((401,1))
f5 = f5.reshape((401,1))
data = np.hstack((f1,f2,f3,f4,f5))

hoja2 = pd.DataFrame(data=data,
                     columns=["f1","f2","f3","f4","f5"],
                     index = np.arange(0,200.5,0.5))

print(hoja2)


"""
Ejercicio: Determinar las medias, medianas, desviaciones estandar, minimos y maximos
por filas y por columnas
"""

medias = hoja2.mean(axis=0)
medianas = hoja2.median(axis=0)
desviaciones = hoja2.std(axis=0)
minimos = hoja2.min(axis=0)
maximos = hoja2.max(axis=0)

print(hoja2)
print("-----------------------")
print("minimos =>", minimos)
print("maximos =>", maximos)


#11 de noviembre del 2022


#--------Indexado de Dataframes-----------

# El indexado se trabaja igual que los arreglos numpy-
# Además, se puede acceder por  clave
arreglo=np.arange(1,25).reshape(3,8)

hoja3=pd.DataFrame(data=arreglo,
                  columns= ['col1','col2','col3','col4','col5','col6','col7','col8'],
                  index=['Alex','Juan','Maria'])

print(hoja3)

"""
Acceder a toda la columna col3
Acceder a toda la fila Alex
"""

columna=hoja3['col3']
fila=hoja3.loc['Alex']

print(columna)

"""
Acceder a un valor específico (fila, columna)
                              (Maria,col2)
"""

resultado=hoja3.loc['Maria','col2']
print('resultado',resultado)

#indexado con iloc, para acceder a índices

