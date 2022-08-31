
### Operadores de asignación 

a=1
b=2
c=3

### Operadores aritméticos

print('Suma  ', 1+2+3)
print('Mult y suma  ', 1*2+3)
print('División entera  ', 5//3)
print('División entera', 0//3)
print('Residuo  ', 5%2)
print('Residuo  ', 13%9)
print('Potencia  ', 9**2)
print('Raíz  ', 9**0.5)
print('Mult y potencia', 2*4**2)
print('Potencia y mult', 2**4*2) 

# Orden de operaciones: potencia, multiplicación-división, suma-resta 

print('concatenación -->  ','hola'+ 'mundo')
print('Replicación -->','a'*10)

print('concatenación -->  ',[1]+ [1,2,3])
print('Replicación -->',[0]*10)

### Operadores lógicos

print('and -->  ', True and False ) # Solo es verdadero si
print('and -->  ', False and True)
print('or -->  ', True or False) # Solo es falso si ambos
print('or -->  ', False or True)

print(1 and 2)
print(1 and 0)
print(19 and 20)
print(0 and 1)
print(100 or 0)
print(-2 or 20)
print('Solvey' and 'Santacruz')

### Para pensar: ejercicio
# Desarrolle un algoritmo que imprima si un número es mayor que 18
# sin utilizar el condicional if, utilizar operadores lógicos

#a=input()
#print('Verdadero  ', a )

### Operadores de comparación

print('Mayor --> ', 1>2)
print('Menor --> ', 19<0)
print('Menor o igual --> ', -1000<=-1000)
print('Igual --> ', 3==-5)
print('Mayor o igual --> ', 19>=20)
print('Diferente --> ', 30!=31)

print('Solvey'>'Santacruz')
print(True>False)
print([20,2]>[20,1]) #Compara elemento a elemento para ver cual es mayor

### Operadores de pertenencia

#Sirve para evaluar si un elemento está contenido en otro

print(" 'a' in 'holamundo' --> ", 'a' in 'holamundo')
print(" 'A' in 'holamundo' --> ",'A' in 'holamundo')
print("'hola' in 'holamundo' --> ", 'hola' in 'holamundo')
print(" ' ' in 'hola mundo' --> ", ' ' in 'hola mundo')

print('1 in [1,2,3] --> ', 1 in [1,2,3])
print("1 in ['1','2','3'] --> ",1 in ['1','2','3'])
print("'3' not in '124567' --> "'3' not in '124567')
print("'01' in '0 1 2 3 4' -->", '01' in '0 1 2 3 4')

