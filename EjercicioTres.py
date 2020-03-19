i = 1
print("Hola, esto es un programa")

while i<=20:
    f = open("C://Users//candelaria.d//Documents//Python//Python Clase 3//Pedidos//pedido_numero "+str(i)+".txt","w")
    f.write(str(i))
    f.close()
    i=i+1