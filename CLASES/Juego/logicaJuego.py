"""
Este módulo contiene 3 funciones:

- generarTableroLogico => No recibe nada
                        retorna una lista Nones
- insertarCaracterEnTablero => recibe lista, posición, caracter
                                retorna una lista actualizada
- determinarGanador => recibe una lista(tablero)
                        retorna ganador

"""

def generarTableroLogico():
    tableroLogico=[None,None,None,None,None,None,None,None,None]
    return tableroLogico

def insertarCaracterEnTablero(tableroLogico:list,posicion:int,caracter:str,cont1:int):
    tableroLogico[posicion]=caracter
    contrario=range(0,9,1)
    caracterContrario=None

    if caracter=='x':
        caracterContrario='o'
    elif caracter=='o':
        caracterContrario='x'
    
    posicionContraria=None
    while posicionContraria==None:
        for i in contrario:
            posicionContraria=contrario[i+cont1]
            if posicionContraria!=posicion and tableroLogico[posicionContraria]==None:
                tableroLogico[posicionContraria]=caracterContrario
                break
        
    
    return tableroLogico 

def determinarGanador(tableroLogico:list):
    posicionesAComparar=[(0,1,2),
                         (3,4,5),
                         (6,7,8),
                         (0,3,6),
                         (1,4,7),
                         (2,5,8),
                         (0,4,8),
                         (2,4,6)]
    ganador=None
    for pos1, pos2, pos3 in posicionesAComparar:
        if tableroLogico[pos1]==tableroLogico[pos2]==tableroLogico[pos3] and (tableroLogico[pos1]!=None):
            ganador=tableroLogico[pos1]
            break
    return ganador






