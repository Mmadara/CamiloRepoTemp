# Ejercicio 1
# # Crea un procedimiento EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla 
# (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además 
# subraya el mensaje utilizando el carácter =.
import math
text=input("\nIngresa el titulo: ")
def EscribirCentrado(text):
    total=math.ceil(40-len(text)/2)
    print (text.center(total," "))
EscribirCentrado(text)
