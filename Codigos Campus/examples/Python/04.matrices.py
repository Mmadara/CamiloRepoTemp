print("\n\n")
import random
a=[]
tamaño=int(input("Digite el tamaño de la matriz: "))

for j in range(tamaño):
    matriz=[]
    for i in range (tamaño):
        matriz.append(random.randint(1,9))
    a.append(matriz)

print("\nLa matriz es: \n")
for i in range(tamaño):
    print(a[i])

print("\n\n")