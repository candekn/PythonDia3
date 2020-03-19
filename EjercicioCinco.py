from openpyxl import Workbook #importa la libreria para trbajar con planillas excel


wb = Workbook() #crea un nuevo archivo excel y lo asigna en wb
ws = wb.active #a ws le asignamos la hoja activa del wb
ws["A1"] = 10 #en A1 guardamos el valor 10
wb.save("balance.xlsx") #guardamos el workbook (excel) con el nombre "balance.xlsx"