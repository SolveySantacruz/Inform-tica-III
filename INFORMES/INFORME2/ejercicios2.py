
nombre_completo = " Solvey Isleny Santacruz Zambrano"   #Por favor ingrese su nombre COMPLETO en la cadena

# ----------------------------Ejercicios INFORME 2--------------------------------

#-------EJERCICIO 1---------

productos={'A032':43000,'B001':10000,'A125':55000,'P009':30000,'B005':20000,'W307':90000,'A011':25000,'P019':49000,'R001':60000,'A001':31000,'Z052':35000,'Z025':27000,'Z278':65000}
ventas = ["A032-52Unidades", "B001-29Unidades", "A125-15Unidades", "A032-22Unidades", "P009-25Unidades", "B005-20Unidades", "B001-19Unidades", "P009-31Unidades", "B005-22Unidades", "W307-15Unidades", "A011-31Unidades", "P019-18Unidades", "A011-20Unidades", "R001-20Unidades", "P019-19Unidades", "A001-12Unidades", "A125-20Unidades", "R001-31Unidades", "Z052-52Unidades", "W307-31Unidades", "Z025-42Unidades", "Z052-10Unidades", "Z278-30Unidades", "Z025-24Unidades", "Z278-21Unidades", "A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades","B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-11Unidades","A001-91unidades"]

# a) Unidades vendidas de cada producto, almacene la respuesta en un diccionario llamado  unidadesPorProducto, 
# cuyas claves sean los productos, y cuyos valores sean el numero de unidades vendidas por producto.

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


# b) Dinero recaudado por cada producto, almacene la respuesta en un diccionario  llamado ventasPorProducto, 
# cuyas claves sean los productos, y cuyos valores sean el dinero recaudado por producto.

ventasPorProducto=[]
dinero=[]
unidades_p=[]
precios=[]
claves=[]

for valor1 in unidadesPorProducto.values():
    unidades_p.append(int(valor1))

for valor2 in productos.values():
    precios.append(int(valor2))

for clave in productos.keys():
    claves.append(clave)

for i in range(0,len(precios),1):
     dinero.append(precios[i]*unidades_p[i])

ventasPorProducto=dict(zip(claves,dinero))


# c) Dinero total recaudado, almacene la respuesta en una variable llamada  ventasTotal, 
# con el dinero total recaudado

ventasTotal=sum(dinero)

reporteVentas = [unidadesPorProducto, ventasPorProducto, ventasTotal]

#-------EJERCICIO 2---------

