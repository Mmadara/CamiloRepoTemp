print ("\n\n")

numeros=[]
par=[]
impar=[]
for i in range (10):
    datos=int(input(f"Ingrese el numero {i+1}: "))
    numeros.append(datos)
  
print(numeros,"\n")
print("Numeros en posiciones pares: ",numeros[0::2])
print("Numeros en posiciones impares: ",numeros[1::2])
print("Primer elemento: ",numeros[0])
print("Ultimo elemento: ",numeros[-1])
print("Lista invertida: ",numeros[::-1])
for i in numeros:
    if i%2==0:
        par.append(i)
    elif i%2!=0:
        impar.append(i)

print(par)
print(impar)
    
print ("\n\n")
