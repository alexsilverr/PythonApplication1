
fac = False
	
	
	

cantidad1,cantidad2,cantidad3,cantidad4=0,0,0,0		
cocacola,medialunas,milanesa,pollo_frito = 0, 0, 0, 0
total_cocacola,total_medialunas,total_milanesa,total_pollo= 0, 0, 0, 0


	
while fac is False:
	print("             MENU                      ")
	print("      PRODUCTO      PRECIO             ")
	print("  [1] Cocacola        20               ")
	print("  [2] Medialuna       30               ")
	print("  [3] Milanesa        50               ")
	print("  [4] Pollo frito     70               ")
	print("                                       ")
	print("        [5] para salir                 ")
	print("                                       ")
	print("             MENU                      ")
	
	option=int(input())
	
	print("La opcion seleccionada es: ",option)
	
	if option == 1:
		print("cocacola")
		cocacola= 20
		cantidad1 = int(input("cuantos productos quieres: "))
		total_cocacola = cocacola * cantidad1
		print (" El precio total del producto es :",total_cocacola)
	
	if option == 2:
		print("medialunas")
		medialunas = 30
		cantidad2 = int(input("cuantos productos quieres: "))
		total_medialunas = medialunas * cantidad2
		print("El precio total del producto es :",total_medialunas)
	
	if option == 3:
		print("milanesa")
		milanesa=50
		cantidad3 = int(input("cuantos productos quieres: "))
		total_milanesa = milanesa * cantidad3
		print("El precio total del producto es:",milanesa)
			
	if option == 4:
		print("pollo frito")
		pollo_frito=70
		cantidad4 = int(input("cuantos productos quieres: "))
		total_pollo = pollo_frito * cantidad4
		print("El precio total del producto es:",total_pollo)
		
	if option ==5:
		print ("se va imprimir tu factura gracias por su compra")
		fac = True
		
		resultado = total_cocacola+total_medialunas+total_milanesa+total_pollo


cantidades=cantidad1+cantidad2+cantidad3,cantidad4
print ("escriba su nombre:")	
nombre=input()
print ("escriba su apellido:")
apellido=input()
print ("escriba su DNI:")
dni=input()


impuesto = resultado * 20
subtotal = impuesto /100
total= subtotal+resultado

print("\nEl total de su compra",nombre,"es:",total,"puede revisar su factura")
factura = open("factura.txt", "w")
factura.write("----------------FACTURA----------------")
factura.write("\nDatos del cliente")
factura.write("\nNombre: "+nombre)
factura.write("\nApellido: "+apellido)
factura.write("\nDNI: "+dni)
factura.write("\n-------------------------------------")
factura.write("\nArticulos     Precio    Cantidad  Total")
lineaCoca = "Cocacola        $20         "+str(cantidad1)+"       "+str(total_cocacola)
factura.write('\n'+lineaCoca)
lineaMedialuna = "Medialuna       $30         " + \
str(cantidad2)+"       "+str(total_medialunas)
factura.write('\n'+lineaMedialuna)
lineaMilanesa = "Milanesa        $50         " + \
str(cantidad3)+"       "+str(total_milanesa)
factura.write('\n'+lineaMilanesa)
lineaPollo = "Pollo Frito     $70         "+str(cantidad4)+"       "+str(total_pollo)
factura.write('\n'+lineaPollo)
factura.write("\n-------------------------------------")
factura.write("\n20% mas ---------------------------$"+str(subtotal))
factura.write("\n---------------------------------------")
factura.write("\nTotal a pagar---------------------$"+str(total))
