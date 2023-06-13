print("\n\n")
precio=int(input("Ingrese el precio del producto: "))

def iva(precio):
    neto=precio+precio*0.19
    print("El precio neto es: ",neto)

iva(precio)

print("\n\n")