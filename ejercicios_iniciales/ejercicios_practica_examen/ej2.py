'''
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario
ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
'''

numero = input("Numero -> ")
contPares = 0
contImpares = 0
contParesTotal = 0
contImparesTotal = 0

while numero != "0":
    for item in numero:
        if int(item) % 2 == 0:
            contPares += 1
            contParesTotal += 1
        else:
            contImpares += 1
            contImparesTotal += 1
    print("Tiene ", contPares, "cifras pares y ", contImpares, "cifras impares")
    contPares = 0
    contImpares = 0
    numero = input("Numero -> ")

print("Cantidad de digitos pares leidos en total -> ", contParesTotal)
print("Cantidad de digitos impares leidos en total -> ", contImparesTotal)
