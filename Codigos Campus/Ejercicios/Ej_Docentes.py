print("\n\n")
numProf=int(input("Ingrese la cantidad de docentes: "))
dic_categoria = {1:25000,2:30000,3:40000,4:50000,5:60000}
profe=[]
totalhon=0
for i in range (numProf):
    honorarios=0
    nombre=input("Ingrese el nombre del docente: ")
    cedula=input("Ingrese el numero de la cedula del docente: ")
    categoria=int(input("A que categoria hace parte: "))
    horaslab=int(input("Cuantas horas laboro este mes: "))
    profe.append([nombre,cedula,categoria,horaslab])
    if categoria== 1 :
        honorarios=profe[i][3]*dic_categoria[categoria]
        profe[i].append(honorarios)
    elif categoria==2:
        honorarios=profe[i][3]*dic_categoria[categoria]
        profe[i].append(honorarios)
    elif categoria==3:
        honorarios=profe[i][3]*dic_categoria[categoria]
        profe[i].append(honorarios)
    elif categoria==4:
        honorarios=profe[i][3]*dic_categoria[categoria]
        profe[i].append(honorarios)
    elif categoria==5:
        honorarios=profe[i][3]*dic_categoria[categoria]
        profe[i].append(honorarios)
    totalhon+=honorarios 

for i in range(numProf):
    print("El total de honorarios a pagar del profesor",profe[i][0],"es",profe[i][4])

print(f"El total de pago por concepto de honorarios es de {totalhon}")

print("\n\n")
