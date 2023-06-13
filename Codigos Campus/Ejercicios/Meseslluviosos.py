'''
Determinar en los meses de abril, mayo y junio el promedio de lluvias
del mes, teniendo en cuenta los centimetros de lluvia caidos por dia
(Los valores de los cms de lluvia por dia pueden ser generados por medio de un numero 
aleatorio entre 0 y 11) determinar cual fue el mes mas lluvioso en promedio.
'''
import random
meses=[[],[],[]]
maximo=0
prom = 0

for j in range(3):
    sum=0
    for i in range(30):
        cms=random.randint(0,11)
        sum+=cms
    promedio=sum/30
    meses[j].append(promedio)
    if(promedio > prom):
        prom = promedio;
        maximo = j;
        

if maximo == 0:
    print("Abril")
elif maximo == 1:
    print("Mayo")
elif maximo == 2:
    print("junio")
print(meses)







