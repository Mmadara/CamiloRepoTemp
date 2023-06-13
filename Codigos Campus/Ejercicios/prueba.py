import random 
# Definimos los nombres de los jugadores
jugador1 = input("Introduce el nombre del primer jugador: ")
jugador2 = input("Introduce el nombre del segundo jugador: ")
jugadores=[jugador1,jugador2]
aleatorio =random.choice(jugadores)
print("\nEl jugador que arranca es: ",aleatorio)

# Definimos las variables iniciales
puntos_jugador1 = 0
puntos_jugador2 = 0

# Iteramos hasta que uno de los jugadores gane
while puntos_jugador1 < 12 and puntos_jugador2 < 12:
    # Pedimos al usuario que indique quién gana el punto
    ganador_punto = input(f"¿Quién gana el punto, {jugador1} o {jugador2}? ")
    
    # Actualizamos los puntos del jugador ganador
    if ganador_punto == jugador1:
        puntos_jugador1 += 1
    else:
        puntos_jugador2 += 1
if puntos_jugador1==1 :
    
# Indicamos quién ganó
if puntos_jugador1 >= 4:
    print(f"{jugador1} gana el juego!")
else:
    print(f"{jugador2} gana el juego!")