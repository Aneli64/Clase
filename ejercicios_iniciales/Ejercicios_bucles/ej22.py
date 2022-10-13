'''
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario
ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
'''

numero = input("Introduzca un numero entero positivo: \n")

while int(numero) != 0:
    contPares = 0
    contImpares = 0
    for i in range(0, len(str(numero))):
        if int(numero[i]) % 2 == 0:
            contPares += 1
        elif int(numero[i]) % 2 != 0:
            contImpares += 1
    print("Su numero tiene ", contPares, "digito(s) pares, y ", contImpares, "digito(s) impares")
    numero = input("Introduzca otro numero entero positivo: \n")
