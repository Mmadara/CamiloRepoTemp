import io   
import json
print("\n\n")
# nombres="carlos\nluis\nluisa\nCamila\nAlejandra"
# archivo.write(nombres)
# archivo=open("./a/diccionario.txt","w")



'Escritura diccionarios'
diccionario={"nombre":'camila','apellidos':'Gomez','Telefono':'3125478851'}
with open("./ex3/archivoJson.json","w") as archivo:
    json.dump(diccionario,archivo)


'Lectura de Json'
with open("./ex3/archivoJson.json","r") as archivo:
    diccionario=json.load(archivo)
archivo.close()
print(diccionario)

print("\n\n")
