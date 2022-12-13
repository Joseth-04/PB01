import random
import openpyxl # Como leer un archivo de excel

filesheet = "./QuinielaM.xlsx"

# Leer el archivo
wb = openpyxl.load_workbook(filesheet)

# Fijar la hoja
hojaParticipantes = wb.get_sheet_by_name('Participantes')

intento = True
listaInicial = []
resGA = []
resGB = []
resGC = []
resGD = []
resGE = []
resGF = []
resGG = []
resGH = []

x = 0
for cell in hojaParticipantes["A"]:
    x += 1
    ubicacionPto = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
    hojaParticipantes[ubicacionPto] = str(0) #insertamos el nuevo valor
    wb.save(filesheet)

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
#random.shuffle(listaInicial)

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
        goles = [random.randint(0, 10),random.randint(0, 10), #Grupo A
                random.randint(0, 10),random.randint(0, 10), #Grupo B
                random.randint(0, 10),random.randint(0, 10), #Grupo C
                random.randint(0, 10),random.randint(0, 10), #Grupo D
                random.randint(0, 10),random.randint(0, 10), #Grupo E
                random.randint(0, 10),random.randint(0, 10), #Grupo F
                random.randint(0, 10),random.randint(0, 10), #Grupo G
                random.randint(0, 10),random.randint(0, 10)] #Grupo H
        
        if(goles[0] > goles[1]):
            enfrentamientoA[i][2] = 3
        elif(goles[0] == goles[1]):
            enfrentamientoA[i][2] = 1
            enfrentamientoA[i][5] = 1
        else:
            enfrentamientoA[i][5] = 3
        
        if(goles[2] > goles[3]):
            enfrentamientoB[i][2] = 3
        elif(goles[2] == goles[3]):
            enfrentamientoB[i][2] = 1
            enfrentamientoB[i][5] = 1
        else:
            enfrentamientoB[i][5] = 3
        
        if(goles[4] > goles[5]):
            enfrentamientoC[i][2] = 3
        elif(goles[4] == goles[5]):
            enfrentamientoC[i][2] = 1
            enfrentamientoC[i][5] = 1
        else:
            enfrentamientoC[i][5] = 3
        
        if(goles[6] > goles[7]):
            enfrentamientoD[i][2] = 3
        elif(goles[6] == goles[7]):
            enfrentamientoD[i][2] = 1
            enfrentamientoD[i][5] = 1
        else:
            enfrentamientoD[i][5] = 3
        
        if(goles[8] > goles[9]):
            enfrentamientoE[i][2] = 3
        elif(goles[8] == goles[9]):
            enfrentamientoE[i][2] = 1
            enfrentamientoE[i][5] = 1
        else:
            enfrentamientoE[i][5] = 3
        
        if(goles[10] > goles[11]):
            enfrentamientoF[i][2] = 3
        elif(goles[10] == goles[11]):
            enfrentamientoF[i][2] = 1
            enfrentamientoF[i][5] = 1
        else:
            enfrentamientoF[i][5] = 3
        
        if(goles[12] > goles[13]):
            enfrentamientoG[i][2] = 3
        elif(goles[12] == goles[13]):
            enfrentamientoG[i][2] = 1
            enfrentamientoG[i][5] = 1
        else:
            enfrentamientoG[i][5] = 3
        
        if(goles[14] > goles[15]):
            enfrentamientoH[i][2] = 3
        elif(goles[14] == goles[15]):
            enfrentamientoH[i][2] = 1
            enfrentamientoH[i][5] = 1
        else:
            enfrentamientoH[i][5] = 3


        enfrentamientoA[i][1] = goles[0]
        enfrentamientoA[i][4] = goles[1]
        enfrentamientoB[i][1] = goles[2]
        enfrentamientoB[i][4] = goles[3]
        enfrentamientoC[i][1] = goles[4]
        enfrentamientoC[i][4] = goles[5]
        enfrentamientoD[i][1] = goles[6]
        enfrentamientoD[i][4] = goles[7]
        enfrentamientoE[i][1] = goles[8]
        enfrentamientoE[i][4] = goles[9]
        enfrentamientoF[i][1] = goles[10]
        enfrentamientoF[i][4] = goles[11]
        enfrentamientoG[i][1] = goles[12]
        enfrentamientoG[i][4] = goles[13]
        enfrentamientoH[i][1] = goles[14]
        enfrentamientoH[i][4] = goles[15]

        #Actualizar información
        x = 0
        participantes = [enfrentamientoA[i][0], enfrentamientoA[i][3],
                        enfrentamientoB[i][0], enfrentamientoB[i][3],
                        enfrentamientoC[i][0], enfrentamientoC[i][3],
                        enfrentamientoD[i][0], enfrentamientoD[i][3],
                        enfrentamientoE[i][0], enfrentamientoE[i][3],
                        enfrentamientoF[i][0], enfrentamientoF[i][3],
                        enfrentamientoG[i][0], enfrentamientoG[i][3],
                        enfrentamientoH[i][0], enfrentamientoH[i][3]]
        
        for cell in hojaParticipantes["A"]:
            x += 1
            if (cell.value == participantes[0]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoA[i][2]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)
                
            elif (cell.value == participantes[1]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoA[i][5]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)

            elif (cell.value == participantes[2]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoB[i][2]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)
                
            elif (cell.value == participantes[3]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoB[i][5]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)

            elif (cell.value == participantes[4]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoC[i][2]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)
                
            elif (cell.value == participantes[5]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoC[i][5]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)

            elif (cell.value == participantes[6]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoD[i][2]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)
                
            elif (cell.value == participantes[7]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoD[i][5]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)

            elif (cell.value == participantes[8]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoE[i][2]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)
                
            elif (cell.value == participantes[9]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoE[i][5]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)

            elif (cell.value == participantes[10]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoF[i][2]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)
                
            elif (cell.value == participantes[11]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoF[i][5]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)

            elif (cell.value == participantes[12]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoG[i][2]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)
                
            elif (cell.value == participantes[13]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoG[i][5]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)

            elif (cell.value == participantes[14]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoH[i][2]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)
                
            elif (cell.value == participantes[15]):
                #Actualizar puntos
                ubicacionPuntos = 'B'+ str(x) #colocamos la ubicación de la celda de Excel
                ptos = int(hojaParticipantes[ubicacionPuntos].value) + enfrentamientoH[i][5]
                hojaParticipantes[ubicacionPuntos] = str(ptos) #insertamos el nuevo valor
                wb.save(filesheet)

    contador = 0 #cargar datos de los resultados para semifinales
    for cont in range(1, 33):
        ubicacionEquipoA = 'A'+ str(cont) #colocamos la ubicación de la celda de Excel
        ubicacionEquipoB = 'B'+ str(cont) #colocamos la ubicación de la celda de Excel
        if(hojaParticipantes[ubicacionEquipoA].value == grupoA[contador]):
            resGA.append(hojaParticipantes[ubicacionEquipoA].value)
            resGA.append(hojaParticipantes[ubicacionEquipoB].value)
            contador += 1
            if(contador == 4):
                contador = 0

        elif(hojaParticipantes[ubicacionEquipoA].value == grupoB[contador]):
            resGB.append(hojaParticipantes[ubicacionEquipoA].value)
            resGB.append(hojaParticipantes[ubicacionEquipoB].value)
            contador += 1
            if(contador == 4):
                contador = 0

        elif(hojaParticipantes[ubicacionEquipoA].value == grupoC[contador]):
            resGC.append(hojaParticipantes[ubicacionEquipoA].value)
            resGC.append(hojaParticipantes[ubicacionEquipoB].value)
            contador += 1
            if(contador == 4):
                contador = 0

        elif(hojaParticipantes[ubicacionEquipoA].value == grupoD[contador]):
            resGD.append(hojaParticipantes[ubicacionEquipoA].value)
            resGD.append(hojaParticipantes[ubicacionEquipoB].value)
            contador += 1
            if(contador == 4):
                contador = 0

        elif(hojaParticipantes[ubicacionEquipoA].value == grupoE[contador]):
            resGE.append(hojaParticipantes[ubicacionEquipoA].value)
            resGE.append(hojaParticipantes[ubicacionEquipoB].value)
            contador += 1
            if(contador == 4):
                contador = 0

        elif(hojaParticipantes[ubicacionEquipoA].value == grupoF[contador]):
            resGF.append(hojaParticipantes[ubicacionEquipoA].value)
            resGF.append(hojaParticipantes[ubicacionEquipoB].value)
            contador += 1
            if(contador == 4):
                contador = 0

        elif(hojaParticipantes[ubicacionEquipoA].value == grupoG[contador]):
            resGG.append(hojaParticipantes[ubicacionEquipoA].value)
            resGG.append(hojaParticipantes[ubicacionEquipoB].value)
            contador += 1
            if(contador == 4):
                contador = 0

        elif(hojaParticipantes[ubicacionEquipoA].value == grupoH[contador]):
            resGH.append(hojaParticipantes[ubicacionEquipoA].value)
            resGH.append(hojaParticipantes[ubicacionEquipoB].value)
            contador += 1
            if(contador == 4):
                contador = 0
        
    doble = 1
    semiptA = 0
    semiptB = 0
    semiEqA = ""
    semiEqB = ""
    semiAA = []
    print("**Grupo A**")
    print("Equipo       Puntos")
    for x in range(0, 8, 2):
        print(resGA[x], " ....... ", resGA[doble])
        if(int(resGA[doble]) >= semiptA):
            semiptA = int(resGA[doble])
            semiEqA = resGA[x]
        
        if(int(resGA[doble]) <= semiptA and int(resGA[doble]) > semiptB and semiEqB != semiEqA):
            semiptB = int(resGA[doble])
            semiEqB = resGA[x]
        doble += 2
    semiAA.append(semiEqA)
    semiAA.append(semiEqB)

    input("\npresione ENTER para continuar\n")
        
    doble = 1
    print("**Grupo B**")
    print("Equipo       Puntos")
    for x in range(0, 8, 2):
        print(resGB[x], " ....... ", resGB[doble])
        print(resGA[x], " ....... ", resGA[doble])
        if(int(resGA[doble]) >= semiptA):
            semiptA = int(resGA[doble])
            semiEqA = resGA[x]
        
        if(int(resGA[doble]) <= semiptA and int(resGA[doble]) > semiptB and semiEqB != semiEqA):
            semiptB = int(resGA[doble])
            semiEqB = resGA[x]
        doble += 2
    semiAA.append(semiEqA)
    semiAA.append(semiEqB)

    input("\npresione ENTER para continuar\n")
        
    doble = 1
    print("**Grupo C**")
    print("Equipo       ----- Puntos -----")
    for x in range(0, 8, 2):
        print(resGC[x], " ....... ", resGC[doble])
        print(resGA[x], " ....... ", resGA[doble])
        if(int(resGA[doble]) >= semiptA):
            semiptA = int(resGA[doble])
            semiEqA = resGA[x]
        
        if(int(resGA[doble]) <= semiptA and int(resGA[doble]) > semiptB and semiEqB != semiEqA):
            semiptB = int(resGA[doble])
            semiEqB = resGA[x]
        doble += 2
    semiAA.append(semiEqA)
    semiAA.append(semiEqB)

    input("\npresione ENTER para continuar\n")
        
    doble = 1
    print("**Grupo D**")
    print("Equipo       ----- Puntos -----")
    for x in range(0, 8, 2):
        print(resGD[x], " ....... ", resGD[doble])
        print(resGA[x], " ....... ", resGA[doble])
        if(int(resGA[doble]) >= semiptA):
            semiptA = int(resGA[doble])
            semiEqA = resGA[x]
        
        if(int(resGA[doble]) <= semiptA and int(resGA[doble]) > semiptB and semiEqB != semiEqA):
            semiptB = int(resGA[doble])
            semiEqB = resGA[x]
        doble += 2
    semiAA.append(semiEqA)
    semiAA.append(semiEqB)

    input("\npresione ENTER para continuar\n")
        
    doble = 1
    print("**Grupo E**")
    print("Equipo       ----- Puntos -----")
    for x in range(0, 8, 2):
        print(resGE[x], " ....... ", resGE[doble])
        print(resGA[x], " ....... ", resGA[doble])
        if(int(resGA[doble]) >= semiptA):
            semiptA = int(resGA[doble])
            semiEqA = resGA[x]
        
        if(int(resGA[doble]) <= semiptA and int(resGA[doble]) > semiptB and semiEqB != semiEqA):
            semiptB = int(resGA[doble])
            semiEqB = resGA[x]
        doble += 2
    semiAA.append(semiEqA)
    semiAA.append(semiEqB)

    input("\npresione ENTER para continuar\n")
        
    doble = 1
    print("**Grupo F**")
    print("Equipo       ----- Puntos -----")
    for x in range(0, 8, 2):
        print(resGF[x], " ....... ", resGF[doble])
        print(resGA[x], " ....... ", resGA[doble])
        if(int(resGA[doble]) >= semiptA):
            semiptA = int(resGA[doble])
            semiEqA = resGA[x]
        
        if(int(resGA[doble]) <= semiptA and int(resGA[doble]) > semiptB and semiEqB != semiEqA):
            semiptB = int(resGA[doble])
            semiEqB = resGA[x]
        doble += 2
    semiAA.append(semiEqA)
    semiAA.append(semiEqB)

    input("\npresione ENTER para continuar\n")
        
    doble = 1
    print("**Grupo G**")
    print("Equipo       ----- Puntos -----")
    for x in range(0, 8, 2):
        print(resGG[x], " ....... ", resGG[doble])
        print(resGA[x], " ....... ", resGA[doble])
        if(int(resGA[doble]) >= semiptA):
            semiptA = int(resGA[doble])
            semiEqA = resGA[x]
        
        if(int(resGA[doble]) <= semiptA and int(resGA[doble]) > semiptB and semiEqB != semiEqA):
            semiptB = int(resGA[doble])
            semiEqB = resGA[x]
        doble += 2
    semiAA.append(semiEqA)
    semiAA.append(semiEqB)

    input("\npresione ENTER para continuar\n")
        
    doble = 1
    print("**Grupo H**")
    print("Equipo       ----- Puntos -----")
    for x in range(0, 8, 2):
        print(resGH[x], " ....... ", resGH[doble])
        print(resGA[x], " ....... ", resGA[doble])
        if(int(resGA[doble]) >= semiptA):
            semiptA = int(resGA[doble])
            semiEqA = resGA[x]
        
        if(int(resGA[doble]) <= semiptA and int(resGA[doble]) > semiptB and semiEqB != semiEqA):
            semiptB = int(resGA[doble])
            semiEqB = resGA[x]
        doble += 2
    semiAA.append(semiEqA)
    semiAA.append(semiEqB)

    input("\npresione ENTER para continuar\n")

    print(semiAA)

def sub_menu():
    intento = True
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
