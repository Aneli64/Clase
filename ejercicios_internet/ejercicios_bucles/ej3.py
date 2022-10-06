'''
Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre
un mensaje cada vez que un número no sea mayor que el primero.
'''

contNumeros = int("Introduzca el numero de numeros que va a introducir: \n")

for i in range(1, contNumeros):
    numero = int(input("Introduzca un numero: \n"))
    if numero < numero:
        print("Introduzca un numero ")