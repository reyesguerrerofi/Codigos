# Inicializar una lista
lista1 = [] #* Lista vacia
print(lista1)

lista1 = [2,34,45] #* Inicializar con valores
print(lista1)

lista2 = [1,"Hola",lista1] #*Una lista con distintos valores
print(lista2)

#? Accediendo a sus datos

lista3 = [i for i in range(10)] #* Una lista con 10 elementos 0-9
print(lista3)
print(lista3[0]) #* Primer elemento
print(lista3[-1])#* Ultimo elemento
print(lista3[-10])#* Primer elemento

#? Slide y Stride de la lista

print(lista3[1:]) #* Desde el segundo hasta el tercer elemento
print(lista3[1:5])#*Desde el segundo al cuarto elemento
print(lista3[2::2]) #*Desde el segundo al ultimo elemento de dos en dos

#? Operaciones de lista 

#Operaciones de listas
lista4 = [1,2,3,4,5,6]
#Tamaño
print(len(lista4))
#Concatenacion
lista5 = lista4 + [7,8,9,"hola "] #Agrega al final de la lista nuevos elementos 
print(lista5)
#Multiplicacion
print(lista5[9]*5)#Imprime el ultimo elemento 5 veces
#Pertenencia
print("hola " in lista5) #Regresa True en caso de que si exista ese elemento en la lista
#Iteracion
for i in lista5:
    print(i)  #Imprime cada uno de los elementos existentes en la lista

lista = [1,2,3]
#Append
lista.append([4,5,6]) #La salida produce [1,2,3,[4,5,6]] debido a que el [4,5,6] lo ve como un solo elemento
print(lista)
#Extend
lista.extend([7,8,9]) #La salida produce [1,2,3,[4,5,6],7,8,9] ya que considera el [7,8,9] como un elemento iterable
print(lista)
lista.extend('hola') #Al considerarse iterable agregara los caracteres de uno en uno como 'h' 'o' 'l' 'a'
print(lista)
#Count
lista.append('a') 
print(lista)
lista.count('a') #La salida es 2 porque hay 2 letras a
#Index
lista.index('a') #Devuelve el indice de la primera a encontrada
#Insert
lista.insert(10,'o') #Inserta la letra o en el indice 10, los valores que le siguen se conservan pero recorren su indice
print(lista)
#Pop
lista.pop() #Remueve el ultimo valor y lo muestra
print(lista)
lista.pop()
lista.pop()
print(lista)
#Remove
lista.remove([4,5,6]) #Remueve la primera coincidencia del valor indicado
print(lista)
#Reverse
lista.reverse() #Invierte el orden de la lista
print(lista)
#Sort
lista2 = [6,9,4,2,5,7,0,1,3]
lista2.sort() #Ordena la lista de manera ascendente
print(lista2)


lista1 = [1,2,3,4,5,10]
print(len(lista1)) #Tamaño de lista
print(max(lista1)) #Muestra el valor mas grande
print(min(lista1))
