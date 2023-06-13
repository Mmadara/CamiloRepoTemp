'''
Para un concierto hay 3 tipos de boletas, desarrollar un programa que calcule el total de ventas para cada boleta
(cuantas boletas se vendieron de cad atipo y cuanto se recaudo por boleta).
En cada venta se pueden vender mas de una boleta,pero solo de un mismo tipo.
|
|   Ubicacion   Valor   US$
1   General     50
2   VIP         75    
3   Platinum    100
'''
print("|  Ubicacion   Valor   US$\n1   General     50\n2   VIP         75 \n3   Platinum    100")
ticket=int(input("Seleccione el tipo de boleta que desea comprar: "))
canTicket = int(input("cuantas boletas va a comprar: "))
total=0
totalB=0


def concert(ticket,canTicket):    
    if ticket== 1 :
        total= canTicket*50
        cant+= canTicket
    elif ticket== 2:
        total=canTicket*75
    elif ticket== 3:
        total = canTicket*100
    print(total)

concert(ticket,canTicket)

totalB+=total

# def totalV ():
#     if ticket== 1 :
#         totalBuy+=0
#     elif ticket== 2:
#         totalBuy+=0
#     elif ticket== 3:
#         totalBuy+=0

# totalV() 



