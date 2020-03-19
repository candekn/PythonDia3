from openpyxl import load_workbook

wb = load_workbook(filename="personas.xlsx") #cargame el libro llamado personas.xlsx y asignalo a la variable wb

hoja = wb['Sheet'] #asignamos en la variable hoja, la hoja que se llama asi: 'Sheet'
print(hoja['A2'].value) #mostramos por consola el valor que esta en esa hoja y esa celda
i=2

while i<6:
    if hoja["C"+str(i)].value>=55000:
        print("\nNombre: "+hoja["A"+str(i)].value)
        print("Sueldo: "+str(hoja["C"+str(i)].value)) 
    i=i+1

