"""
Aqui se controla el juego triqui.

"""
from interfaz import explicarJuego, imprimirTablero
from logicaJuego import generarTableroLogico, insertarCaracterEnTablero, determinarGanador


print(explicarJuego())

tableroLogico=generarTableroLogico()
caracter=input('Ingrese el caracter con el que desea jugar: ')
posicion=int(input('Ingrese la posición para su caracter: '))
cont1=0

ganador=None

while ganador==None:

    actulizacion=insertarCaracterEnTablero(tableroLogico,posicion,caracter,cont1)
    acttablero= imprimirTablero(tableroLogico)
    ganador=determinarGanador(tableroLogico)
    posicion=int(input('Ingrese la posición para su caracter: '))
    cont1=cont1+1

print('El ganador es: ',ganador)




