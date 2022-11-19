from datetime import datetime

# Como leer un archivo de excel
import openpyxl

filesheet = "./Jugadores.xlsx"

# Leer el archivo
wb = openpyxl.load_workbook(filesheet)

# Fijar la hoja
hojaPlayers = wb.get_sheet_by_name('Players')

#declarar matriz
tablero = []
fila=0
columna=0
vGanador=0

#rellenamos la matriz con datos
for i in range(3):
    tablero.append([" "] * 3)

def pintarTablero(tablero):
#imprimimos el tablero con los limites
    print("\n")
    print(tablero[0][0], " | ", tablero[0][1], " | ", tablero[0][2],)
    print("-------------")
    print(tablero[1][0], " | ", tablero[1][1], " | ", tablero[1][2],)
    print("-------------")
    print(tablero[2][0], " | ", tablero[2][1], " | ", tablero[2][2],)

def verificar(tablero):
    if(tablero[0][0]=="X" and tablero[0][1]=="X"and tablero[0][2]=="X"):  
        print("Ganaste jugador X")
        vGanador=1
    elif(tablero[1][0]=="X"and tablero[1][1]=="X"and tablero[1][2]=="X"):
        print("Ganaste jugador X")
        vGanador=1
    elif(tablero[2][0]=="X"and tablero[2][1]=="X"and tablero[2][2]=="X"):
        print("Ganaste jugador X")
        vGanador=1
    elif(tablero[0][0]=="X" and tablero[1][0]=="X"and tablero[2][0]=="X"):  
        print("Ganaste jugador X")
        vGanador=1
    elif(tablero[0][1]=="X"and tablero[1][1]=="X"and tablero[2][1]=="X"):
        print("Ganaste jugador X")
        vGanador=1
    elif(tablero[0][2]=="X"and tablero[1][2]=="X"and tablero[2][2]=="X"):
        print("Ganaste jugador X")
        vGanador=1
    elif(tablero[0][0]=="X" and tablero[1][1]=="X"and tablero[2][2]=="X"):  
        print("Ganaste jugador X")
        vGanador=1
    elif(tablero[0][2]=="X"and tablero[1][1]=="X"and tablero[2][0]=="X"):
        print("Ganaste jugador X")
        vGanador=1
    elif(tablero[0][0]=="O" and tablero[0][1]=="O"and tablero[0][2]=="O"):  
        print("Ganaste jugador")
        vGanador=1
    elif(tablero[1][0]=="O"and tablero[1][1]=="O"and tablero[1][2]=="O"):
        print("Ganaste jugador")
        vGanador=1
    elif(tablero[2][0]=="O"and tablero[2][1]=="O"and tablero[2][2]=="O"):
        print("Ganaste jugador")
        vGanador=1
    elif(tablero[0][0]=="O" and tablero[1][0]=="O"and tablero[2][0]=="O"):  
        print("Ganaste jugador")
        vGanador=1
    elif(tablero[0][1]=="O"and tablero[1][1]=="O"and tablero[2][1]=="O"):
        print("Ganaste jugador")
        vGanador=1
    elif(tablero[0][2]=="O"and tablero[1][2]=="O"and tablero[2][2]=="O"):
        print("Ganaste jugador")
        vGanador=1
    elif(tablero[0][0]=="O" and tablero[1][1]=="O"and tablero[2][2]=="O"):  
        print("Ganaste jugador")
        vGanador=1
    elif(tablero[0][2]=="O"and tablero[1][1]=="O"and tablero[2][0]=="O"):
        print("Ganaste jugador")
        vGanador=1
    
    elif(tablero[0][0]=="X"and tablero[0][1]=="X"and tablero[0][2]=="O"):
        print("Empate")
        vGanador=2
    elif(tablero[1][0]=="X"and tablero[1][1]=="O" and tablero[1][2]=="X"):
        print("Empate")
        vGanador=2
    elif(tablero[2][0]=="O"and tablero[2][1]=="O"and tablero[2][2]=="X"):
        print("Empate")
        vGanador=2
    elif(tablero[0][0]=="O"and tablero[0][1]=="X"and tablero[0][2]=="O"):
        print("Empate")
        vGanador=2
    elif(tablero[1][0]=="X"and tablero[1][1]=="X" and tablero[1][2]=="O"):
        print("Empate")
        vGanador=2
    elif(tablero[2][0]=="X"and tablero[2][1]=="O"and tablero[2][2]=="X"):
        print("Empate")
        vGanador=2
    elif(tablero[0][0]=="O"and tablero[0][1]=="X"and tablero[0][2]=="O"):
        print("Empate")
        vGanador=2
    elif(tablero[1][0]=="X"and tablero[1][1]=="X" and tablero[1][2]=="O"):
        print("Empate")
        vGanador=2
    elif(tablero[2][0]=="O"and tablero[2][1]=="O"and tablero[2][2]=="X"):
        print("Empate")
        vGanador=2
    else: 
        vGanador=0

    return vGanador