calificaciones={"001": {"Nombre": "Cristian Pachon",      "Fisica":  2.0,   "Ingles": 2.2,   "Deportes": 4.2,   "Artes": 4.0,  "Musica": 0.5},
                "002": {"Nombre": "Daniela Pineda",       "Fisica":  2.2,   "Ingles": 1.0,   "Deportes": 4.0,   "Artes": 3.1,  "Musica": 4.0},
                "003": {"Nombre": "Esteban Murcia",       "Fisica":  2.9,   "Ingles": 4.2,   "Deportes": 3.1,   "Artes": 0.0,  "Musica": 3.1},
                "004": {"Nombre": "Jose Guzman",          "Fisica":  2.0,   "Ingles": 4.0,   "Deportes": 4.0,   "Artes": 0.2,  "Musica": 0.0},
                "005": {"Nombre": "Camilo Rodriguez",     "Fisica":  2.2,   "Ingles": 0.2,   "Deportes": 0.2,   "Artes": 1.0,  "Musica": 0.2},
                "006": {"Nombre": "Mariana Londoño",      "Fisica":  2.0,   "Ingles": 5.0,   "Deportes": 1.0,   "Artes": 1.3,  "Musica": 1.0},
                "007": {"Nombre": "Estefania Muños",      "Fisica":  5.0,   "Ingles": 1.2,   "Deportes": 1.2,   "Artes": 1.9,  "Musica": 1.3},
                "008": {"Nombre": "Cristian Rodriguez",   "Fisica":  0.2,   "Ingles": 2.9,   "Deportes": 1.0,   "Artes": 4.2,  "Musica": 1.9},
                "009": {"Nombre": "Natalia Alzate",       "Fisica":  5.0,   "Ingles": 2.3,   "Deportes": 2.9,   "Artes": 2.9,  "Musica": 0.2},
                "010": {"Nombre": "Juan Sanabria",        "Fisica":  4.2,   "Ingles": 5.0,   "Deportes": 4.2,   "Artes": 4.2,  "Musica": 3.9},
                "011": {"Nombre": "Juanita Calderon",     "Fisica":  4.5,   "Ingles": 4.2,   "Deportes": 4.0,   "Artes": 0.5,  "Musica": 4.2},
                "012": {"Nombre": "Laura Quintero",       "Fisica":  4.2,   "Ingles": 4.5,   "Deportes": 4.2,   "Artes": 0.0,  "Musica": 0.5},
                "013": {"Nombre": "Viviana Quesada",      "Fisica":  0.5,   "Ingles": 0.5,   "Deportes": 2.3,   "Artes": 4.2,  "Musica": 0.0},
                "014": {"Nombre": "Camila Alzate",        "Fisica":  4.1,   "Ingles": 3.1,   "Deportes": 2.5,   "Artes": 4.3,  "Musica": 3.2},
                "015": {"Nombre": "Leonidas Sanabria",    "Fisica":  4.2,   "Ingles": 4.2,   "Deportes": 4.2,   "Artes": 2.5,  "Musica": 4.3},
                "016": {"Nombre": "Juana Diaz",           "Fisica":  4.1,   "Ingles": 0.0,   "Deportes": 4.5,   "Artes": 4.2,  "Musica": 2.5},
                "017": {"Nombre": "Laura Playonero",      "Fisica":  1.2,   "Ingles": 3.1,   "Deportes": 0.5,   "Artes": 4.5,  "Musica": 3.2},
                "018": {"Nombre": "Viviana Restrepo",     "Fisica":  0.5,   "Ingles": 0.2,   "Deportes": 4.1,   "Artes": 4.1,  "Musica": 4.5},
                "019": {"Nombre": "Elias Rodriguez",      "Fisica":  2.2,   "Ingles": 0.5,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 4.1},
                "020": {"Nombre": "Mariana Pacheco",      "Fisica":  2.0,   "Ingles": 2.2,   "Deportes": 4.0,   "Artes": 4.2,  "Musica": 0.5},
                "021": {"Nombre": "Estefany Muñoz",       "Fisica":  2.2,   "Ingles": 1.0,   "Deportes": 3.1,   "Artes": 4.0,  "Musica": 4.0},
                "022": {"Nombre": "Cristian Fernandez",   "Fisica":  2.9,   "Ingles": 4.2,   "Deportes": 0.0,   "Artes": 3.1,  "Musica": 3.1},
                "023": {"Nombre": "Jessika Arias",        "Fisica":  2.0,   "Ingles": 4.0,   "Deportes": 4.0,   "Artes": 0.0,  "Musica": 0.2},
                "024": {"Nombre": "Juan Mendoza",         "Fisica":  4.5,   "Ingles": 4.2,   "Deportes": 4.0,   "Artes": 4.2,  "Musica": 0.5},
                "025": {"Nombre": "Maria Calderon",       "Fisica":  2.2,   "Ingles": 0.2,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 1.0},
                "026": {"Nombre": "Laura Lozada",         "Fisica":  2.0,   "Ingles": 5.0,   "Deportes": 1.0,   "Artes": 1.0,  "Musica": 1.3},
                "027": {"Nombre": "Yessica Quesada",      "Fisica":  1.2,   "Ingles": 5.0,   "Deportes": 1.9,   "Artes": 1.2,  "Musica": 1.3},
                "028": {"Nombre": "Jennifer Alzate",      "Fisica":  2.9,   "Ingles": 0.2,   "Deportes": 4.2,   "Artes": 1.0,  "Musica": 1.9},
                "029": {"Nombre": "Karen Sanabria",       "Fisica":  0.0,   "Ingles": 4.1,   "Deportes": 4.2,   "Artes": 4.5,  "Musica": 2.5},
                "030": {"Nombre": "Fernando Rodriguez",   "Fisica":  0.5,   "Ingles": 2.2,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 4.1},
                "031": {"Nombre": "Nina Londoño",         "Fisica":  4.2,   "Ingles": 4.2,   "Deportes": 2.5,   "Artes": 4.2,  "Musica": 4.3},
                "032": {"Nombre": "Favio Munera",         "Fisica":  5.0,   "Ingles": 2.3,   "Deportes": 2.9,   "Artes": 2.9,  "Musica": 0.2},
                "033": {"Nombre": "Lindsey Roy",          "Fisica":  4.2,   "Ingles": 5.0,   "Deportes": 4.2,   "Artes": 4.2,  "Musica": 3.9},
                "034": {"Nombre": "Nathalia Hernandez",   "Fisica":  4.2,   "Ingles": 4.5,   "Deportes": 0.0,   "Artes": 4.2,  "Musica": 0.5},
                "035": {"Nombre": "Juan Gaviria",         "Fisica":  0.5,   "Ingles": 0.5,   "Deportes": 4.2,   "Artes": 2.3,  "Musica": 0.0},
                "036": {"Nombre": "Fabio Urrego",         "Fisica":  4.1,   "Ingles": 3.1,   "Deportes": 4.3,   "Artes": 2.5,  "Musica": 3.2},
                "037": {"Nombre": "Fernanda Quintero",    "Fisica":  0.5,   "Ingles": 0.2,   "Deportes": 4.1,   "Artes": 4.1,  "Musica": 4.5},
                "038": {"Nombre": "Camila Queiroz",       "Fisica":  1.2,   "Ingles": 3.1,   "Deportes": 4.5,   "Artes": 0.5,  "Musica": 3.2},
                "039": {"Nombre": "Ursula Alzate",        "Fisica":  2.2,   "Ingles": 4.0,   "Deportes": 4.2,   "Artes": 0.5,  "Musica": 2.0},
                "040": {"Nombre": "Aureliano Buendia",    "Fisica":  1.0,   "Ingles": 3.1,   "Deportes": 4.0,   "Artes": 4.0,  "Musica": 2.2}}


  # a) El promedio obtenido por cada estudiante, almacene la respuesta en un diccionario 
  # llamado promediosPorEstudiante, cuyas claves son los nombres de los estudiantes y 
  # los valores sus respectivos promedios (flotantes de 2 decimales)
