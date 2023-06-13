print("\n\n")
precio=int(input("Ingrese el valor a pagar: "))

def neto(precio):
    if precio>100000:
        neto=precio-precio*0.12
        print("El precio neto a pagar es: ",neto)
    else:
        neto=precio-precio*0.06
        print("El precio neto a pagar es: ",neto)
        
neto(precio)
print("\n\n")
