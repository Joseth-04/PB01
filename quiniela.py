import random
import openpyxl # Como leer un archivo de excel

filesheet = "./QuinielaM.xlsx"

# Leer el archivo
wb = openpyxl.load_workbook(filesheet)

# Fijar la hoja
hojaParticipantes = wb.get_sheet_by_name('Participantes')

intento = True
listaInicial = []


for cell in hojaParticipantes["A"]: #Cantidad de columnas necesarias
    listaInicial.append(cell.value) #Agregar participante

grupoA = [listaInicial[0],listaInicial[1],listaInicial[2],listaInicial[3]]
grupoB = [listaInicial[4],listaInicial[5],listaInicial[6],listaInicial[7]]
grupoC = [listaInicial[8],listaInicial[9],listaInicial[10],listaInicial[11]]
grupoD = [listaInicial[12],listaInicial[13],listaInicial[14],listaInicial[15]]
grupoE = [listaInicial[16],listaInicial[17],listaInicial[18],listaInicial[19]]
grupoF = [listaInicial[20],listaInicial[21],listaInicial[22],listaInicial[23]]
grupoG = [listaInicial[24],listaInicial[25],listaInicial[26],listaInicial[27]]
grupoH = [listaInicial[28],listaInicial[29],listaInicial[30],listaInicial[31]]

#Alterar lista
random.shuffle(listaInicial)

def grupos():
    #Asignamos participantes por grupo
    grupoA = [listaInicial[0],listaInicial[1],listaInicial[2],listaInicial[3]]
    grupoB = [listaInicial[4],listaInicial[5],listaInicial[6],listaInicial[7]]
    grupoC = [listaInicial[8],listaInicial[9],listaInicial[10],listaInicial[11]]
    grupoD = [listaInicial[12],listaInicial[13],listaInicial[14],listaInicial[15]]
    grupoE = [listaInicial[16],listaInicial[17],listaInicial[18],listaInicial[19]]
    grupoF = [listaInicial[20],listaInicial[21],listaInicial[22],listaInicial[23]]
    grupoG = [listaInicial[24],listaInicial[25],listaInicial[26],listaInicial[27]]
    grupoH = [listaInicial[28],listaInicial[29],listaInicial[30],listaInicial[31]]

    #Asignar enfrentamientos
    #A
    enfrentamientoA = [[grupoA[0],0,0,grupoA[1],0,0]]
    vsGrupoA_A = [grupoA[0],0,0,grupoA[1],0,0]
    vsGrupoA_B = [grupoA[0],random.randint(0,10),grupoA[2],random.randint(0,10)]
    vsGrupoA_C = [grupoA[0],random.randint(0,10),grupoA[3],random.randint(0,10)]
    vsGrupoA_D = [grupoA[1],random.randint(0,10),grupoA[2],random.randint(0,10)]
    vsGrupoA_E = [grupoA[1],random.randint(0,10),grupoA[3],random.randint(0,10)]
    vsGrupoA_F = [grupoA[2],random.randint(0,10),grupoA[3],random.randint(0,10)]
    
    #B
    vsGrupoB_A = [grupoB[0],random.randint(0,10),grupoB[1],random.randint(0,10)]
    vsGrupoB_B = [grupoB[0],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoB_C = [grupoB[0],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoB_D = [grupoB[1],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoB_E = [grupoB[1],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoB_F = [grupoB[2],random.randint(0,10),grupoB[3],random.randint(0,10)]
    
    #C
    vsGrupoC_A = [grupoB[0],random.randint(0,10),grupoB[1],random.randint(0,10)]
    vsGrupoC_B = [grupoB[0],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoC_C = [grupoB[0],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoC_D = [grupoB[1],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoC_E = [grupoB[1],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoC_F = [grupoB[2],random.randint(0,10),grupoB[3],random.randint(0,10)]
    
    #D
    vsGrupoD_A = [grupoB[0],random.randint(0,10),grupoB[1],random.randint(0,10)]
    vsGrupoD_B = [grupoB[0],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoD_C = [grupoB[0],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoD_D = [grupoB[1],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoD_E = [grupoB[1],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoD_F = [grupoB[2],random.randint(0,10),grupoB[3],random.randint(0,10)]
    
    #E
    vsGrupoE_A = [grupoB[0],random.randint(0,10),grupoB[1],random.randint(0,10)]
    vsGrupoE_B = [grupoB[0],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoE_C = [grupoB[0],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoE_D = [grupoB[1],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoE_E = [grupoB[1],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoE_F = [grupoB[2],random.randint(0,10),grupoB[3],random.randint(0,10)]
    
    #F
    vsGrupoF_A = [grupoB[0],random.randint(0,10),grupoB[1],random.randint(0,10)]
    vsGrupoF_B = [grupoB[0],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoF_C = [grupoB[0],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoF_D = [grupoB[1],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoF_E = [grupoB[1],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoF_F = [grupoB[2],random.randint(0,10),grupoB[3],random.randint(0,10)]
    
    #G
    vsGrupoG_A = [grupoB[0],random.randint(0,10),grupoB[1],random.randint(0,10)]
    vsGrupoG_B = [grupoB[0],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoG_C = [grupoB[0],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoG_D = [grupoB[1],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoG_E = [grupoB[1],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoG_F = [grupoB[2],random.randint(0,10),grupoB[3],random.randint(0,10)]
    
    #H
    vsGrupoH_A = [grupoB[0],random.randint(0,10),grupoB[1],random.randint(0,10)]
    vsGrupoH_B = [grupoB[0],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoH_C = [grupoB[0],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoH_D = [grupoB[1],random.randint(0,10),grupoB[2],random.randint(0,10)]
    vsGrupoH_E = [grupoB[1],random.randint(0,10),grupoB[3],random.randint(0,10)]
    vsGrupoH_F = [grupoB[2],random.randint(0,10),grupoB[3],random.randint(0,10)]

def simulacion_grupos():
    #puntos
    print()

def sub_menu():
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

def campeon(): #Codigo campeon
    print()

def modificar_participantes():
    print()

def reorganizar_grupos():
    print()