d_001=[]
dd_001=[]
prom=[]
promedios=[]
promediosPorEstudiante=[]
claves1=[]

for j in calificaciones.keys():
    for i in calificaciones[j].values():
        d_001.append(i)
        if type(i)==float:
            dd_001.append(i)   
        elif type(i)==str:
            claves1.append(i)

for i in range(0,len(dd_001),5):
    prom=round((sum(dd_001[i:i+5])/5),2)

    promedios.append(prom)

promediosPorEstudiante=dict(zip(claves1,promedios))


  #b) El promedio obtenido por cada materia, almacene la respuesta en un diccionario llamado 
  # promediosPorMateria, cuyas claves son los nombres de las materias y los valores sus respectivos promedios

fisica=[]
ingles=[]
deportes=[]
artes=[]
musica=[]
prom_m=[]

for j in calificaciones:
    fisica.append(calificaciones[j]['Fisica'])
    ingles.append(calificaciones[j]['Ingles'])
    deportes.append(calificaciones[j]['Deportes'])
    artes.append(calificaciones[j]['Artes'])
    artes.append(calificaciones[j]['Artes'])
    musica.append(calificaciones[j]['Musica'])
    

prom_fisica=round((sum(fisica)/len(fisica)),2)
prom_m.append(prom_fisica)
prom_ingles=round((sum(ingles)/len(ingles)),2)
prom_m.append(prom_ingles)
prom_deportes=round((sum(deportes)/len(deportes)),2)
prom_m.append(prom_deportes)
prom_artes=round((sum(artes)/len(artes)),2)
prom_m.append(prom_artes)
prom_musica=round((sum(musica)/len(musica)),2)
prom_m.append(prom_musica)

materias=['Fisica','Ingles','Deportes','Artes','Musica']
promediosPorMateria=dict(zip(materias,prom_m))

  # c) Estudiantes con promedio mayor o igual a 3, almacene la respuesta en una lista llamada 
  # estudiantesAprobados, que contenga los nombres de los estudiantes que aprueban

estudiantesAprobados=[]

for i in promediosPorEstudiante:
    if promediosPorEstudiante[i]>=3:
        estudiantesAprobados.append(i)

  # d) Estudiantes con promedio menor a 3, almacene la respuesta en una lista llamada estudiantesReprobados, 
  # que contenga los nombres de los estudiantes que reprueban

