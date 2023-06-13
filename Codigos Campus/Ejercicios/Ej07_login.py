print("\n\n")
def login():
    erroneo=0
    bloqueo= True
    
    while bloqueo :
        usuario=input("Ingrese su usuario:")
        password=input("Ingrese su contraseña:")
        
        if usuario=="usuario1" and password=="asdasd":
            print("\nIngreso Exitoso")
        elif erroneo == 3 :
            print("\nUsuario bloqueado")
            bloqueo=False
        else:
            print("\nUsuario o contraseña incorrecta\n")
            erroneo+=1
login()
print("\n\n")
