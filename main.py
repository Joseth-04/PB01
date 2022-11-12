import Ahorcado as ahor
import Usuarios as users
import Gato as cat

# Como leer un archivo de excel
import openpyxl

filesheet = "./Jugadores.xlsx"

# Leer el archivo
wb = openpyxl.load_workbook(filesheet)

# Fijar la hoja
hojaPlayers = wb.get_sheet_by_name('Players')

def volverMenuP():
    menuPrincipal()
  
def menuPrincipal():
    print("=========================================\n")
    print("=============CENTRAL DE JUEGOS===========\n")
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
    if opcion == 2:
        #codigo agregar jugadores    
        cat.gato()
    if opcion == 3:
        #Código ahorcado
        ahor.ahorcado()
    if opcion == 4:
        #codigo agregar jugadores    
        print("codigo Juego Mundialista")
    if opcion == 5:
        #codigo salir del sistema    
        quit()

menuPrincipal()
