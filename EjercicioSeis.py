from openpyxl import Workbook

c = ["Nombre","Edad","Telefono"]
persona1 = ["Carlos","30","11234234"]
wb = Workbook()
ws = wb.active
ws.append(c)
ws.append(persona1)
wb.save("personas.xlsx")