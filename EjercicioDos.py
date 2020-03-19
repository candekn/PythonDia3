
"""
Los archivos se crean en el mismo directorio que el archivo .py
w: Modo Write: escritura. Si el archivo no existe lo crea, si existe lo sobreescribe
r: Modo Read: lectura
a: Modo Append: Agrega nuevas cosas sin sobreescribirlo. No lee
a+: Modo Append binario. Sobreescribe y lee

"""
f = open("archivo.txt","w") #Abre el archivo (o lo crea si no existe)
f.write("Escribe lo que va dentro del archivo")
f.close() #Guarda y cierra el archivo
r = open("archivo.txt","r")
texto = r.read() #guarda lo q esta dentro del archivo y lo almacena en la variable read
print(texto)
r.close()

a = open("archivo.txt","a") 
a.write(" y esto es un nuevo texto") #con modo "a", no sobreescribe lo escrito, solo lo agrega a lo ya escrito antes
a.close()
textoNuevo = open("archivo.txt","r").read()
print (textoNuevo)
