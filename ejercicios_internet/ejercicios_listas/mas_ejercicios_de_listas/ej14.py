'''
Programa que declare una lista y la vaya llenando de números hasta que introduzcamos
un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).
'''

listaNumeros = []
numero = int(input("Introduzca un numero (positivo para que sea almacenado) -> "))

while numero > 0:
    listaNumeros.append(numero)
    numero = int(input("Introduzca un numero (positivo para que sea almacenado) -> "))

print(listaNumeros)