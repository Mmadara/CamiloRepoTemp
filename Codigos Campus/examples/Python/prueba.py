# Importar el módulo
import json

# Cadena de caracteres en el formato JSON
datos_JSON =  """
{
	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["champinones", "queso extra", "pepperoni", "albahaca"],
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": "455-344-234",
		"correo": "janedoe@email.com"
	}
}
"""

# Convertir cadena de caracteres JSON a un diccionario
datos_diccionario = json.loads(datos_JSON)

print(datos_diccionario)