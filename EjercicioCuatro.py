personas = []

while True:
	nombre = input("Ingrese nombre: ")
	edad = input ("Ingrese la edad: ")
	personas.append([nombre,edad])
	op = input("Desea continuar: Y/N ")
	if op == "n":
		break
#ME LOS GUARDA EN users/candelaria.d WTF?????
f = open("personas.txt", "w")

for n in personas:
	f.write(str(n))

f.close()

f = open("personas.txt","r")
d = f.read()
f.close

print(d)