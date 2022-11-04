# 04 de noviembre 2022

"""
Crear las siguientes series

*Venta de productos
    código     001  002  003  004  005  006  007  008  009  010  011  012  013  014  015 
    cantidades  22   3   21   10   15   18   14   13   22   12   98    32   51   45   60

*calificaciones

 Nombre              Nota 
    Miguel Pineda        1.0 
    Maria Gonzalez       3.1 
    Jose Nuñez           5.0 
    Angelica Lozano      3.1 
    Camilo Suarez        3.2 
    Mariana Rosero       5.0 
    Esteban Quesada      3.4 
    Julia Quintero       2.0 
    Mauricio Lizcano     3.7 
    Angie Gomez          4.1 
    Camilo Restrepo      5.0 
    Mauricio Velazquez   5.0 
    Esteban Rodriguez    3.2 


 * Rendimiento deportivo
   
   Cod. Deportista (str) =>   001   002   003   004   005   006   007   008   009    010   011   012    013    014    015    016    017   018  019  020  021  022   023   024   025  026  027   028   029   030   031   032   033    034    035   036    037   038   039   040 041   042   043   044   045  046   047   048   049   050   051  052    053    054   055   056   057   058   059  060  061   062   063   064   065   066  067   068   069   070   071   072   073    074   075   076    077   078   079   080   081   082   083   084   085  086   087   088   089   090   091  092    093    094   095    096   097  098  099  100
   rendimiento     (str) =>   A     B     C     B     B     B     C     B     A      C     B     A      C      B      B      B      B     A    B    A    A    C     B     B     B    B    C     B     B     C     B     A     C      B      A     C      B     B     B     C   B     C     B     A     C     B    A     C     B     B     B    B      A      B     A     A     C     B     B    B    B     C     B     B     C     B    A     C     B     A     C     B     B      B     C     A      B     C     B     B     A     B     C     B     B    B     B     B     A     B     B    A      C      B     B      B     B    A    B    B  

"""


import pandas as pd 
import numpy as np

data =np.array([22, 3,  21, 10, 15, 18, 14, 13, 22, 12, 98, 32, 51, 45, 60])
index = ["001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012", "013", "014", "015"]
serieVentas = pd.Series(data = data, index=index)

print(serieVentas)


index = ["Miguel Pineda","Maria Gonzalez","Jose Nuñez","Angelica Lozano","Camilo Suarez","Mariana Rosero","Esteban Quesada","Julia Quintero","Mauricio Lizcano","Angie Gomez","Camilo Restrepo","Mauricio Velazquez","Esteban Rodriguez"]
data = [1.0,3.1,5.0,3.1,3.2,5.0,3.4,2.0,3.7,4.1,5.0,5.0,3.2]
serieCalificaciones = pd.Series(data=data, index=index)
print(serieCalificaciones)


index =  ["001",   "002",   "003",   "004",   "005",   "006",   "007",   "008",   "009",    "010",   "011",   "012",    "013",    "014",    "015",    "016",    "017",   "018",  "019",  "020",  "021",  "022",   "023",   "024",   "025",  "026",  "027",   "028",   "029",   "030",   "031",   "032",   "033",    "034",    "035",   "036",    "037",   "038",   "039",   "040", "041",   "042",   "043",   "044",   "045",  "046",   "047",   "048",   "049",   "050",   "051",  "052",    "053",    "054",   "055",   "056",   "057",   "058",   "059",  "060",  "061",   "062",   "063",   "064",   "065",   "066",  "067",   "068",   "069",   "070",   "071",   "072",   "073",    "074",   "075",   "076",    "077",   "078",   "079",   "080",   "081",   "082",   "083",   "084",   "085",  "086",   "087",   "088",   "089",   "090",   "091",  "092",    "093",    "094",   "095",    "096",   "097",  "098",  "099",  "100"]
data =   np.array(["A","B","C","B","B","B","C","B","A","C","B","A", "C",  "B",  "B",  "B",  "B", "A","B","A","A","C", "B", "B", "B","B","C", "B", "B", "C", "B", "A", "C",  "B",  "A", "C",  "B", "B", "B", "C",   "B", "C", "B", "A", "C", "B","A", "C", "B", "B", "B","B",  "A",  "B", "A", "A", "C", "B", "B","B","B", "C", "B", "B", "C", "B","A", "C", "B", "A", "C", "B", "B",  "B", "C", "A",  "B", "C", "B", "B", "A", "B", "C", "B", "B","B", "B", "B", "A", "B",  "B", "A","C","B",  "B","B",  "B", "A", "B", "B"])
serieDeportistas = pd.Series(data=data, index=index)
print(serieDeportistas)


"""
Imprimir los índices, datos del arreglo serieVentas utilizando
sus atributos. 
"""
print('índices => ', serieVentas.index)
print('data => ', serieVentas.values)
print('tamaño => ', serieVentas.shape)

"""
Imprimir la media, la desviación estándar, el min y el max de la serie calificaciones.
"""
print(serieCalificaciones.mean())
print(serieCalificaciones.std())
print(serieCalificaciones.min())
print(serieCalificaciones.max())

"""
Imprimir el código del producto menos vendido y el del producto más vendido 
"""
menosVendido= serieVentas.idxmin()
masVendido=serieVentas.idxmax()

"""
Acceder mediante indexado a 3 valores de la serieDeportistas utilizando 
el índice numérico y el índice clave.
"""

val1= serieDeportistas[0]
val2=serieDeportistas[-1]

val4=serieDeportistas['001']
val5=serieDeportistas['100']

"""
El precio de venta de los artículos de una empresa es el siguiente:
       Producto            Precio unitario
         A001                 $ 31 000
         A011                 $ 25 000
         A032                 $ 43 000
         A125                 $ 55 000
         B001                 $ 10 000
         B005                 $ 20 000
         P009                 $ 30 000
         P019                 $ 49 000
         R001                 $ 60 000
         W307                 $ 90 000
         Z052                 $ 35 000
         Z025                 $ 27 000
         Z278                 $ 65 000

Las ventas a lo largo de un día se ha registrado en la siguiente lista:
ventas = ["A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades", "P009-25Unidades", "B005-20Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-11Unidades","A001-91unidades"]

a) Crear 2 series => seriePrecioProductos (con codigos (str) y precios (int))
                  => serieVentasProductos (con codigos (str) y unidades vendidas(int))

b) Calcular de serie serieVentasProductos lo siguiente:
                *media
                *mediana
                *desviacion
                *frecuencias

c) Calcular el dinero recaudado por producto
"""
ventas = ["A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades", "P009-25Unidades", "B005-20Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-11Unidades","A001-91unidades"]


index1= ['A001','A011','A032','A125','B001','B005','P009','P019','R001','W307','Z052','Z025','Z278']
data1=np.array([31000, 25000, 43000, 55000, 10000, 20000, 30000, 49000, 60000, 90000, 35000, 27000, 65000])

seriePrecioProductos=pd.Series(data=data1, index=index1)

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

serieVentasProductos=pd.Series(data=unidades, index=index1)


print(serieVentasProductos)

media=serieVentasProductos.mean()
mediana=serieVentasProductos.median()
desviacion=serieVentasProductos.std()

print(media, mediana, desviacion)

#Dinero recaudado por producto
dinero=data1*serieVentasProductos.values

serieDinero= pd.Series(data=dinero, index=index1)

print(serieDinero)
