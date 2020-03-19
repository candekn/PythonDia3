import tkinter as tk

def sumar():
	cajatres.delete(0,tk.END)
	a = cajauno.get()
	b = cajados.get()
	a = float(a)
	b = float(b)
	c = a + b
	cajatres.insert(0,c) #0 para elegir la posición donde muestre el resultado

def restar():
	cajatres.delete(0,tk.END)
	a = cajauno.get()
	b = cajados.get()
	a = float(a)
	b = float(b)
	c = a - b
	cajatres.insert(0,c)

def mult():
	cajatres.delete(0,tk.END)
	a = cajauno.get()
	b = cajados.get()
	a = float(a)
	b = float(b)
	c = a * b
	cajatres.insert(0,c)

def div():
	cajatres.delete(0,tk.END)
	a = cajauno.get()
	b = cajados.get()
	a = float(a)
	b = float(b)
	if b == 0:
		cajatres.insert(0,"Error. No se puede dividir por cero.")
	else:
		c = a / b
		cajatres.insert(0,c)

ventana = tk.Tk() #Tk() crea una ventana nueva
ventana.title("App") #le asigna nombre a la ventana
ventana.config(height=400, width=400) #le da un tamaño predeterminado
botonsuma = tk.Button(text=" + ", command = sumar) #crea un boton con ese texto
botonsuma.place(x=100, y=100)
botonrestar = tk.Button(text=" - ", command = restar)
botonrestar.place(x=150, y=100)
botonmult = tk.Button(text=" * ", command = mult)
botonmult.place(x=200, y=100)
botondiv = tk.Button(text=" / ", command = div)
botondiv.place(x=250, y=100)
cajauno = tk.Entry()
cajauno.place(x=50, y=50)
cajados = tk.Entry()
cajados.place(x=200, y=50)
cajatres = tk.Entry()
cajatres.place(x=120, y=150)
ventana.mainloop()