import random

intento = True

def subMenu():
    while(intento):
        print("======== QUINIELA MUNDIALISTA ========\n")
        print ("\n1) Buscar al Campeón del Mundo",
        "\n2) Modificar participantes",
        "\n3) Reorganizar los grupos del mundial",
        "\n4) Volver al menú principal")
        print("=========================================\n")
        opcion = int(input("Ingrese la opcion a la que desea ingresar: "))

        if opcion == 1:
            #codigo Buscar Campeon  
            print()
            intento = False
        elif opcion == 2:
            #codigo Modificar participantes   
            print()
            intento = False
        elif opcion == 3:
            #Código reorganizar los grupos
            print()
            intento = False
        elif opcion == 4:
            #codigo Menú principal    
            import main
            main.menuPrincipal()
            intento = False
        else:
            #Otra vuleta
            print("Ingrese un número valido")
            intento = True
