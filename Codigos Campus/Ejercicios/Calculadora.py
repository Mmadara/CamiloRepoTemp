print("\n\n")
numero1= float(input("Ingrese los numeros que desea operar: "))
numero2= float(input("Ingrese los numeros que desea operar: "))
operacion= int (input("Que operacion desea realizar: \n1.Suma \n2.Resta \n3.Multiplicacion \n4.Division\n"))
otro = "S"
suma=0
resta=0
multi=0
div=0

while otro == "S" or otro == "s" :
    if operacion == 1:
        print("\nEl resultado es: ",numero1+numero2)
        suma += 1
    elif operacion == 2 :
        print("\nEl resultado es: ",numero1-numero2)
        resta +=1
    elif operacion== 3 :
        print("\nEl resultado es: ",numero1*numero2)      
        multi +=1
    elif operacion== 4 :
        print("\nEl resultado es: ",numero1/numero2)     
        div+=1
        
    otro=input("¿Desea hacer otra operacion? s/n\n")

        
    