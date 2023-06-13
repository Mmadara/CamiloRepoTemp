milista=['juan','Maria','Jose']
milista.sort(reverse=True)

m=len (milista)

for i in range (m-1):
    for j in range(i-1,m):
        if milista[i]>milista[j]:
            t=milista[i]
            milista[i]=milista[j]
            milista[j]=t

print (milista)