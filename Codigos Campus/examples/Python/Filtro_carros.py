'''Elabore un programa Python para gestionar el CRUD del archivo de datos AutoShopping.json con las siguientes funcionalidades:

1. Mostrar en pantalla todos los automóviles a la venta Mostrando: Marca, Línea, Modelo, Precio y Equipamento
2. Crear Nuevo Auto con la posibilidad de múltiples ítems de Equipamento
3. Mostrar los datos de Autos consultado por Marca Mostrando: Línea, Modelo, Precio y Equipamento
4. Actualizar los datos de un Auto consultado por índice (Mostrar el listado total y elegir por índice)
5. Eliminar un Auto de la tienda (Mostrar el listado total y elegir por índice)'''

import json
import time
import os

with open("AutoShopping.json","r") as archivo:
        Autoshopping=json.load(archivo)

def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

Ruta=Autoshopping["autostore"]["auto"]

def guardar():
    with open("AutoShopping.json","w") as archivo:
        json.dump(Autoshopping,archivo,indent=4)

def MostrarCarros():
    borrarPantalla()
    print("---------AUTOSHOPPING------------")
    print("---------------------------------")
    for i in range (len(Ruta)):
        a=type(Ruta[i]['equipamiento'])
        b=str(a)
        if b== "<class 'str'>":
            print("\n-------------------------------")
            print("Carro Numero: ",i+1)
            print("Marca: ",Ruta[i]['marca'])
            print("Linea: ",Ruta[i]['linea'] )
            print("Modelo: ",Ruta[i]['modelo'])
            print("Precio: ",Ruta[i]['precio'] )
            print("Equipamiento: ",Ruta[i]['equipamiento'])
        elif b== "<class 'list'>":
            print("\n-------------------------------")
            print("Carro Numero: ",i+1)
            print("Marca: ",Ruta[i]['marca'])
            print("Linea: ",Ruta[i]['linea'] )
            print("Modelo: ",Ruta[i]['modelo'])
            print("Precio: ",Ruta[i]['precio'] )
            print("Equipamiento: ")
            for j in Ruta[i]['equipamiento']:
                print(j)

def Equipamientos():
    cantidad=int(input("Seleccione de las siguientes opciones:\n1.Full equipo o sin equipo adicional\n2.Multiple equipamiento\n"))
    if cantidad==1:
        equipamiento=input("Ingrese el tipo de equipamiento: ")
    elif cantidad>1:
        numero=int(input("Cuantos equipamientos adicionales tiene: "))
        equipamiento=[]
        for i in range(numero):
            nombres=input(f"Ingrese el equipamiento #{i+1}: ")
            equipamiento.append(nombres)
    return equipamiento

def AgregarCarros():
    borrarPantalla()
    print("------INGRESE LA INFORMACION DEL VEHICULO-----")
    marca=input("Ingrese la marca del vehiculo: ")
    linea=input("Ingrese la linea del vehiculo: ")
    modelo=input("Ingrese el año: ")
    precio=input("Ingrese el precio: ")
    equipamiento=Equipamientos()
    dato={
        "marca":marca,
        "linea": linea,
        "modelo": modelo,
        "precio": precio,
        "equipamiento": equipamiento
    }
    Ruta.append(dato)
    guardar()
    print("-------------VEHICULO AGREGADO----------")
    time.sleep(2)

def ConsultarCarro():
    borrarPantalla()
    print("\n------INGRESE LA INFORMACION DEL VEHICULO-----\n")
    nombre=input("Ingrese la marca del vehiculo: ")
    for i in range(len(Ruta)):
        if nombre in Ruta[i]['marca']:
            a=type(Ruta[i]['equipamiento'])
            b=str(a)
            if b== "<class 'str'>":
                print("\n------------------------------------")
                print("Marca: ",Ruta[i]['marca'])
                print("Linea: ",Ruta[i]['linea'] )
                print("Modelo: ",Ruta[i]['modelo'])
                print("Precio: ",Ruta[i]['precio'] )
                print("Equipamiento: ",Ruta[i]['equipamiento'])
            elif b== "<class 'list'>":
                print("\n------------------------------------")
                print("Marca: ",Ruta[i]['marca'])
                print("Linea: ",Ruta[i]['linea'] )
                print("Modelo: ",Ruta[i]['modelo'])
                print("Precio: ",Ruta[i]['precio'] )
                print("Equipamiento: ")
                for j in Ruta[i]['equipamiento']:
                    print(j)
    print("\n")
    input("Presione Enter para continuar: ")

def ActualizarInformacion():
    borrarPantalla()
    print("\n------INGRESE LA INFORMACION DEL VEHICULO-----\n")
    MostrarCarros()
    indice=int(input("\nIngrese el numero del vehiculo que desea actualizar: "))
    for i in range(len(Ruta)):
        if (indice-1) == i :
            print("\nQue dato desea actualizar: \n1.Marca\n2.Linea\n3.Modelo\n4.Precio\n5.Equipamiento\n")
            dato=int(input())
            if dato == 1:
                Ruta[i]['marca']=input("Ingrese dato correcto: ")
                guardar()
            elif dato == 2:
                Ruta[i]['linea']=input("Ingrese dato correcto: ")
                guardar()
            elif dato==3:
                Ruta[i]['modelo']=input("Ingrese dato correcto: ")
                guardar()
            elif dato==4:
                Ruta[i]['precio']=input("Ingrese dato correcto: ")
                guardar()
            elif dato == 5:
                for j in range (len(Ruta)):
                    a=type(Ruta[i]['equipamiento'])
                    b=str(a)
                    if b == "<class 'str'>":
                        Ruta[i]['equipamiento']=input("Ingrese dato correcto: ")
                        break
                    elif b == "<class 'list'>":
                        equipamiento=Equipamientos()
                        Ruta[i]['equipamiento']= equipamiento
                guardar()
    print("-------------INFORMACION ACTUALIZADA----------------")

def EliminarCarro():
    borrarPantalla()
    print("\n------INGRESE LA INFORMACION DEL VEHICULO-----\n")
    MostrarCarros()
    indice=int(input("\nIngrese el indice del vehiculo: "))
    for i in range(len(Ruta)):
        if (indice-1) == i:
            del Ruta[i]
            print("----------VEHICULO ELIMINADO-------")
            guardar()

opcmenu=True

while opcmenu:
    borrarPantalla()
    print("--------------AUTOSTORE------------------")
    print("-----------------------------------------")
    print("\n1.Agregar\t2.Mostrar\t3.Buscar\n4.Actualizar\t5.Eliminar\t6.Salir\t")
    opcion=int(input("\nIntroduzca la opcion: "))
    if opcion==1:
        AgregarCarros()
    if opcion==2:
        MostrarCarros()
        input("\nPresione Enter para continuar")
    if opcion==3:
        ConsultarCarro()
    if opcion==4:
        ActualizarInformacion()
        time.sleep(2)
    if opcion==5:
        EliminarCarro()
        time.sleep(2)
    if opcion==6:
        opcmenu=False

