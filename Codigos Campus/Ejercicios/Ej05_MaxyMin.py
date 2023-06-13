print("\n\n")


def MaxyMin():
    numeros=[]
    Cantidad= int(input ("Cuantos numeros desea agregar: "))
    for i in range(Cantidad):
        numeros.append(int(input("Ingrese un numero: ")))
    maximo=0
    minimo=numeros[0]    
    for i in range(Cantidad):
        if numeros[i]>maximo:
            maximo=numeros[i]
        else: 
            numeros[i]< minimo
            minimo=numeros[i]
    print(f"El numero maximo es {maximo} y el minimo es {minimo}")
MaxyMin()

print("\n\n")
