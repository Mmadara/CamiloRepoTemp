''' Elabore un programa Python para gestionar el CRUD del archivo de datos Biblioteca.json con las siguientes funcionalidades:

Mostrar en pantalla todos los libros
Crear Nuevo libro con la posibilidad de múltiples autores por Libro
Mostrar los datos de un libro consultado por título
Actualizar los datos de un libro consultado por título
Eliminar un Libro de la biblioteca'''
import json
import time
import os

with open("Biblioteca.json","r") as archivo:
        biblioteca=json.load(archivo)

def guardar():
    with open("Biblioteca.json","w") as archivo:
        json.dump(biblioteca,archivo,indent=4)

def MostrarLibros():
    os.system("cls")
    print("--------BIBLIOTECA---------")
    print("---------------------------")
    atajo=biblioteca['bookstore']['book']
    for i in range (len(atajo)):
        a=type(atajo[i]['author'])
        b=str(a)
        if b== "<class 'str'>":
            print("--------------------------")
            print("Titulo: ",atajo[i]['title']['__text'])
            print("Idioma: ",atajo[i]['title']['_lang'])
            print("Autor: ",atajo[i]['author'])
            print("Año: ",atajo[i]['year'])
            print("Precio: ",atajo[i]['price'])
            print("Categoria: ",atajo[i]['_category'])
        elif b== "<class 'list'>":
            print("--------------------------")
            print("Titulo: ",atajo[i]['title']['__text'])
            print("Idioma: ",atajo[i]['title']['_lang'])
            print("Autores: ")
            for j in atajo[i]['author']:
                print(j)
            print("Precio: ",atajo[i]['price'])
            print("Categoria: ",atajo[i]['_category'])
            

def autores():
    cantidad=int(input("Cuantos autores tiene el libro: "))
    if cantidad==1:
        autor=input("Ingrese el nombre del autor: ")
    elif cantidad>=2:
        autor=[]
        for i in range(cantidad):
            nombres=input(f"Ingrese el nombre del autor {i}: ")
            autor.append(nombres)
    return autor

def AgregarLibro():
    os.system("cls")
    print("------INGRESE LA INFORMACION DE LOS LIBROS-----")
    idioma=input("Ingrese el idioma: ")
    titulo=input("Ingrese el titulo: ")
    autor=autores()
    año=int(input("Ingrese el año: "))
    precio=float(input("Ingrese el precio: "))
    categoria=input("Ingrese la categoria: ")
    atajo=biblioteca['bookstore']['book']
    dato={
        "title": {
        "_lang": idioma,
        "__text": titulo
        },
        "author": autor,
        "year": año,
        "price": precio,
        "_category": categoria
    }
    atajo.append(dato)
    guardar()
    print("-------------LIBRO AGREGADO----------")
    time.sleep(2)

def ConsultarLibro():
    os.system("cls")
    print("------INGRESE LA INFORMACION DE LOS LIBROS-----\n")
    nombre=input("Ingrese el nombre del libro: ")
    atajo=biblioteca['bookstore']['book']
    for i in range(len(atajo)):
        if nombre in atajo[i]['title']['__text']:
            print("--------------------------")
            print("Titulo: ",atajo[i]['title']['__text'])
            print("Idioma: ",atajo[i]['title']['_lang'])
            print("Autor: ",atajo[i]['author'])
            print("Año: ",atajo[i]['year'])
            print("Precio: ",atajo[i]['price'])
            print("Categoria: ",atajo[i]['_category'])

def EliminarLibro():
    os.system("cls")
    print("\n------INGRESE LA INFORMACION DE LOS LIBROS-----\n")
    nombre=input("Ingrese el nombre del libro: ")
    atajo=biblioteca['bookstore']['book']
    for i in range(len(atajo)):
        if nombre == atajo[i]['title']['__text']:
            del atajo[i]
            print("----------LIBRO ELIMINADO-------")
            guardar()
        
def ActualizarLibro():
    os.system("cls")
    print("\n------INGRESE LA INFORMACION DE LOS LIBROS-----\n")
    nombre=input("Ingrese el nombre del libro: ")
    atajo=biblioteca['bookstore']['book']
    for i in range(len(atajo)):
        if nombre == atajo[i]['title']['__text']:
            print("Que dato desea actualizar: \n1.Titulo\n2.Idioma\n3.Autor\n4.año\n5.Precio\n6.Categoria\n")
            dato=int(input())
            if dato == 1:
                atajo[i]['title']['__text']=input("Ingrese dato correcto: ")
                guardar()
            if dato == 2:
                atajo[i]['title']['_lang']=input("Ingrese dato correcto: ")
                guardar()
            if dato == 3:
                for i in range (len(atajo)):
                    a=type(atajo[i]['author'])
                    b=str(a)
                    if b== "<class 'str'>":
                        atajo[i]['author']=input("Ingrese dato correcto: ")
                    elif b== "<class 'list'>":
                        autor=autores()
                        atajo[i]['author']=autor
                guardar()
            if dato==4:
                atajo[i]['year']=input("Ingrese dato correcto: ")
                guardar()
            if dato==5:
                atajo[i]['price']=input("Ingrese dato correcto: ")
                guardar()
            if dato==6:
                atajo[i]['_category']=input("Ingrese dato correcto: ")
                guardar()
    print("------------INFORMACION ACTUALIZADA----------------")

opcmenu=True

while opcmenu:
    os.system("cls")
    print("--------BIBLIOTECA---------")
    print("---------------------------")
    print("\n1.Agregar\t2.Mostrar\t3.Buscar\n4.Actualizar\t5.Eliminar\t6.Salir\t")
    opcion=int(input("\nIntroduzca la opcion: "))
    if opcion==1:
        AgregarLibro()
    if opcion==2:
        print("---------LIBROS---------")
        MostrarLibros()
        time.sleep(10)
    if opcion==3:
        ConsultarLibro()
        time.sleep(5)
    if opcion==4:
        ActualizarLibro()
        time.sleep(2)
    if opcion==5:
        EliminarLibro()
        time.sleep(2)
    if opcion==6:
        opcmenu=False








        




