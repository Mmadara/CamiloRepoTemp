print("\n\n")
import math
num=int(input("Ingrese el valor de n: "))
R=int(input("Ingrese el valor de r: "))
mix=num-R
fact=1

for i in range(1,num):
    fact= fact*(i+1)
    n=fact
    

for i in range(1,R):
    fact= fact*(i+1)
    r=fact
    

for i in range(1,mix):
    fact= fact*(i+1)
    r=fact
    

c= n/((mix)*R)
print(int(c))    

print("\n\n")