'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por
 pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''

nombre = input("Introduzca su nombre: ")
numero = int(input("Introduzca un numero entero: "))

for i in range(0, numero): print(nombre + "\n")