estudiantesReprobados=[]

for i in promediosPorEstudiante:
    if promediosPorEstudiante[i]<3:
        estudiantesReprobados.append(i)

reporteEstudiantes = [promediosPorEstudiante, promediosPorMateria, estudiantesAprobados, estudiantesReprobados]


#-------EJERCICIO 3---------

cine=[("2D_3NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("3D_0NIÑOS_LUNES", "3D_1ADULTOS_LUNES"),("2D_2NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("3D_0NIÑOS_LUNES", "3D_3ADULTOS_LUNES"),("3D_3NIÑOS_LUNES", "3D_4ADULTOS_LUNES"),("2D_2NIÑOS_LUNES", "2D_4ADULTOS_LUNES"),("2D_1NIÑOS_MARTES",
    "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),
   ("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),(
       "2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),
   ("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"), ("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),(
       "2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
   ("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES",
    "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
   ("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),(
       "2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),
   ("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),(
       "2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
   ("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),(
       "2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
   ("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES",
    "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
   ("2D_2NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES",
    "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
   ("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),(
       "3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("3D_1NIÑOS_SABADO", "3D_1ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),
   ("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),(
       "2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),
   ("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO",
    "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_DOMINGO", "2D_0ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"), ("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO",
    "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),
   ("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO",
    "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),
   ("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO",
    "2D_4ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_9ADULTOS_DOMINGO")]

# 2D Y 3D NIÑOS LUNES
sum_2D_NS=[]
sum_3D_NS=[]

sumas=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:9]=='NIÑOS' and personas[10:15]=='LUNES':
            sum_2D_NS.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:9]=='NIÑOS' and personas[10:15]=='LUNES':
            sum_3D_NS.append(int(personas[3]))
    suma1=(sum(sum_2D_NS))
    suma1D=(sum(sum_3D_NS))

    
sumas.append(suma1)  
sumas.append(suma1D)      

# 2D Y 3D NIÑOS MARTES
sum_2D_NM=[]
sum_3D_NM=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:9]=='NIÑOS' and personas[10:16]=='MARTES':
            sum_2D_NM.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:9]=='NIÑOS' and personas[10:16]=='MARTES':
            sum_3D_NM.append(int(personas[3]))
    suma2=(sum(sum_2D_NM))
    suma2D=(sum(sum_3D_NM))

    
sumas.append(suma2)   
sumas.append(suma2D)        

# 2D Y 3D NIÑOS MIERCOLES
sum_2D_NMI=[]
sum_3D_NMI=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:9]=='NIÑOS' and personas[10:19]=='MIERCOLES':
            sum_2D_NMI.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:9]=='NIÑOS' and personas[10:19]=='MIERCOLES':
            sum_3D_NMI.append(int(personas[3]))
    suma3=(sum(sum_2D_NMI))
    suma3D=(sum(sum_3D_NMI))

    
sumas.append(suma3)  
sumas.append(suma3D)  

# 2D Y 3D NIÑOS JUEVES
sum_2D_NJ=[]
sum_3D_NJ=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:9]=='NIÑOS' and personas[10:16]=='JUEVES':
            sum_2D_NJ.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:9]=='NIÑOS' and personas[10:16]=='JUEVES':
            sum_3D_NJ.append(int(personas[3]))
    suma4=(sum(sum_2D_NJ))
    suma4D=(sum(sum_3D_NJ))
    
sumas.append(suma4)  
sumas.append(suma4D)  

# 2D Y 3D NIÑOS VIERNES
sum_2D_NV=[]
sum_3D_NV=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:9]=='NIÑOS' and personas[10:17]=='VIERNES':
            sum_2D_NV.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:9]=='NIÑOS' and personas[10:17]=='VIERNES':
            sum_3D_NV.append(int(personas[3]))
    suma5=(sum(sum_2D_NV))
    suma5D=(sum(sum_3D_NV))
    
sumas.append(suma5)  
sumas.append(suma5D) 

# 2D Y 3D NIÑOS SABADO
sum_2D_NSS=[]
sum_3D_NSS=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:9]=='NIÑOS' and personas[10:16]=='SABADO':
            sum_2D_NSS.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:9]=='NIÑOS' and personas[10:16]=='SABADO':
            sum_3D_NSS.append(int(personas[3]))
    suma6=(sum(sum_2D_NSS))
    suma6D=(sum(sum_3D_NSS))
    
sumas.append(suma6)  
sumas.append(suma6D) 

# 2D Y 3D NIÑOS DOMINGO
sum_2D_ND=[]
sum_3D_ND=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:9]=='NIÑOS' and personas[10:17]=='DOMINGO':
            sum_2D_ND.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:9]=='NIÑOS' and personas[10:17]=='DOMINGO':
            sum_3D_ND.append(int(personas[3]))
    suma7=(sum(sum_2D_ND))
    suma7D=(sum(sum_3D_ND))
    
