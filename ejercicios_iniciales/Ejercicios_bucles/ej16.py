'''
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0.
Informar cuál fue el mayor número ingresado.
'''

numero = int(input("Introduzca un numero: \n"))
total = []

while numero != 0:
    total.append(numero)
    numero = int(input("Introduzca un numero: \n"))

print("El numero mayor ha sido -> ", max(total))