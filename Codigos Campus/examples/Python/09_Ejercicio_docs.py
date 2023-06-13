'''1. Elabore un Programa Python que lea la ruta y nombre de un archivo y muestre por pantalla la línea M del archivo.
La línea a mostrar también debe ser un dato ingresado por el usuario del programa.
Si el archivo no existe debe mostrar un mensaje por pantalla informando de ello.'''

import io 

def VerLinea():
    linea=int(input("Que linea desea observar: "))-1
    texto=open("tigre.txt","r")
    a= texto.readlines()
    print(a[linea])
    texto.close()
# VerLinea()

'''2. Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa.
El programa debe incorporar funciones para: 1. crear el archivo si este no existe, 2. para consultar el teléfono de un cliente, 
3. añadir el teléfono de un nuevo cliente y 4. eliminar el teléfono de un cliente. El listado debe estar guardado en el archivo de texto Directorio.txt 
donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.'''

import io
import os 

def CrearArchivo():
    nombre=input("Como se desea llamar el documento: ")
    try :
        archivo=open(f"{nombre}.txt","x")
        archivo.close()
    except:
        print("El documento ya existe")


def agregarCliente(nombre):
    cliente= input("Agregue la informacion del cliente: ")
    telefono=input("Agregue el numero del cliente: ")
    with open(f"{nombre}.txt","a+") as archivo:
        archivo.write((cliente)+",")
        archivo.write((telefono)+"\n")



def ConsultarCliente(nombre):
    cliente= input("Ingrese el cliente que desea buscar: ")
    texto=open(f"{nombre}.txt","r")
    b=texto.readlines()
    print(b.index(cliente))
    
        
        

    



ConsultarCliente("prueba")