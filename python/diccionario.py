
#!Diccionarios

diccionario1 = {
  "Antonio": "Estudiante",
  "Emiliana": "Maestra",
  "Nancy": "Lic",
  "JC": "Mago"
}

#*Accediendo al diccionario

print(diccionario1["Emiliana"])
print(diccionario1["JC"])

print(diccionario1)

#*Nuevo valor

diccionario1["Ara"]="Comunicologa"

print(diccionario1)

del diccionario1["Nancy"]

print(diccionario1)

#*Creando a partir de otra estructura

milista = ["CDMX","EdoMex","NL","Guadalajara"]

midiccionario = {
  milista[0]:1,
  milista[1]:2,
  milista[2]:3,
  milista[3]:4
}
print(midiccionario)

#*Almacenar otra estructura

midiccionario = {
  "Maeta":"Escuela",
  "nombre":"Emi",
  "lugar": "Xochimilco",
  "talentos":{"artes":[1,2,3]}
}
print(midiccionario.keys())
print(midiccionario.values())