def gatoGame():
    winDos=False
    winUno=False
    vGanador=0

    #Valida cuanto jugadores existen
    for i in range(2, hojaPlayers.max_row+1):
        cantidadJugadores = i - 1

    if cantidadJugadores >= 2: 
        #Lista de jugadores disponibles
        print("Jugadores Disponibles")
        for i in range(2, hojaPlayers.max_row +1):
            print("\n")
    
            for j in range(1, hojaPlayers.max_column -4):
              celda = hojaPlayers.cell(row=i, column =j)
              print("ID:",celda.value, end = " ")

        print("\n")

    #Seleccionar jugador
    selectUno = input("Por favor, ingrese solamente el ID del jugador uno: ")
    print("")
    selectDos = input("Por favor, ingrese solamente el ID del jugador dos: ")

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

    #reiniciar tablero
    tablero = []
    fila=0
    columna=0

    #rellenamos la matriz con datos
    for i in range(3):
        tablero.append([" "] * 3)

    #invocar funcion
    pintarTablero(tablero)
    repetir=True 

    while(repetir): #pasar turno hasta ganar

        if(winDos == False):
            print("\n")
            print("Turno de: ", jugadorUno)
            fila = int(input("Coloque la fila donde quiere colcar la X:")) - 1
            columna = int(input("Coloque la Columna donde quiere colcar la X:")) - 1
            tablero[fila][columna] = "X"
            pintarTablero(tablero)

            if (verificar(tablero) == 1):
                print("El ganador es: " + jugadorUno)
                repetir = False
                winUno = True
                break
            elif (verificar(tablero) == 2):
                print("Empate")
                repetir = False
                break
            else:
                print("")
         
        if (winUno == False):
            print("\n")
            print("Turno de: ", jugadorDos)
            fila = int(input("Coloque la fila donde quiere colcar la O:")) - 1
            columna = int(input("Coloque la Columna donde quiere colcar la O:")) - 1
            tablero[fila][columna] = "O"
            pintarTablero(tablero)
                
            if (verificar(tablero) == 1):
                print("El ganador es: " + jugadorDos)
                repetir = False
                winDos = True
                break
            elif (verificar(tablero) == 2):
                print("Empate")
                repetir = False
                break
            else:
                print("")

    print("Menu: \n1- Iniciar juego \n2- Volver a jugar \n3- Salir\n")
    opcionMenu=int(input())
    if(opcionMenu==1 or 2):
        print()

    elif(opcionMenu==3):
        print("Gracias por jugar")

    print ("Juego terminado")

    print("1- Volver a menu de juegos  2-Volver a menu de gato")
    menuGrande=int(input())

    if(menuGrande==2):
        gatoGame()
    elif(menuGrande==1):
        print("aqui va lo del menu principal")