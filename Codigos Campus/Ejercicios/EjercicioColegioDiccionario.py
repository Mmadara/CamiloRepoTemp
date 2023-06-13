import os
import time
print("\n\n")
opc = ''
opcMenu = ''
dicEstudiantes={
    1:{
        'nombres':'Jose Luis',
        'apellidos':'Gomez Trillos',
        'correo':'jose@cole.edu'
    },2:{
        'nombres':'Daniela',
        'apellidos':'Forero Hernandez',
        'correo':'danieña@cole.edu'
    },3:{
        'nombres':'Santiago',
        'apellidos':'Figueroa Peña',
        'correo':'santiago@cole.edu'
    },   
}
dicMateria={
    1:{
        "nomMateria":"Matemáticas"
    },
    2:{
        "nomMateria":"Lenguaje"
    },
    3:{
        "nomMateria":"Química"
    },
    4:{
        "nomMateria":"Física"
    }
}
dicNotas={
}
def verMenu():
    os.system('clear')
    print('********************** COLEGIO **********************')
    print('Seleccione alguna de las siguientes opciones:\n\t1. Notas\t\t2. Estudiantes\n\t3. Materias\t\t0. Salir')
#materias    
def verMenuMaterias(materias):
    os.system('clear')
    print('********************** MATERIAS **********************')
    print(verMaterias(materias))
    verMaterias(materias)
    print('Seleccione alguna de las siguientes opciones:\n\t1. Agregar\t\t2. Editar\n\t3. Eliminar\t\t4. Volver')

def crearID(diccionario):
    id=list(diccionario.keys())[len(diccionario)-1]
    return (id)

def agregarMaterias(materias,nombreMateria):
    id = crearID(materias)
    materias[id]={
        "nomMateria":nombreMateria
    }
    return materias

def verMaterias(materias):
    listaMaterias = "\nCODIGO\tMATERIA\n"
    for materia in materias:
        listaMaterias += str(materia) +"\t" + materias[materia]['nomMateria']+'\n'
    return listaMaterias
#Estudiantes
def agregarEstudiantes(estudiante,nombre,apellido,correo):
    id=crearID(estudiante)

    estudiante[id+1]={
        'nombres':nombre,
        "apellidos":apellido,
        "correo":correo
    }
    return estudiante

def verEstudiante(estudiantes):
    listaEstudiantes="\nCODIGO\tNOMBRES\t\tAPELLIDOS\t\tCORREOS\n"
    for estudiante in estudiantes:
        listaEstudiantes+=str(estudiante)+"\t"+str(estudiantes[estudiante]['nombres'])+"\t"+str(estudiantes[estudiante]['apellidos'])+"\t"+str(estudiantes[estudiante]['correo'])+"\n"
    return listaEstudiantes

def verMenuEstudiantes(estudiantes):
    os.system('clear')
    print('********************** ESTUDIANTES **********************')
    print(verEstudiante(dicEstudiantes))
    print('Seleccione alguna de las siguientes opciones:\n\t1. Agregar\t\t2. Editar\n\t3. Eliminar\t\t4. Volver')


verMenu()

opcMenu = input()
while opcMenu != '0':
    if opcMenu == '1':
        print()
    elif opcMenu == '2':
        verMenuEstudiantes(dicEstudiantes)
        opc=input()
        while opc != '0':
            if opc == '1':
                print('********************** AGREGAR **********************')
                nombre= input('Ingrese el nombre del estudiante: ')
                apellido=input('Ingrese el apellido del estudiante: ')
                correo=input('Ingrese el correo del estudiante: ')
                agregarEstudiantes(dicEstudiantes,nombre,apellido,correo)
                print('************** ESTUDIANTE AGREGADO **************')
                time.sleep(3)
            elif opc == '2':
                print('********************** EDITAR **********************')
                codigo= int(input('Ingrese el código del estudiante: '))
                print('Ingrese el nombre correcto:')
                dicEstudiantes[codigo]['nombres']=input()
                print('Ingrese el apellido correcto:')
                dicEstudiantes[codigo]['apellidos']=input()
                print('Ingrese el correo correcto:')
                dicEstudiantes[codigo]['correo']=input()
                print('************** ESTUDIANTE ACTUALIZADO **************')
                time.sleep(3)
            elif opc == '3':
                print('********************** ELIMINAR **********************')
                codigo= int(input('Ingrese el código del estudiante: '))
                del(dicEstudiantes[codigo])
                print('************** ESTUDIANTE ELIMINADO **************')
                time.sleep(3)
            elif opc == '4':
                verMenu()
                opcMenu=input()
            else:
                print('\nPor favor seleccione una opción válida.')
                time.sleep(3)
            verMenuEstudiantes(dicEstudiantes)
            opc = input() 
    elif opcMenu == '3':
        verMenuMaterias(dicMateria)
        opc=input()
        while opc != '0':
            if opc == '1':
                print('********************** AGREGAR **********************')
                nombre= input('Ingrese el nombre de la materia: ')
                dicMateria = (dicMateria,nombre)
                print('************** MATERIA AGREGADA **************')
                time.sleep(3)
            elif opc == '2':
                print('********************** EDITAR **********************')
                codigo= int(input('Ingrese el código de la materia: '))
                print('Ingrese el nuevo nombre de la materia:')
                dicMateria[codigo]['nomMateria']=input()
                print('************** MATERIA ACTUALIZADA **************')
                time.sleep(3)
            elif opc == '3':
                print('********************** ELIMINAR **********************')
                codigo= int(input('Ingrese el código de la materia: '))
                del(dicMateria[codigo])
                print('************** MATERIA ELIMINADA **************')
                time.sleep(3)
            elif opc == '4':
                verMenu()
                opcMenu=input()
            else:
                print('\nPor favor seleccione una opción válida.')
                time.sleep(3)
            verMenuMaterias(dicMateria)
            opc = input() 
    else:
        verMenu()
        opc = input()
print("\n\n")