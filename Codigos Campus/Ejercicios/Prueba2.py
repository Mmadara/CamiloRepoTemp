print("\n\n")
import math
otro="s"
def numerosprimos(): 
    numero=int(input("Ingrese el numero a verificar: "))
    for i in range(2,numero):
        if (numero%i) == 0:
            print(False) 
        else:
            print(True) 
def areadefiguras():
    operacion = int(input("Que area desea calcular \n 1. Circulo 2. Triangulo 3. Cuadrado\n"))
    if operacion == 1:
        radio= int(input("Ingrese el radio del circulo: "))
        circulo= (radio**2)*math.pi
        print("El area del circulo es: ", circulo)
    elif operacion == 2:
        base= int(input("Ingrese la base del triangulo: "))
        altura= int(input("Ingrese la altura del triangulo: "))
        triangulo=(base*altura)/2
        print("El area del triangulo es: ", triangulo)
    else:
        operacion == 3 
        lado= int(input("Ingrese cuanto vale el lado del cuadrado: "))
        cuadrado= lado*lado
        print("El area del cuadrado es: ", cuadrado) 
def factorial():
    fact =1
    numero=int(input("Ingrese el numero a verificar: "))
    if numero==0 and numero==1:
        print("El factorial es: 1") 
    while numero > 0:
        fact= fact * numero
        numero-=1
    print ("El factorial es: ",fact) 
def cambiomonedas():
    precio=int(input("Cuantos pesos colombianos desea convertir: "))
    valor=input("Introduzca la moneda a la que desea cambiar:\n1.Dolares\n2.Yenes\n3.Libras\n")
    if valor == "1":
        total= precio/4758
        print("Su cambio es: ",total)
    elif valor == "2":
        total= precio/36.36
        print("Su cambio es: ",total)
    elif valor == "3" :
        total= precio/5845.04
        print(" Su  cambio es: ",total )        
def cuadratica(): 
    a=int(input("Ingrese el valor para 'a' : "))
    b=int(input("Ingrese el valor para 'b' : "))
    c=int(input("Ingrese el valor para 'c' : "))
    raiz= (b**2)-4*a*c
    if raiz < 0:
        print("Los resultados son numeros imaginarios")
    else:
        x1 = (-b + math.sqrt(raiz))/2*a
        x2 = (-b - math.sqrt(raiz))/2*a
        print(f"Los valores son x1:{x1} y x2: {x2}")
while otro=="s":
    programa=input("\nSeleccione el programa que desea ejecutar:\n1.Calcular el area de figuras.\n2.Calcular cuando un número es primo.\n3.Calcular el factorial de un número.\n4.Cambio de divisas.\n5.Solucionar una función cuadratica.\n")
    if programa=="1":
        areadefiguras()
        otro= input("\nDesea ejecutar otro programa: s/n\n")
    elif programa=="2":
        numerosprimos()
    elif programa =="3":
        factorial()
    elif programa == "4":
        cambiomonedas()
    elif programa=="5":
        cuadratica()
print("\n\n")
