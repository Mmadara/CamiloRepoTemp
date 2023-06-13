print("\n\n\n")
print("Lista de compras\n")
opcion = input ("¿Desea crear una lista de compras o calcular el total de ventas? \n 1.Compras\n 2.Ventas\n ")
otro="S"
indice =0
lista = ""
costo = 0
total = 0


while otro == "S" or otro == "s":
   if opcion == "1" :
      lista += "\n" + input("Ingrese un elemento a la lista: ")
      costo =int(input("Ingrese su valor: $"))
      lista += "\t\t\t $" + str(costo);
      total += costo;
      indice += 1
      otro = input("¿Desea agregar otro elemento ? s/n\n") 
     

print("Su lista es la siguiente: \n\nPRODUCTOS\t\tCOSTO\n\n"+lista)
print("\n"+ str(indice)+"TOTAL: $"+str(total))
print("\n\n\n")        


