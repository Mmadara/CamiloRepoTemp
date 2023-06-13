print("\n\n")
import time
import os

pacientes= []

def VerMenu():
    os.system("clear")
    print("-------------IPS---------------")
    print("-------------------------------")
    print("Que deseas realizar: ")
    print("1.Agregar Pacientes\n2.Mostrar pacientes\n3.Editar pacientes\n4.Borrar pacientes\n5.Salir")
    
def AddPacientes(lista):
    os.system("clear")
    print("Ingrese los datos del paciente: ")
    nombre=input("Nombre y apellido del paciente: ")
    codigo=int(input("Codigo del paciente: "))
    edad=int(input("Edad del paciente: "))
    peso=int(input("Peso del paciente: "))
    sexo=input("Genero del paciente: ")
    lista.append({1:codigo,2:nombre,3:edad,4:peso,5:sexo})

def EditarPacientes(lista):
    codigo=int(input("Digite el codigo del paciente que desea editar: "))
    cambio=int(input("Que dato desea cambiar: \n1.Codigo\n2.Nombre\n3.Edad\n4.peso\n5.sexo\n"))
    for i in range(len(lista)):
        if lista[i][1]==codigo:
            lista[i][cambio]=input("Ingrese la informacion correcta: ")
            print("-------DATO MODIFICADO-----")
            time.sleep(2)

def VerPacientes(lista):
    os.system("clear")
    print("-----------------Pacientes-----------------")
    print("-------------------------------------------")
    print("Codigo\tNombre\t\tEdad\tPeso\tSexo")
    for i in range(len(lista)):
        print(f"{lista[i][1]}\t{lista[i][2]}\t{lista[i][3]}\t{lista[i][4]}\t{lista[i][5]}")
    time.sleep(10)

def BorrarPacientes(lista):
    os.system("clear")
    print("-----------------Pacientes-----------------")
    print("-------------------------------------------")
    print("Codigo\tNombre\t\tEdad\tPeso\tSexo\n")
    for i in range(len(lista)):
        print(f"{lista[i][1]}\t{lista[i][2]}\t{lista[i][3]}\t{lista[i][4]}\t{lista[i][5]}")
    codigo=int(input("Digite el codigo del paciente que desea eliminar: "))
    for i in range(len(lista)):
        if lista[i][1]==codigo:
            lista.pop(i)
            print("-------Paciente Eliminado-------")
            time.sleep(1)
            break


menu=True

while menu:
    VerMenu()
    opcion=int(input("\nDigite la opcion que desea realizar: "))
    if opcion==1:
        AddPacientes(pacientes)
    elif opcion==2:
        VerPacientes(pacientes)
    elif opcion==3:
        EditarPacientes(pacientes)
    elif opcion==4:
        BorrarPacientes(pacientes)
    elif opcion==5:
        menu=False

