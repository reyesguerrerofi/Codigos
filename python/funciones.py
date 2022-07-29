def una_suma(num1 = 1,num2 = 4):
  """una_suma
  Funcion que suma dos numeros
  Args:
      num1 (int, optional): Primer valor de la suma. Defaults to 1.
      num2 (int, optional): Segundo valor de la suma. Defaults to 4.

  Returns:
      int: Resultado de sumar dos numeros.
  """
  
  return num1 + num2  

#*Paso sin referencia
print(una_suma(5,6)) 

print('---')

print(una_suma())

#*Paso por referencia
suma1 = una_suma(2,5) #!Devuelve 7
suma2 = una_suma() #!Devuelve por default 5
suma_total = suma1 + suma2 #! 7 + 5 = 12

print(suma_total)