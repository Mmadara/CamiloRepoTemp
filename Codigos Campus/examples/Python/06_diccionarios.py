print("\n\n")
articulos={1:"lapiz",2:"cuadernos",3:"Borrador",4:"calculadora",5:"Escuadra"}
valores={1:2500,2:3800,3:1200,4:35000,5:3700}
opcmenu='s'
total=[]

while opcmenu == 's':
    temporal=[]
    print("----------------Objetos--------------")
    print(f"1.{articulos[1]}\n2.{articulos[2]}\n3.{articulos[3]}\n4.{articulos[4]}\n5.{articulos[5]}\n\n")
    elemento= int(input("Que elemento desea comprar: "))
    cantidad= int(input("Digite cuando elementos va a comprar: "))
    compra= cantidad*valores[elemento]
    opcmenu=input("desea seguir comprando: s/n ")

print("----------Lista de elementos comprados-------------")

        


