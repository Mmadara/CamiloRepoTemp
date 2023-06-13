print("\n\n")
person = {
    "nombre:":"Juan Ernesto",
    "apellidos":"Montoya Ardila",
    "direcciòn":"calle 52 # 35-27 "
}
print(person["direcciòn"])

juego ={
    "p1":{
       "nombre":"",
       "puntos": 0
    },
    "p2":{
        "nombre":"",
        "puntos": 0
    }   
}

juego["p1"]["nombre"] = "Serena Williams"
print(juego["p1"]["nombre"])
print(juego["p1"]["puntos"])
print(juego)
juego["p3"]={
    "nombre":"Mario",
    "puntos":0
}


for i in range (30):
    juego["p"+str(i)]={
        "nombre":"Mario",
        "puntos":0
    }

for i in range (4):
    juego["p"+str(i)]={
        "nombre": "mario",
        "puntos":0
    }

print("\n\n")
