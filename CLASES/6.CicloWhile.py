# Ciclo While

# Crear un ciclo infinito

#while True:
#    print('Ciclo ejecutado')

# Crear un ciclo infinito pero protejerlo en caso de
# que se ejecute más de 100 veces.

contador=0
while True:
    print('Ciclo ejecutado {}'.format(contador))
    contador=contador+1

    if contador>100:
        print('Contador superado')
        break 

# Imprima los números del 20 al 50, utilizando el 
# ciclo While

cont=20
while True:
    print(cont)
    cont+=1
    print(cont)
    if cont>=50:
        break

# Mostrar en pantalla los primeros 10 números de la
# serie de Fibonacci.


cont=1
serie=0
num1=1
num2=1
while cont<9:
    suma=num1+num2
    print(suma)
    serie=suma+serie
    num1=suma
    num2=serie
    cont+=1
    print(serie)

# Realice un programa que solicite una
# contraseña 

cusuario=input('Ingrese una contraseña: ')
coriginal='1234'

while coriginal!=cusuario:
    print('Contraseña incorrecta')
    cusuario=input('Ingrese una contraseña: ')

print('Contraseña correcta')