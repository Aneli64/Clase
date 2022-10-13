'''
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente,
mostrar la sumatoria de todos los números positivos ingresados.
'''

numero = int(input("Introduzca un numero: \n"))
total = 0

while numero != 0:
    if numero > 0:
        total += numero
        numero = int(input("Introduzca un numero: \n"))
    else:
        numero = int(input("Introduzca un numero: \n"))

print("La sumatoria de todos los numeros es ->", total)