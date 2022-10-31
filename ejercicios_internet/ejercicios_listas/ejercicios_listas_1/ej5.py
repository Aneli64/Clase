'''
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre
por pantalla en orden inverso separados por comas.
'''

numeros = []

for i in range(0, 100):
    numeros.append(i)

for item in reversed(numeros):
    print(item)
