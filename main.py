# Como leer un archivo de excel
import openpyxl
import getpass
from datetime import datetime

filesheet = "./Jugadores.xlsx"

# Leer el archivo
wb = openpyxl.load_workbook(filesheet)

# Fijar la hoja
hojaPlayers = wb.get_sheet_by_name('Players')

def nuevoUsuario():
    #información dentro de las filas
    valido = True
    repetir = True

    #Repetir agregar
    while(repetir == True):
        #Validar que no exista el mismo ID
        while (valido == True):
            print("\n ============AGREGAR USUARIO============ \n")
            
            idUsuario = input("ID del usuario \n")

            for cell in hojaPlayers["A"]:
                if (cell.value == idUsuario):
                    valido = True
                    break
                elif(cell.value != idUsuario):
                    valido = False

            if (valido == False):
                print("ID valido")
                print ("")
                nombreUsuario = input("Nombre del usuario \n")
                datos = [(idUsuario, nombreUsuario, 0)]
                #Agregar usuario en linea
                for row in datos:
                    hojaPlayers.append(row)
                    wb.save(filesheet)
                    print("******Jugador agregado******")

            else:
                
                print("\nEl ID ingresado ya existe\nDigite uno nuevo")
            
        agregar = input("\n¿Desea agregar más usuarios? \n Digite SI o NO \n")

        if(agregar == "SI" or (agregar == "Si" or agregar == "si")):
            repetir = True
            valido = True
        else:
            repetir = False
    print()
    print ("\n 1) Menu principal \n 2) Volver")
    opcion = int(input("Ingrese la opcion a la que desea ingresar: "))
    if opcion == 1:
     menuPrincipal()
    else:
     menuJugadores()

def eliminarJugador():

    print("\n******Lista de Jugadores******")
    print("\nID", "   Nombre")
    for i in range(2, hojaPlayers.max_row +1):
        print()
        for j in range(1, hojaPlayers.max_column -3):
            celda = hojaPlayers.cell(row=i, column =j)
            print(celda.value, "  ", end = " ")
    print("")
    idUsuario = input("\nID del usuario que desea eliminar \n")
    contador = 0
    for cell in hojaPlayers["A"]:
        contador += 1
        if (cell.value == idUsuario):
            hojaPlayers.delete_rows(contador)    
            wb.save(filesheet)  
            print("******Jugador eliminado******")
            break
    print()
    print ("\n1) Menu principal",
        "\n2) Volver")
    opcion = int(input("Ingrese la opcion a la que desea ingresar: "))
    if opcion == 1:
     menuPrincipal()
    else:
     menuJugadores()
        
def mostrarJugadores():
    print("\nJugadores Disponibles")
    print("\nID", "   Nombre")
    for i in range(2, hojaPlayers.max_row +1):
        print()
        for j in range(1, hojaPlayers.max_column -3):
            celda = hojaPlayers.cell(row=i, column =j)
            print(celda.value, "  ", end = " ")
        
    print()
    print ("\n1) Menu principal",
        "\n2) Volver")
    opcion = int(input("Ingrese la opcion a la que desea ingresar: "))
    if opcion == 1:
     menuPrincipal()
    else:
     menuJugadores()

def volverMenuP():
    menuPrincipal()
    
def menuJugadores():
    print ("\n1) Agregar jugador",
    "\n2) Eliminar jugador",
    "\n3) Mostrar jugadores activos",
    "\n4) Volver\n")
    opcion = int(input("Ingrese la opcion a la que desea ingresar: "))
    if opcion == 1:
        #codigo agregar jugadores    
        nuevoUsuario()
    if opcion == 2:
        #codigo agregar jugadores    
        eliminarJugador()
    if opcion == 3:
        #Código ahorcado
        mostrarJugadores()
    if opcion == 4:
        #codigo agregar jugadores    
        volverMenuP()

