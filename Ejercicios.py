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
