'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''

listaNumeros = []

for i in range(0, 5):
    numGanad = int(input("Introduzca los numeros ganadores: \n"))
    listaNumeros.append(numGanad)

print("Los numeros ganadores ordenados de menor a mayor son -> ", sorted(listaNumeros))
