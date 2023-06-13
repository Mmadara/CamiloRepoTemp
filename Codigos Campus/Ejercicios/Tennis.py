import random 
import math
a=0
b=0
j1=0
j2=0
jugador1 = input("\nIngrese el nombre del jugador1: ") 
jugador2 = input("\nIngrese el nombre del jugador2: ")
jugadores=[jugador1,jugador2]
aleatorio =random.choice(jugadores)
print("\nEl jugador que arranca es: ",aleatorio)

while ((j1-j2)*-1) <= 2:
 punto = input("\nQuien realizo un punto: ")
 if punto == jugador1:
    j1= j1+1
 elif punto== jugador2:
    j2=j2+1
 print(j1," ", j2)

 if j1==1:
    a=15
    print("\nEl puntaje es ",jugador1," ", a ,' ',jugador2,' ', b )
 elif j2==1:
    b=15
    print("\nEl puntaje es ",jugador1," ", a ,' ',jugador2,' ', b )
 elif j1==2:
    a=30
    print("\nEl puntaje es ",jugador1," ", a ,' ',jugador2,' ', b )
 elif j2==2:
    b=30
    print("\nEl puntaje es ",jugador1," ", a ,' ',jugador2,' ', b )
 elif j1 == 3:
    a=40
    print("\nEl puntaje es ",jugador1," ", a ,' ',jugador2,' ', b )
 elif j2==3:
    b=40
    print("\nEl puntaje es ",jugador1," ", a ,' ',jugador2,' ', b )
 elif j1==8:
    print("\nEl puntaje es ",jugador1," ", a ,' ',jugador2,' ', b )
    print("\nGano: ",jugador1)
 elif j2==8:
     print("\nEl puntaje es ",jugador1," ", a ,' ',jugador2,' ', b )
     print("\nGano: ",jugador2)
 elif j1==4 and abs(j1-j2)>=2:
     print("funciona")
     



