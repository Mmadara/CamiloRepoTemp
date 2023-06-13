print("\n\n")

def saludar():
    print("\nHola")

def verNombreCompleto(nombre,apellido):
    print(nombre,apellido)

def obtenerNombreCompleto(nombre,apellido):
    return nombre + " " + apellido

#funcion con parametros y retorno
print("\nFuncion Saludo")
saludar()
print("\nFuncion ver nombre completo")
verNombreCompleto("Juan", "Perez")
print("\nFuncion obtener nombre completo")
nombreCompleto=obtenerNombreCompleto("Juan", "Perez")
print(nombreCompleto)
print("\n\n")
