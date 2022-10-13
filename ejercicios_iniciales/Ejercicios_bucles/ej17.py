'''
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
'''

numero = int(input("Introduzca un numero: \n"))
sum = 0
for i in range(0, len(str(numero))):
    sum += i
print("La suma de sus cifras es ->", sum)