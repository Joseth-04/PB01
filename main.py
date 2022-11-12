from Ahorcado import ahorcado
from Usuarios import menuJugadores

# Como leer un archivo de excel
import openpyxl
import getpass
from datetime import datetime


filesheet = "./Jugadores.xlsx"

# Leer el archivo
wb = openpyxl.load_workbook(filesheet)

# Fijar la hoja
hojaPlayers = wb.get_sheet_by_name('Players')

def volverMenuP():
    menuPrincipal()
    
def gato():
    
    #declarar matriz
    tablero = []
    fila=0
    columna=0

    #Valida cuanto jugadores existen
    for i in range(2, hojaPlayers.max_row+1):
        cantidadJugadores = i - 1

    if cantidadJugadores >= 2:
        #Lista de jugadores disponibles
        print("Jugadores Disponibles")
        for i in range(2, hojaPlayers.max_row +1):
            print("\n")

            for j in range(1, hojaPlayers.max_column -1):
                celda = hojaPlayers.cell(row=i, column =j)
                print("ID:",celda.value, end = " ")

        print("\n")

        #Seleccionar jugador
        selectUno = input("Por favor, ingrese solamente el ID del jugador X: ")
        print("")
        selectDos = input("Por favor, ingrese solamente el ID del jugador O: ")

        #buscar en la lista
        for cell in hojaPlayers["A"]:
            if cell.value == selectUno:
                jugadorUno = hojaPlayers[f"B{cell.row}"].value #Asignamos el nombre del usuario al jugador1

        for cell in hojaPlayers["A"]:
            if cell.value == selectDos:
                jugadorDos = hojaPlayers[f"B{cell.row}"].value #Asignamos el nombre del usuario al jugador2

        print("\n", "\n")
        print(jugadorUno," VS ", jugadorDos)
        print("\n", "\n")

    else:
        print("No puede jugar")
        quit()

    #rellenamos la matriz con datos
    for i in range(3):
        tablero.append([" "] * 3)

    def pintarTablero():
    #imprimimos el tablero con los limites
        print("\n")
        print(tablero[0][0], " | ", tablero[0][1], " | ", tablero[0][2],)
        print("-------------")
        print(tablero[1][0], " | ", tablero[1][1], " | ", tablero[1][2],)
        print("-------------")
        print(tablero[2][0], " | ", tablero[2][1], " | ", tablero[2][2],)

    print("\n")
    pintarTablero()
    print("\n")
    print("Turno de: ", jugadorUno)
    fila = int(input("Coloque la fila donde quiere colcar la X:")) - 1
    columna = int(input("Coloque la Columna donde quiere colcar la X:")) - 1
    tablero[fila][columna] = "X"
    pintarTablero()

    print("\n")
    print("Turno de: ", jugadorDos)
    print("\n")
    fila = int(input("Coloque la fila donde quiere colcar la O:")) - 1
    columna = int(input("Coloque la Columna donde quiere colcar la O:")) - 1
    tablero[fila][columna] = "O"
    pintarTablero()

def menuPrincipal():
    print ("\n1) Jugadores",
    "\n2) Juego Gato",
    "\n3) Juego Ahorcado",
    "\n4) Juego Mundialista",
    "\n5) Salir del juego\n")
    opcion = int(input("Ingrese la opcion a la que desea ingresar: "))
    if opcion == 1:
        #codigo agregar jugadores    
        menuJugadores()
    if opcion == 2:
        #codigo agregar jugadores    
        gato()
    if opcion == 3:
        #Código ahorcado
        ahorcado()
    if opcion == 4:
        #codigo agregar jugadores    
        print("codigo Juego Mundialista")
    if opcion == 5:
        #codigo salir del sistema    
        quit()

menuPrincipal()
