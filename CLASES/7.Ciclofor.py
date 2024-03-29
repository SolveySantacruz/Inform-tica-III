# 09 de septiembre

# Ciclo FOR

# Ejercicio: recorrer los siguientes iterables utilizando el ciclo for:

alturas=[10,20,50,80,1,50]
pesos= (70, 60, 55, 52, 45, 90)
mensaje='hola mundo'
secuencia= range(1,11,1)

for altura in alturas:
    print(altura, end= ' ')

for peso in pesos:
    print(peso, end=' ')

for letra in mensaje: 
    print(letra, end=' ')

for numero in secuencia: 
    print(numero,end=' ')

# Utilizar ciclo for para recorrer los anterioes
# iterables sin necesidad de definirlos en las
# variables anteriormente nombradas.

print('Recorrido de iterables')

for altura in [10,20,50,80,1,50]:
    print(altura, end= ' ')

for peso in (70, 60, 55, 52, 45, 90):
    print(peso, end=' ')

for letra in 'hola mundo': 
    print(letra, end=' ')

for numero in range(1,11,1):
    print(numero,end=' ')


# Ejercicio: utilizando el ciclo for, generar las
# siguientes secuencias.

# 10, 11, 12, 13, 14, 15,...., 20

for i in range(10,21,1):
    print(i)

# 3, 6, 9, 12, 15, 18, 21, 24, 27,30

for i in range(3,31,3):
    print(i)
# 3, 6, 9, 12, 15, 18, 21, 24, 27,33,36,39,42,45

for i in (3,6, 9, 12, 15, 18, 21, 24, 27,33,36,39,42,45):
    print(i)
    
# Números pares del 200 al 400

for i in range(200, 401, 2):
    print(i)

# Las primeras 20 potencias de 2

for i in range(1,21):
     print(2**i, end = " ")


# Múltiplos de 5 del 10 a 50

n = 7
factores = range(2, n)
bandera = True

for factor in factores:
        if (n%factor)==0:
            print(n, "No es primo", end='\n\n')
            bandera = False
            break

if bandera == True:
    print(n, "Si es primo", end='\n\n')
