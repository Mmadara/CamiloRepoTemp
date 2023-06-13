print("\n\n")
import math 
x=int(input("Ingrese el valor del cateto adyacente: "))
y=int(input("Ingrese el valor del cateto opuesto: "))

def hipotenusa(x,y):
    hip=math.sqrt(x**2+y**2)
    print("El valor de la hipotenusa es: ",hip)

hipotenusa(x,y)
print("\n\n")
