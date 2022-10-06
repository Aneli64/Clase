'''
Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es un número primo o no.
'''

numero = int(input("Introduzca un numero para saber si es primo: \n"))
listaNumDiv = []

for i in range(1, numero+1):
    if numero % i == 0:
        listaNumDiv.append(i)

if listaNumDiv.__len__() == 2:
    print("Su numero es primo")
else:
    print("Su numero no es primo, es divisible por -> ", listaNumDiv)

# 3455363