# 11 de noviembre 2022

import pandas as pd
import numpy as np

"""
Crear un dataframe con 3 columnas: ['F1','F2,'F3']
                      100 índices: [0, 0.01,0.02,...1]

F1(x)=x*sin(x)+ 0.5*random(x)
F2(x)=cos(x)+2*random(x)
F3(x)=x+1/2
"""

x = np.arange(0.01, 1.01, 0.01)
columna1 = (x * np.sin(x) + 0.2 * np.random.rand(100)).reshape(100,1)
columna2 = (np.cos(x) + 0.1 * np.random.rand(100)).reshape(100,1)
columna3 = (x * 1/2).reshape(100,1)
data = np.hstack((columna1, columna2, columna3))

hoja1 = pd.DataFrame(data= data,
                     index= np.arange(0.01, 1.01, 0.01),
                     columns= ["F1", "F2", "F3"]
)

print(hoja1)


"""
Graficar F1(x), F2(x),F3(x)
"""
import matplotlib.pyplot as plt 

def graficaGenerica(x,y,marca):
    plt.figure() #Para crear lienzo vacío
    plt.plot(x,y,marca)
    plt.show() #Para mostrar la figura

x= hoja1.index
y=hoja1['F1']
graficaGenerica(x,y,'--')

x = hoja1.index
y = hoja1["F2"]
graficaGenerica(x, y, "--")

x = hoja1.index
y = hoja1["F3"]
graficaGenerica(x, y, "--")












