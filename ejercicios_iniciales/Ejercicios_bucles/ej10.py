'''
Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es un número primo o no.
'''

numero = int(input("Introduzca un numero para saber si es primo: \n"))

for i in range(1, numero):
    if numero/2 != 0:
        print()
