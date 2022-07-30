
#!creando generadores

#*Metodo tradicional
def tradicional(limite=40):
  num=1
  pares=[]
  while num < limite:
    pares.append(num*2)
    num+=1
  return pares

print(tradicional(10))
#*Con generador

def generador(limite=20):
  num = 1
  while num<limite:
    yield num*2
    num+=1

pares = generador()

print(next(pares)) #Devuelve de uno por uno
'''
devuelve todos los valores del generador
for i in pares:
  print(i)
'''

#*yield from para bucles anidados

def devuelve_ciudades(*ciudades):#Numero ideterminado de ciudades, en forma de tupla
  for elemento in ciudades:
    yield elemento
    
ciudades_devueltas = devuelve_ciudades("Ixtapaluca","Xochimilco","Coyoacan","Iman")

print(next(ciudades_devueltas))

def devuelve_ciudades2(*ciudades):#Numero ideterminado de ciudades, en forma de tupla
  for elemento in ciudades:
    for subElemento in elemento:
      yield subElemento
    #Esto devuelve las letras de ixtapaluca

ciudades_devueltas1 = devuelve_ciudades2("Ixtapaluca")

print(next(ciudades_devueltas1))
print(next(ciudades_devueltas1))

#*Version corta


def devuelve_ciudades2(*ciudades):#Numero ideterminado de ciudades, en forma de tupla
  for elemento in ciudades:
      yield from elemento
    #Esto devuelve las letras de ixtapaluca

ciudades_devueltas1 = devuelve_ciudades2("Ixtapaluca")

print(next(ciudades_devueltas1))
print(next(ciudades_devueltas1))

