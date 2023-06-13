import json
#lista
lista=[10,20,30,40,60]

with open ("lista.json","w") as archivo:
    json.dump(lista,archivo)

archivo.close()

#diccionario

diccionario={'1':'lapiz','2':'borrador','3':'cuaderno','4':'lapicero'}

with open("diccionario.json","w") as archivo:
    json.dump(diccionario,archivo)

with open("diccionario.json","r") as archivo:
    datos=json.load(archivo)
archivo.close()

for i in datos:
    print(datos[i])
