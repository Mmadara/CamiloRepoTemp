import os
import json
'************Funcion para crear id en los diccionarios************'
def crearID(diccionario):
    id=list(diccionario.keys())[len(diccionario)-1]
    return (id)

'****************Funciones para las materias**********************'
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

def verMenuMaterias(materias):
    os.system('clear')
    print('********************** MATERIAS **********************')
    print(verMaterias(materias))
    print('Seleccione alguna de las siguientes opciones:\n\t1. Agregar\t\t2. Editar\n\t3. Eliminar\t\t4. Volver')

'****************Funciones para los estudiantes****************'

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
    print(verEstudiante(estudiantes))
    print('Seleccione alguna de las siguientes opciones:\n\t1. Agregar\t\t2. Editar\n\t3. Eliminar\t\t4. Volver')

'****************Funciones para las notas*******************'

def agregarNotas(notas,idEstudiante,idMateria,nota1,nota2,nota3,notaf):

    id=crearID(notas)
    notas[id+1]={
    "idEstudiante":idEstudiante,
    "idMateria":idMateria,
    "nota1":nota1,
    "nota2":nota2,
    "nota3":nota3,
    "notaf":notaf
    }
    return notas



def verNotas(notas,estudiantes,materias):#Estudiantes=dicEstudiantes_notas=dicNotas_materias=dicMaterias
    listaNotas="\nCODIGO\tNOMBRE\t\tAPELLIDO\tMATERIA\t\tNOTA1\tNOTA2\tNOTA3\tNOTA FINAL\n"
    for nota in notas:
        nombre=str(estudiantes[notas[nota]['idEstudiante']]['nombres'])+"\t"+str(estudiantes[notas[nota]['idEstudiante']]['apellidos'])
        listaNotas+=str(nota)+"\t"+ nombre +"\t"+str(materias[notas[nota]['idMateria']]['nomMateria'])+"\t"+str(notas[nota]['nota1'])+"\t"+str(notas[nota]['nota2'])\
            +"\t"+str(notas[nota]['nota3'])+"\t"+str(notas[nota]['notaf'])+"\n"
    return listaNotas

def verMenuNotas(estudiantes,materias,notas):
    os.system('clear')
    print('********************** ESTUDIANTES **********************')
    print(verEstudiante(estudiantes))
    print('********************** MATERIAS **********************')
    print(verMaterias(materias))
    print('*******notas*************')
    print(verNotas(notas),"\n")
    print('**************************************************************************************************\n')
    print('Seleccione alguna de las siguientes opciones:\n\t1. Agregar\t\t2. Editar\n\t3. Eliminar\t\t4. Volver\n')


'************Funciones para json**************'
def crearjson(diccionario):
    with open ("estudiantes.json","w") as archivo:
        json.dump(diccionario,archivo)
    archivo.close()