sumas.append(suma7)  
sumas.append(suma7D) 


# 2D Y 3D ADULTOS LUNES
sum_2D_AS=[]
sum_3D_AS=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:11]=='ADULTOS' and personas[12:17]=='LUNES':
            sum_2D_AS.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:11]=='ADULTOS' and personas[12:17]=='LUNES':
            sum_3D_AS.append(int(personas[3]))
    suma1A=(sum(sum_2D_AS))
    suma1AD=(sum(sum_3D_AS))

sumas.append(suma1A)  
sumas.append(suma1AD) 


# 2D Y 3D ADULTOS MARTES
sum_2D_AM=[]
sum_3D_AM=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:11]=='ADULTOS' and personas[12:18]=='MARTES':
            sum_2D_AM.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:11]=='ADULTOS' and personas[12:18]=='MARTES':
            sum_3D_AM.append(int(personas[3]))
    suma2A=(sum(sum_2D_AM))
    suma2AD=(sum(sum_3D_AM))

sumas.append(suma2A)  
sumas.append(suma2AD) 

# 2D Y 3D ADULTOS MIERCOLES
sum_2D_AMI=[]
sum_3D_AMI=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:11]=='ADULTOS' and personas[12:21]=='MIERCOLES':
            sum_2D_AMI.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:11]=='ADULTOS' and personas[12:21]=='MIERCOLES':
            sum_3D_AMI.append(int(personas[3]))
    suma3A=(sum(sum_2D_AMI))
    suma3AD=(sum(sum_3D_AMI))

sumas.append(suma3A)  
sumas.append(suma3AD) 

# 2D Y 3D ADULTOS JUEVES
sum_2D_AJ=[]
sum_3D_AJ=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:11]=='ADULTOS' and personas[12:18]=='JUEVES':
            sum_2D_AJ.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:11]=='ADULTOS' and personas[12:18]=='JUEVES':
            sum_3D_AJ.append(int(personas[3]))
    suma4A=(sum(sum_2D_AJ))
    suma4AD=(sum(sum_3D_AJ))

sumas.append(suma4A)  
sumas.append(suma4AD) 

# 2D Y 3D ADULTOS VIERNES
sum_2D_AV=[]
sum_3D_AV=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:11]=='ADULTOS' and personas[12:19]=='VIERNES':
            sum_2D_AV.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:11]=='ADULTOS' and personas[12:19]=='VIERNES':
            sum_3D_AV.append(int(personas[3]))
    suma5A=(sum(sum_2D_AV))
    suma5AD=(sum(sum_3D_AV))

sumas.append(suma5A)  
sumas.append(suma5AD)

# 2D Y 3D ADULTOS SABADO
sum_2D_ASS=[]
sum_3D_ASS=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:11]=='ADULTOS' and personas[12:18]=='SABADO':
            sum_2D_ASS.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:11]=='ADULTOS' and personas[12:18]=='SABADO':
            sum_3D_ASS.append(int(personas[3]))
    suma6A=(sum(sum_2D_ASS))
    suma6AD=(sum(sum_3D_ASS))

sumas.append(suma6A)  
sumas.append(suma6AD)


# 2D Y 3D ADULTOS DOMINGO
sum_2D_AD=[]
sum_3D_AD=[]

for unidades in cine:
    for personas in unidades:
        if personas[0:2]=='2D' and personas[4:11]=='ADULTOS' and personas[12:19]=='DOMINGO':
            sum_2D_AD.append(int(personas[3]))
        elif personas[0:2]=='3D' and personas[4:11]=='ADULTOS' and personas[12:19]=='DOMINGO':
            sum_3D_AD.append(int(personas[3]))
    suma7A=(sum(sum_2D_AD))
    suma7AD=(sum(sum_3D_AD))

