con=0
def TowerOfHanoi(n , source, auxiliary, destination):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",auxiliary)
        return
    TowerOfHanoi(n-1, source, destination, auxiliary)
    print ("Move disk",n,"from source",source,"to destination",auxiliary)   
    TowerOfHanoi(n-1, destination, auxiliary, source)

# Driver code
n =3
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods
 