def ahorcado():

    letrasIncorrectas = ""
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

        input("Presione ENTER")

        print("===================================================")
        print("El jugador 1 debe ingresar la palabra oculta",
            "\nEl único caracter especial permitido es la ñ",
            "\nEl jugador 2 debe ingresar una letra",
            "\nSi la letra es correcta se marcará de lo",
            "\ncontrario se agregaráuna pieza al muñeco.",
            "\nSi logra adivinar la palabra GANA",
            "\nsino lo logra PIERDE el juego")
        print("===================================================")

        palabra = getpass.getpass("Ingrese la palabra secreta: ") #No se debe de ver
        intentos = 0
        intento = 0
        win = False
        espacios  = "_" * len(palabra)

        tableroAhorcado = ['''

        +---+
        |   |
            |
            |
            |
            |

        =========''', '''

        +----+
        |    |
        O    |
             |
             |
             |
        =========''', '''

        +----+
        |    |
        O    |
        |    |
             |
             | 
        =========''', '''

        +----+
        |    |
        O    |
       /|    |
             |
             |
        =========''', '''

        +----+
        |    |
        O    |
       /|\   |
             |
             |
        =========''', '''

        +----+
        |    |
        O    |
       /|\   |
       /     |
             |
        =========''', '''

        +----+
        |    |
        O    |
       /|\   |
       / \   |
             |
        =========''']

        while((intento < 7) or (win)):
            letraCorrecta = False
            #nuevo
            print(tableroAhorcado[intentos])
            print ("Espacios: ", espacios)

            print("\n")
            letra = input("Ingrese una letra: ")
            print("\n")

            for i in range(len(palabra)):
                if (palabra[i] in letra):
                    espacios = espacios[:i] + palabra[i] + espacios[i+1:] #Agregamos letra, borramos espacio y imprimimos guiones
                    letraCorrecta = True #Si entra una vez queda fijo y se puede validar los intentos

                #Valiamos el ganador por encontrar palabra o superar intentos
                if(espacios == palabra):
                    win = False
                    intento = 7
                    ganador = jugadorDos
                    id = selectDos
                else:
                    ganador = jugadorUno
                    id = selectUno

            if(letraCorrecta != True): #Validamos solo una vez el verdadero y sumamos intentos
                intentos += 1
                intento = intentos
                letrasIncorrectas = letrasIncorrectas + letra
                print("Letras incorrectas: ", letrasIncorrectas)
        
        #Actualizar información
        i = 0
        for cell in hojaPlayers["A"]:
            i += 1
            if (cell.value == id):
                    #agregar victoria a jugador
                    ubicacionWinA = 'E'+ str(i) #colocamos la ubicación de la celda de Excel
                    datoCelda = int(hojaPlayers[ubicacionWinA].value) #Convertimos el valor a INT
                    victorias = datoCelda + 1 #Sumamos valor base con el gane
                    hojaPlayers[ubicacionWinA] = str(victorias) #insertamos el nuevo valor
                    
                    #Agregar fecha actual
                    ubicacionFechaA = 'F'+ str(i) #colocamos la ubicación de la celda de Excel
                    now = datetime.now()
                    fecha = now.strftime('%d/%m/%Y %H:%M') #Usamos libreria datetime para la fecha
                    hojaPlayers[ubicacionFechaA] = str(fecha) #insertamos el nuevo valor
                    wb.save(filesheet)
                    break
                    
        #Validamos el ganador para imprimir el final correspondiente
        if(ganador == jugadorUno):
            print("\n============== FIN DEL JUEGO ==============\n")
            print("La palabra es: ", palabra)
            print("El ganador es: ", ganador)
            print("\n")
        else:
            print("\n============== FIN DEL JUEGO ==============\n")
            print(tableroAhorcado[intentos])
            print ("Espacios: ", espacios)
            print("El ganador es: ", ganador)
            print("\n")

        input("PULSE ENTER PARA CONTINUAR\n")
        
        #imprimir reporte
        print("\n=================== REGISTRO HISTORICO AHORCADO ===================\n")
        #buscar en la lista
        print("ID_USUARIO         WINS         ULTIMO JUEGO")
        for select in range(2, hojaPlayers.max_row +1):
            print(hojaPlayers[f"A{select}"].value, "                ",hojaPlayers[f"E{select}"].value, "       ",hojaPlayers[f"F{select}"].value, "\n") #imprimir jugadores
        
        input("PULSE ENTER PARA CONTINUAR\n")

        #Opciones de final del juego
        print("\n1) ¿Desea volver a jugar? \n2) Volver al menú principal \n3) Salir")
        seleccion = input()

        if(seleccion == 1):
            ahorcado()
        elif(seleccion == 2):
            menuPrincipal()
        else:
            quit()
    else:
              print("No existen jugadores suficientes para jugar")

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
