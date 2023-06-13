print("\n\n")
import os 
import time
#Diccionarios
basico=[{
    "nombre": "trainer",
    "grupo":"basico"
},]
intermedio=[{
    "nombre": "trainer",
    "grupo":"intermedio"
},]
avanzado=[{
    "nombre": "trainer",
    "grupo":"avanzado"
},]

#Menus
def MenuPrin():
    os.system("clear")
    print("-----------------Menu------------------\n\nSeleccione a que modulo desea ingresar\n\n1.Grupo Basico\t\t2.Grupo Intermedio\n3.Grupo Avanzado\t4.Premios\n\n")

def Vermenu(grupo):
    os.system("clear")
    print("----MANTENIMIENTO Y PREMIOS CAMPERS CAMPUS---\n---------------------------------------------")
    print("0. TERMINAR PROCESO                          \n---------------------------------------------")
    print(f"1.0 CREAR GRUPO {grupo} CON CAMPERS Y SUS DATOS PERSONALES\n1.1 REGISTRAR EXPERT TRAINER DEL GRUPO BASICO\n1.2 BUSQUEDA DE CAMPERS DUPLICADOS\n1.3 ELIMINACION DE CAMPERS POR INASISTENCIA\n1.4 LISTAR CAMPERS\n1.5 TRANSLADO DE CAMPER ENTRE GRUPOS POR NIVELACION\n1.6 AGREGAR CAMPERS AL GRUPO\n1.7 REPORTAR CAMPERS DE MAYOR Y MENOR EDAD\n\n")
  
def crearGrupo(lista):
    nombre=input("Ingrese el nombre del estudiante: ")
    mes=input("Ingrese el mes en el que ingreso el estudiante: ")
    grupo=input("Ingrese a que grupo hace parte: ")
    edad=input("Ingrese la edad del camper: ")

    lista.append({
        "nombre":nombre,
        "mes":mes,
        "grupo":grupo,
        "edad":edad
    })
    
    


MenuPrin()
opc=input()

while opc != '0':

    if opc=='1':
        Vermenu("BASICO")
        opcmenu=input()
        while opcmenu != "0":
            if opcmenu=='1':
                crearGrupo(basico)
                opcmenu=input("Desea agregar otro estudiante: 1.Si     0.No : ")
    elif opc== '2':
        Vermenu("INTERMEDIO")
    elif opc=='3':
        Vermenu("AVANZADO")
    else:opc=='4'

opc=input()














print("\n\n")