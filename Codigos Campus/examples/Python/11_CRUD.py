import os
Empresa={
    "personas":[
    {
    'id':1,
    'nombre':'pedro',
    'edad':20,
    'numdoc':123456789
    }
    ,
    {
    'id':2,
    'nombre':'ofelia',
    'edad':30,
    'numdoc':123456789
    },
    {
    'id':3,
    'nombre':'Ruthy',
    'edad':17,
    'numdoc':123456789
    }]
}
def limpiar():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def Crear(lista):
    id=int(input("Ingrese el ID del cliente: "))
    nombre=input("Ingrese el nombre del cliente: ")
    edad=int(input("Ingrese la edad del cliente: "))
    numdoc=int(input("Ingrese el numero de documento del cliente: "))
    lista['personas'].append({'id':id,'nombre':nombre,'edad':edad,'numdoc':numdoc})

def Leer(lista):
    print('-------------LISTA----------------')
    print('id','nombre\t','edad\t','Documento')
    print('----------------------------------')
    for i in lista['personas']:
        print(i['id'],i['nombre'],"\t",i['edad'],"\t",i['numdoc'])

def Actualizar(lista):
    print('\n--------QUE DATO VA A MODIFICAR------')
    print('   1.Id\n   2.Nombre\n   3.Edad\n   4.Numero de documento\n')
    dato= input("Ingrese el dato a modificar: ")
    nombre=input("Ingrese el nombre del cliente a modificar: ")
    for i in range(len(lista['personas'])):
        if nombre==lista['personas'][i]['nombre']:
            if dato=='1':
                lista['personas'][i]['id']=input("Digite el dato correcto: ")
                break
            elif dato=='2':
                lista['personas'][i]['nombre']=input("Digite el dato correcto: ")
                break
            elif dato=='3':
                lista['personas'][i]['edad']=input("Digite el dato correcto: ")
                break
            elif dato=='4':
                lista['personas'][i]['numdoc']=input("Digite el dato correcto: ")
                break
        else:
            print("El cliente no existe")
            break

def BorrarClientes(lista):
    print("-------------CLIENTES-------------")
    print("----------------------------------")
    for i in lista['personas']:
        print(i['id'],i['nombre'],"\t",i['edad'],"\t",i['numdoc'])

    nombre=input("Ingrese el nombre del cliente a eliminar: ")
    for i in range(len(lista['personas'])):
        if nombre==lista['personas'][i]['nombre']:
            Empresa['personas'].pop(i)
            print("-------Cliente Eliminado--------")
            break

    

