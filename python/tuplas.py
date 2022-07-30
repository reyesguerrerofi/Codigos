
#! Tuplas

tupla1 = ('Antonio',23,4,1996)
lista1 = list(tupla1)#*Convierte a lista
tupla2 = tuple(lista1)
print(tupla1[0])
print(lista1)
print(tupla2)

#*COmprobar si existe valor en la tupla

print("Antonio" in tupla1)

#*Cuantos elementos en tupla

print(tupla2.count(1996))

print(len(tupla1)) #*Tamaño

#*Tupla unitaria
tuplaUnit=(1)
tuplaUnit1 = 1 ,2 ,3 ,4, 'a'
#*Se empaqueta la tupla
print(tuplaUnit1)

#*Desempaquetado de tupla

nombre,dia,mes,ano = tupla1

print(nombre)
print(dia)
print(mes)
print(ano)