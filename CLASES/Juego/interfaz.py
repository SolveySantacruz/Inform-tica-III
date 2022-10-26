"""
Aquí se encuentra la parte visual del juego triqui.
Este módulo contiene 2 funciones.
explicarJuego: retornar mensaje explicativo.
imprimirTablero: retornar string con el tablero.

"""

def explicarJuego():
    explicacion=""" 
    --------------------------------------------------------------------
    Bienvenido, esto es triki.
    
    Para ganar, debe completar una línea recta, compuesta por un mismo 
    caracter ('X' o 'O')

    Línea recta=> horizontal, vertical, diagonal.

    Además debe ingresar la posición 0-8, para ingresar la posición durante 
    su turno.

    Tablero de posiciones

    0 | 1 | 2
    ----------
    3 | 4 | 5
    ----------
    6 | 7 | 8


    ---------------------------------------------------------------------
    """
    print(explicacion) 

def imprimirTablero(tableroLogico:list):
    tableroVisual= """ 
                        {} | {} | {}
                        ----------
                        {} | {} | {}
                        ----------
                        {} | {} | {}""".format(tableroLogico[0],tableroLogico[1],
                        tableroLogico[2],tableroLogico[3],tableroLogico[4],tableroLogico[5],tableroLogico[6],
                        tableroLogico[7],tableroLogico[8]).replace('None',' ')
    print(tableroVisual)




