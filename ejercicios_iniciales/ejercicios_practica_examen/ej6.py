'''
Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o
negativos. Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
No olvides que no es posible dividir por cero, por lo que es necesario evitar que el
programa arroje un error si no se ingresaron números positivos.
'''

sumNumNegativos = 0

sumNumPositivos = 0
contMedia = 0
for i in range(0, 6):
    numero = int(input("Numero -> "))
    if numero < 0:
        sumNumNegativos += numero
    else:
        sumNumPositivos += numero
        contMedia += 1

if sumNumPositivos == 0:
    print("Suma numeros negativos ->", sumNumNegativos, "|", "No hay numeros positivos con los que hacer la media")
else:
    print("Suma numeros negativos ->", sumNumNegativos, "|", "Media numeros positivos ->", sumNumPositivos / contMedia)
