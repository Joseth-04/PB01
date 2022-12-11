import Ahorcado as ahor
import Usuarios as users
import Gato as cat

# Como leer un archivo de excel
import openpyxl

filesheet = "./Jugadores.xlsx"
selecMenu = True

# Leer el archivo
wb = openpyxl.load_workbook(filesheet)

# Fijar la hoja
hojaPlayers = wb.get_sheet_by_name('Players')

def volverMenuP():
    menuPrincipal()
  
def menuPrincipal():
    selecMenu = True
    while(selecMenu):
        print("=========================================\n")
        print("============CENTRAL DE JUEGOS============\n")
        print("=========================================")
        print ("\n1) Jugadores",
        "\n2) Juego Gato",
        "\n3) Juego Ahorcado",
        "\n4) Juego Mundialista",
        "\n5) Salir del juego\n")
        print("=========================================\n")
        opcion = int(input("Ingrese la opcion a la que desea ingresar: "))

        if opcion == 1:
            #codigo agregar jugadores    
            users.menuJugadores()
            selecMenu = False
        elif opcion == 2:
            #codigo agregar jugadores    
            cat.gatoGame()
            selecMenu = False
        elif opcion == 3:
            #Código ahorcado
            ahor.ahorcado()
            selecMenu = False
        elif opcion == 4:
            #codigo agregar jugadores    
            print("codigo Juego Mundialista")
            selecMenu = False
        elif opcion == 5:
            #codigo salir del sistema
            selecMenu = False    
            quit()
        else:
            #Otra vuleta
            print("Ingrese un número valido")
            selecMenu = True

menuPrincipal()
