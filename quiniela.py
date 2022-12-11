import random
import openpyxl # Como leer un archivo de excel

filesheet = "./QuinielaM.xlsx"

# Leer el archivo
wb = openpyxl.load_workbook(filesheet)

# Fijar la hoja
hojaParticipantes = wb.get_sheet_by_name('Participantes')

intento = True
listaInicial = []
enfrentamientoA = []
enfrentamientoB = []
enfrentamientoC = []
enfrentamientoD = []
enfrentamientoE = []
enfrentamientoF = []
enfrentamientoG = []
enfrentamientoH = []

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
    enfrentamientoA = [[grupoA[0],0,0,grupoA[1],0,0],
                    [grupoA[0],0,0,grupoA[2],0,0],
                    [grupoA[0],0,0,grupoA[3],0,0],
                    [grupoA[1],0,0,grupoA[2],0,0],
                    [grupoA[1],0,0,grupoA[3],0,0],
                    [grupoA[2],0,0,grupoA[3],0,0]]
    
    #B
    enfrentamientoB = [[grupoB[0],0,0,grupoB[1],0,0],
                    [grupoB[0],0,0,grupoB[2],0,0],
                    [grupoB[0],0,0,grupoB[3],0,0],
                    [grupoB[1],0,0,grupoB[2],0,0],
                    [grupoB[1],0,0,grupoB[3],0,0],
                    [grupoB[2],0,0,grupoB[3],0,0]]
    
    #C
    enfrentamientoC = [[grupoC[0],0,0,grupoC[1],0,0],
                    [grupoC[0],0,0,grupoC[2],0,0],
                    [grupoC[0],0,0,grupoC[3],0,0],
                    [grupoC[1],0,0,grupoC[2],0,0],
                    [grupoC[1],0,0,grupoC[3],0,0],
                    [grupoC[2],0,0,grupoC[3],0,0]]
    
    #D
    enfrentamientoD = [[grupoD[0],0,0,grupoD[1],0,0],
                    [grupoD[0],0,0,grupoD[2],0,0],
                    [grupoD[0],0,0,grupoD[3],0,0],
                    [grupoD[1],0,0,grupoD[2],0,0],
                    [grupoD[1],0,0,grupoD[3],0,0],
                    [grupoD[2],0,0,grupoD[3],0,0]]

    #E
    enfrentamientoE = [[grupoE[0],0,0,grupoE[1],0,0],
                    [grupoE[0],0,0,grupoE[2],0,0],
                    [grupoE[0],0,0,grupoE[3],0,0],
                    [grupoE[1],0,0,grupoE[2],0,0],
                    [grupoE[1],0,0,grupoE[3],0,0],
                    [grupoE[2],0,0,grupoE[3],0,0]]

    #F
    enfrentamientoF = [[grupoF[0],0,0,grupoF[1],0,0],
                    [grupoF[0],0,0,grupoF[2],0,0],
                    [grupoF[0],0,0,grupoF[3],0,0],
                    [grupoF[1],0,0,grupoF[2],0,0],
                    [grupoF[1],0,0,grupoF[3],0,0],
                    [grupoF[2],0,0,grupoF[3],0,0]]

    #G
    enfrentamientoG = [[grupoG[0],0,0,grupoG[1],0,0],
                    [grupoG[0],0,0,grupoG[2],0,0],
                    [grupoG[0],0,0,grupoG[3],0,0],
                    [grupoG[1],0,0,grupoG[2],0,0],
                    [grupoG[1],0,0,grupoG[3],0,0],
                    [grupoG[2],0,0,grupoG[3],0,0]]


    #H
    enfrentamientoH = [[grupoH[0],0,0,grupoH[1],0,0],
                    [grupoH[0],0,0,grupoH[2],0,0],
                    [grupoH[0],0,0,grupoH[3],0,0],
                    [grupoH[1],0,0,grupoH[2],0,0],
                    [grupoH[1],0,0,grupoH[3],0,0],
                    [grupoH[2],0,0,grupoH[3],0,0]]

    #puntos
    for i in range(6):
        golA_A = random.randint(0, 10)
        golA_B = random.randint(0, 10)
        
        if(golA_A > golA_B):
            enfrentamientoA[i][2] = 3
        elif(golA_A == golA_B):
            enfrentamientoA[i][2] = 1
            enfrentamientoA[i][5] = 1
        else:
            enfrentamientoA[i][5] = 3

        enfrentamientoA[i][1] = golA_A
        enfrentamientoA[i][4] = golA_B

         #Actualizar información

        x = 0
        participante1 = enfrentamientoA[i][0]
        participante2 = enfrentamientoA[i][3]
        for cell in hojaParticipantes["A"]:
            x += 1
            if (cell.value == participante1):
                #Actualizar puntos
                ubicacionPuntosA_A = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptoA_A = int(hojaParticipantes[ubicacionPuntosA_A].value) + enfrentamientoA[i][2]
                hojaParticipantes[ubicacionPuntosA_A] = str(ptoA_A) #insertamos el nuevo valor
                wb.save(filesheet)
                
            if (cell.value == participante2):
                #Actualizar puntos
                ubicacionPuntosA_B = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptoA_B = int(hojaParticipantes[ubicacionPuntosA_B].value) + enfrentamientoA[i][5]
                hojaParticipantes[ubicacionPuntosA_B] = str(ptoA_B) #insertamos el nuevo valor
                wb.save(filesheet)
                

    print(enfrentamientoA)

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

grupos()
