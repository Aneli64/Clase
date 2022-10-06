'''
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a
una las letras de la palabra introducida empezando por la primera.
'''

palabra = str(input("Introduzca una palabra para ser leida letra a letra -> "))

for i in range(0, palabra.__len__()):
    print(palabra[i])