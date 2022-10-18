'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
'''

palabra = list(input("Palabra: \n"))
palabraReversed = reversed(palabra)

cond = print("palindromo") if palabra == palabraReversed else print("no palindromo")