import json
with open("Pasaporte.json","r") as archivo:
        Pasaporte=json.load(archivo)
        
def Guardar():
    with open("Pasaporte.json","w") as archivo:
        json.dump(Pasaporte,archivo,indent=4)
    
def AgregarCita():
    print("------------BIENVENIDO----------")
    dia=input("Ingrese el dia de la cita: ")
    mes=input("Ingrese el mes de la cita: ")
    hora=input("Ingrese la  hora de la cita")
    FechaPago=input("Ingrese la fecha de pago: ")
    tipo=input("¿Cita de emergencia?: Si/No")
    dato={
        "dia":dia,
        "mes":mes,
        "hora":hora,
        "pago":{
            "fecha":FechaPago
        },
        "emergencia":tipo
    }
    Pasaporte['Pasaportes']['citas'].append(dato)
    Guardar()
    
AgregarCita()