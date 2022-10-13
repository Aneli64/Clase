'''Leer números enteros de teclado, hasta que el usuario ingrese el 0.
Finalmente, mostrar la sumatoria de todos los números ingresados y la media aritmética
'''

numero = int(input("Introduzca un numero: \n"))
total = 0
cont = 0

while numero != 0:
    total += numero
    cont += 1
    numero = int(input("Introduzca un numero: \n"))

print("La sumatoria de todos los numeros es ->", total, "y su media es ->", round(total/cont))