# Como leer un archivo de excel
import openpyxl

filesheet = "./Jugadores.xlsx"

# Leer el archivo
wb = openpyxl.load_workbook(filesheet)

# Fijar la hoja
hojaPlayers = wb.get_sheet_by_name('Players')