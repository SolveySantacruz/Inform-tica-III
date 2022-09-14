#------EJERCICIOS 1------

### EJERCICIOS OPERADORES

# EJERCICIO 1 

# Dada una cantidad de segundos, realice un algoritmo que los convierta a unidades horas,minutos
# mostrando en pantalla en formato "horas:minutos"  

a=3660  #segundos
print(a//3600,':',(a%3600)/60)


# EJERCICIO 2 

# ¿Qué radio debe tener una esfera, para que su volumen sea el mismo al de un cubo de lado 5 cm?

Vol_cubo= 5*5*5
radio= ((Vol_cubo)*(3/4)*(3.14))**(1/3)
print('radio esfera en cm = ',radio)

# EJERCICIO 3 

# ¿Cuantas veces supera, el area de un cubo, al area de una esfera, si el lado del
# cubo es 10 cm. Y el radio de la esfera 2 cm? 

Acubo= 10**2
Aesfer= (4)*(3.14)*(2)**2

print('El área de un cubo supera al de una esfera en ', Acubo/Aesfer, 'veces')
print('El área de un cubo supera al de una esfera en ', Acubo//Aesfer, 'veces')

# EJERCICIO 4 

# Realice un código, que permita la conversión de millas a km y km a millas

millas= 0.621*2
kilometros= 2

mak= millas/0.621
kam=kilometros*0.621

print(millas,'millas','es igual a ',mak,'km')
print(kilometros,'km', 'es igual a ',kam,'millas')

# EJERCICIO 5 

# Dadas las coordenadas P1(5,4,5) y P2(0,10,9).
# Realice un codigo que determine la distancia entre ambos puntos

#  EJERCICIO 6 

# La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
# con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
# Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia.


notas=range(0,6,1)
nota1=4.0
nota2=3.5
nota3=4.0

for final in notas:
    promedio= nota1*0.15+nota2*0.25+nota3*0.2+final*0.4
    if promedio>=3:
      print('La nota final puede ser: ',final)
      print('El promedio sería: ',promedio)


# EJERCICIO 8 

# Cuatro compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
# El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. El servicio se
# prestará solo de ida.
# Sin embargo, los cuatro no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
# debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
# utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre los cuatro.
# A continuación veamos el uso del servicio por parte de los compañeros en la última semana de clases:

#             LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
# JUAN          Si        Si        No        Si    No
# CAMILA        Si        Si        No        No    No
# JOSE          Si        No        Si        No    No
# MARIA         Si        Si        Si        No    No  

# ¿Cuanto debe pagar cada estudiante?

JUAN=[1,1,0,1,0]
CAMILA=[1,1,0,0,0]
JOSE=[1,0,1,0,0]
MARIA=[1,1,1,0,0]

# De lunes a jueves 

cuota_personal=15000/4
cuota_juan=0
cuota_cam=0
cuota_jos=0
cuota_mar=0

for i in JUAN:
    if i==1:
        cuota_juan+=cuota_personal

for i in CAMILA:
    if i==1:
        cuota_cam+=cuota_personal

for i in JOSE:
    if i==1:
        cuota_jos+=cuota_personal

for i in MARIA:
    if i==1:
        cuota_mar+=cuota_personal

print('Juan debe pagar= ',cuota_juan+(10000/4))
print('Camila debe pagar= ',cuota_cam+(10000/4))
print('Jose debe pagar= ',cuota_jos+(10000/4))
print('Maria debe pagar= ',cuota_mar+(10000/4))


# ----- EJERCICIOS 3----

#====================== MÉTODOS DE STRINGS ====================

#==> EJERCICIO 1

# "A continuación se encuentra el poema el salmon"

# """
# TÍTULO: EL SALMÓN
# PÁRRAFO 1: DETRÁS DE UN SALMÓN, NADA UN TIBURÓN, LO CAZA EN ALASKA, CANSADOS LOS DOS. 
# PÁRRAFO 2: ASUSTADO GRITA: ¡NOOO! POR FAVOR,MI VIDA ES MUY CORTA, ¡MUESTRA COMPASIÓN!.
# PÁRRAFO 3: ABRIENDO SU BOCA, LO DEJA ESCAPAR, Y CORRIENTE ARRIBA, LO HA VISTO NADAR.
# """

string1='TÍTULO: EL SALMÓN'
string2='PÁRRAFO 1: DETRÁS DE UN SALMÓN, NADA UN TIBURÓN, LO CAZA EN ALASKA, CANSADOS LOS DOS.'
string3='PÁRRAFO 2: ASUSTADO GRITA: ¡NOOO! POR FAVOR,MI VIDA ES MUY CORTA, ¡MUESTRA COMPASIÓN!.'
string4='PÁRRAFO 3: ABRIENDO SU BOCA, LO DEJA ESCAPAR, Y CORRIENTE ARRIBA, LO HA VISTO NADAR.'

# a) Corrija el poema de tal manera que:

# Los indicadores de título y párrafo desaparezcan.

print(string1.removeprefix('TÍTULO:'))
print(string2.removeprefix('PÁRRAFO 1:'))
print(string3.removeprefix('PÁRRAFO 2:'))
print(string4.removeprefix('PÁRRAFO 3:'))

# Corregir el uso de mayúsculas y minúsculas según las reglas gramaticales.
#       El titulo esté en formato de título.

tit=string1.title()
print(tit.center(50))
print('\n')

# Separar los cuatro versos de cada párrafo en renglones sucesivos.
# Generar un espacio de renglon entre titulo-parrafo y párrafo-parrafo

cad1= string2.removeprefix('PÁRRAFO 1:')
cad2= string3.removeprefix('PÁRRAFO 2:')
cad3= string4.removeprefix('PÁRRAFO 3:')


print(cad1.replace(',','\n'))
print('\n')
print(cad2.replace(',','\n'))
print('\n')
print(cad3.replace(',','\n'))



#       El título debe estar centrado.   








#    b) Contar el número de veces que aparece cada vocal
#       contar el numero de lineas del poema.
#       Reemplazar las palabras: salmón ==> tiburón
#                                tiburón ==> salmón
#    c) Verificar si el contenido del poemas es: alfabetico
#                                                alfanumerico
#                                                decimal
#                                                digitos
#    d) Utilizar la indexación para extraer los elementos ubicados
#       en los índices: 0, 10, 100, último índices
#    e) Utilizar slicing para extraer los elementos ubicados en:
#       - Indices pares.
#       - Indices impares.
#       - Cada quinto elemento, empezando desde el 20
#       - Cada tercer elemento, pero empezando desde el indice 4 y terminando en el 62
#       - Desde la mitad hacia adelante
#       - Todos pero al revés
#       - Cada segundo elemento, pero al revés"""