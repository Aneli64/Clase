'''
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''

numero = int(input("Introduzca un numero para realizar su cuenta atras -> "))

for i in range(-numero, 0):
    print(-i, ", ")