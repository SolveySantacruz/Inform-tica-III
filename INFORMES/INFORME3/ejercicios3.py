nombre_completo = "Solvey Isleny Santacruz Zambrano"   #Por favor ingrese su nombre COMPLETO en la cadena

# ----------------------------Ejercicios INFORME 3--------------------------------

import numpy as np
import pandas as pd

#-----------EJERCICIO 2------------

import pandas as pd
archivo = "estudiantes.csv"
ruta = "INFORME3/" + archivo
hojaEstudiantes = pd.read_csv(ruta, index_col="codigo", dtype={"codigo":str})

codigosEst= hojaEstudiantes.index
promedios=hojaEstudiantes.mean(axis=1) #fila

promediosEstudiantes=pd.Series(data=promedios, index=codigosEst)
print(promediosEstudiantes)

data2=hojaEstudiantes.mean(axis=0)
index2=['examen1','examen2','examen3','examen4','examen5','examen6','examen7','examen8','examen9','examen10']

promediosExamenes=pd.Series(data=data2, index=index2)
mejorEstudiante=promediosEstudiantes.idxmax()
peorEstudiante=promediosEstudiantes.idxmin()

reporteEstudiantes = [promediosEstudiantes, promediosExamenes, mejorEstudiante, peorEstudiante]
#--------Ejercicio 3-------

ventas=["B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","A032-52Unidades","B001-29Unidades","A125-15Unidades","A032-22Unidades","P009-25Unidades","B005-20Unidades","B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","B005-20Unidades","B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades","Z278-30Unidades","Z025-24Unidades","P009-21Unidades","Z278-30Unidades","Z025-24Unidades","Z278-11Unidades","A001-91unidades","A032-52Unidades","B001-29Unidades","A125-15Unidades","A032-22Unidades","P009-25Unidades","B005-20Unidades","B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-11Unidades","A001-91unidades","A032-52Unidades","B001-29Unidades","A125-10Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-21Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-15Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","A032-22Unidades","P009-25Unidades","Z278-11Unidades","A001-91unidades"]

index1= ['A001','A011','A032','A125','B001','B005','P009','P019','R001','W307','Z052','Z025','Z278']

unidadesPorProducto={}
suma_A001=[]
suma_A011=[]
suma_A032=[]
suma_A125=[]
suma_B001=[]
suma_B005=[]
suma_P009=[]
suma_P019=[]
suma_R001=[]
suma_W307=[]
suma_Z052=[]
suma_Z025=[]
suma_Z278=[]

for unidades in ventas:
    if unidades[0:4]=='A001':
        suma_A001.append(int(unidades[5:7]))
        unidadesPorProducto['A001']=sum(suma_A001)
    elif unidades[0:4]=='A011':
        suma_A011.append(int(unidades[5:7]))
        unidadesPorProducto['A011']=sum(suma_A011)
    elif unidades[0:4]=='A032':
        suma_A032.append(int(unidades[5:7]))
        unidadesPorProducto['A032']=sum(suma_A032)
    elif unidades[0:4]=='A125':
        suma_A125.append(int(unidades[5:7]))
        unidadesPorProducto['A125']=sum(suma_A125)
    elif unidades[0:4]=='B001':
        suma_B001.append(int(unidades[5:7]))
        unidadesPorProducto['B001']=sum(suma_B001)
    elif unidades[0:4]=='B005':
        suma_B005.append(int(unidades[5:7]))
        unidadesPorProducto['B005']=sum(suma_B005)
    elif unidades[0:4]=='P009':
        suma_P009.append(int(unidades[5:7]))
        unidadesPorProducto['P009']=sum(suma_P009)
    elif unidades[0:4]=='P019':
        suma_P019.append(int(unidades[5:7]))
        unidadesPorProducto['P019']=sum(suma_P019)
    elif unidades[0:4]=='R001':
        suma_R001.append(int(unidades[5:7]))
        unidadesPorProducto['R001']=sum(suma_R001)
    elif unidades[0:4]=='W307':
        suma_W307.append(int(unidades[5:7]))
        unidadesPorProducto['W307']=sum(suma_W307)
    elif unidades[0:4]=='Z052':
        suma_Z052.append(int(unidades[5:7]))
        unidadesPorProducto['Z052']=sum(suma_Z052)
    elif unidades[0:4]=='Z025':
        suma_Z025.append(int(unidades[5:7]))
        unidadesPorProducto['Z025']=sum(suma_Z025)
    elif unidades[0:4]=='Z278':
        suma_Z278.append(int(unidades[5:7]))
        unidadesPorProducto['Z278']=sum(suma_Z278)

unidades=np.array(unidadesPorProducto.values())

ventasPorProducto=pd.Series(data=unidades, index=index1).astype(int)

media=int(ventasPorProducto.mean())
mediana=int(ventasPorProducto.median())
desviacion=int(ventasPorProducto.std())
maximo=int(ventasPorProducto.max())
minimo=int(ventasPorProducto.min())

estadisticas = [media, mediana,desviacion, maximo, minimo]

masVendido=ventasPorProducto.idxmax()
menosVendido=ventasPorProducto.idxmin()
extremos = [masVendido, menosVendido]

reporteVentas = [ventasPorProducto, estadisticas, extremos]

#-------Ejercicio 4---------
"""
    Dados dos arreglos numpy cualquiera (arreglo x, arreglo y) provenientes de una funcion arbitraria y = f(x)
    Cree una funcion que reciba dos arreglos numpy x, y. 
    Esta funcion debe graficar  y   = f(x)   
                                y'  = f'(x)  
                                y'' = f''(x)
    (Realice las 3 graficas sobre un mismo lienzo)
    La funcion se debe llamar graficaGenerica, guiese siguiendo el siguiente esquema:
       | def graficaGenerica(x, y):
       |     #Valores numericos   
       |     y_derivadaOrden1 = ...
       |     y_derivadaOrden2 = ...
       |
       |     #Grafica
       |     import matplotlib.pyplot as plt
       |     plt.figure()
       |     plt.subplot(1,3,1)
       |     plt.plot(...)      # y vs x
       |     plt.subplot(1,3,2)
       |     plt.plot(...)      # y' vs x
       |     plt.subplot(1,3,3)
       |     plt.plot(...)      # y'' vs x
       |     plt.legend()
       |     plt.show()
"""

def graficaGenerica(x, y):
#Valores numericos   
    y_derivadaOrden1 = np.diff(y)/np.diff(x)  #Pendientes
    y_derivadaOrden2 = np.diff(y,2)/(np.diff(x,2))

    
    
    #Grafica
    import matplotlib.pyplot as plt
    plt.figure()
    plt.subplot(1,3,1)
    plt.plot(y,x)      # y vs x
    plt.subplot(1,3,2)
    plt.plot(x[:-1],y_derivadaOrden1)      # y' vs x
    plt.subplot(1,3,3)
    plt.plot(x[:-2],y_derivadaOrden2)      # y'' vs x
    plt.legend()
    plt.show()

x = np.arange(0, 10.01, 0.01)
y=x**3-9*x
grafica=graficaGenerica(x,y)

# Terminar