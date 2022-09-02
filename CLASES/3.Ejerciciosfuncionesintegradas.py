# 02 de septiembre 2022

# Funciones integradas de Python

### Funciones de entrada y salida

# Solicitar una clave y luego responder en pantalla si es correcta o no.
#   Clave: "Unal2022"

clave_real="Unal2022"
clave_usuario=input('Ingrese su clave: ')

print((clave_usuario==clave_real) and 'La clave es correcta' or 'La clave es incorrecta')

# Solicitar un número y luego responder en pantalla si es mayor a 18.

numero=float(input('Ingrese un número: '))

print((numero>18) and 'El número es mayor que 18' or 'El número es menor que 18')


### Formateo de valores numéricos

# format(valor,tipo)

num=10398757665

formato_cientifico=format(num,'e')
formato_flotante=format(num,'.2e')

print(formato_cientifico)
print(formato_flotante)

# Exprese el número 0.000 000 029 213 en formato científico con 3 decimales

num= 0.000000029213

print(format(num,'.3e'))

## Formato flotante

num=12.1392
print(format(num,'.2f'))

num1=0.045
num2=12.1392

# Formatear num1 a flotante con un decimal

print(format(num1,'.1f'))

# Formatear num2 a entero 

# print(format(num2,'int'))


### Ayuda (help, dir, type)

# Determine el tipo de datos de los siguientes mostrados

# {'1','2'}
# {1:2}.itema()
# range(1,10)
# '1'
# (1,)

print(type({'1','2'}))
# print(type({1:2}.itema()))
print(type(range(1,10)))
print(type('1'))
print(type((1,)))

# ¿Qué funcionalidades tienen los tipos de datos: int, float, str, set?

entero=1 

print('---- funcionalidades enteros-----')
# for function in dir(entero):

print(dir(entero))

### Funciones de conversión  (bin,oct,)

print('Número 1 a bin, oct, hex -->', bin(1),oct(1),hex(1))
print('Número 8 a bin, oct, hex -->', bin(8),oct(8),hex(8))
print('Número 513 a bin, oct, hex -->', bin(513),oct(513),hex(513))

# Convertir a decimal los números: 0b1000   0o10   0x8

num1='0b1000'
num2='0o10'
num3='0x8'

print(int(num1,base=2))
print(int(num2,base=8))
print(int(num3,base=16))


### Funciones para secuencias 

# Secuencia: rango, lista, tupla,...

# Crear una secuencia con los números 1 al 10

secuencia1= [1,2,3,4,5,6,7,8,9,10]
secuencia2=(i for i in [1,2,3,4,5,6,7,8,9,10])
secuencia3= range(1,11,1) # El primer valor se toma, pero el segundo no
print(list(secuencia3))

# Crear la siguientes secuencias

# 2,4,6,8,10,12,...,50

print(list(range(2,51,2)))

# 0,3,6,9,12,15,18,...,200

print(list(range(0,201,3)))

# 10,9,8,7,...,0

print(list(range(10,-1,-1)))

# números múltiplos del 2 y 3 del 100 al 3

print(list(range(96,5,-6)))

# números múltiplos de 15 del 1000 al 900

print(list(range(990,899,-15)))

# len(), min(), max(), sum()
# Luego calcule el tamaño, máximo, mínimo y suma de los elementos de la última secuencia creada

secuencia=range(990,899,-15)

# Mapear la secuencia de la siguiente manera: 
    # Convertir los números a cadenas
    # Transformar los números al residuo entre 5
    # Multiplicar cada elemento por 3.1

def multiplicacion(elemento):
    return elemento*3.1

print(list(map(multiplicacion, secuencia)))

# Filtrar la anterior secuencia:
    # Retener solo los números pares

def esPar(elemento):    #Debe devolver True o False
    return elemento%2 == 0

print(list(filter(esPar,secuencia)))
    # Retener solo los números que al sumarles 5 sean pares
    # Retener solo los números cuyo primer dígito sea par 


