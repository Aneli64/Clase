'''
Escribir un programa que pida al usuario un número entero positivo y muestre
por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

numero = int(input("Introduzca un numero para saber sus valores impares hasta el -> "))
resultado = ""
for i in range(0, numero):
    if i%2 != 0:
        resultado += str(i) + ", "

print(resultado)