sumas.append(suma7A)  
sumas.append(suma7AD)

boletasVendidas=sum(sumas)

# Dinero recaudado por el cine
dincine=[]
sem={'semana':{'2D':{'nino':5000,'adulto':8000},'3D':{'nino':8000,'adulto':12000}}}
finde={'finde':{'2D':{'nino':7000,'adulto':9000},'3D':{'nino':9000,'adulto':15000}}}

#Niños 2D Y 3D

#lunes 
dincine.append(suma1*sem['semana']['2D']['nino'])
dincine.append(suma1D*sem['semana']['3D']['nino'])
#Martes
dincine.append(suma2*sem['semana']['2D']['nino'])
dincine.append(suma2D*sem['semana']['3D']['nino'])
#Miercoles
dincine.append(suma3*sem['semana']['2D']['nino'])
dincine.append(suma3D*sem['semana']['3D']['nino'])
#Jueves
dincine.append(suma4*sem['semana']['2D']['nino'])
dincine.append(suma4D*sem['semana']['3D']['nino'])
#Viernes
dincine.append(suma5*sem['semana']['2D']['nino'])
dincine.append(suma5D*sem['semana']['3D']['nino'])
#Sabado
dincine.append(suma6*finde['finde']['2D']['nino'])
dincine.append(suma6D*finde['finde']['3D']['nino'])
#Domingo
dincine.append(suma7*finde['finde']['2D']['nino'])
dincine.append(suma7D*finde['finde']['3D']['nino'])

#Adultos 2D Y 3D
#lunes 
dincine.append(suma1A*sem['semana']['2D']['adulto'])
dincine.append(suma1AD*sem['semana']['3D']['adulto'])
#Martes
dincine.append(suma2A*sem['semana']['2D']['adulto'])
dincine.append(suma2AD*sem['semana']['3D']['adulto'])
#Miercoles
dincine.append(suma3A*sem['semana']['2D']['adulto'])
dincine.append(suma3AD*sem['semana']['3D']['adulto'])
#Jueves
dincine.append(suma4A*sem['semana']['2D']['adulto'])
dincine.append(suma4AD*sem['semana']['3D']['adulto'])
#Viernes
dincine.append(suma5A*sem['semana']['2D']['adulto'])
dincine.append(suma5AD*sem['semana']['3D']['adulto'])
#Sabado
dincine.append(suma6A*finde['finde']['2D']['adulto'])
dincine.append(suma6AD*finde['finde']['3D']['adulto'])
#Domingo
dincine.append(suma7A*finde['finde']['2D']['adulto'])
dincine.append(suma7AD*finde['finde']['3D']['adulto'])

dineroRecaudado=sum(dincine)
reporteCine = [boletasVendidas, dineroRecaudado]

print(reporteCine)

#-------EJERCICIO 4---------

def obtenerMultiplos(numero):
    mul=range(numero,(numero*11),1)
    multiplos=[]
    for i in mul:
        if i%numero==0:
            multiplos.append(i)
    return multiplos


def obtenerDivisores(numero):
    div=range(1,numero+1,1)
    divisores=[]
    for i in div:
        if numero%i==0 and i!=1 and i!=numero:
            divisores.append(i)
    return divisores

def obtenerNesimoFibonacci(numero):
    num1=0
    num2=1
    nesimo=[]
    nesimo.append(num1)
    nesimo.append(num2)

    for i in range(numero):
        total = num1 + num2
        num1=num2
        num2= total
        nesimo.append(total)
    
    n_nesimo=nesimo[numero-1]
        
    return n_nesimo

funciones = [obtenerMultiplos, obtenerDivisores, obtenerNesimoFibonacci]
print(funciones)

#-------EJERCICIO 5---------

def calcularSalario(nombre,ventas):
    base= 1200000+1200000*0.1+1200000*0.05
    comision=[50000*0.05,70000*0.04,40000*0.06,25000*0.07,35000*0.05,80000*0.03,95000*0.02]
    total=[]
    sal={}
    for i in range(0,len(ventas),1):
        salario=(ventas[i]*comision[i])
        total.append(salario)
    fintotal=sum(total)+base
    sal['nombre']=nombre
    sal['salario']=fintotal

    return sal

funcion=calcularSalario
print(funcion)
