'''
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a
una las letras de la palabra introducida empezando por la última.
'''

palabra = str(input("Introduzca una palabra para ser leida letra a letra -> "))

for i in range(palabra.__len__()-1, -1, -1):
    print(palabra[i])