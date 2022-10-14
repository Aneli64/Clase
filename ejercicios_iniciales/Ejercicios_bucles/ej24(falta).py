'''
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1,
finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
'''

numeros = int(input("Introduzca un numero mayor que 1: \n"))
contNumPrimos = 0
listaNumDiv = []

while numeros != 0:
    for i in range(1, numeros + 1):
        if numeros % i == 0:
            listaNumDiv.append(i)
    if listaNumDiv.__len__() == 2:
        contNumPrimos += 1
    numeros = int(input("Introduzca un nuevo numero (0 para salir): \n"))

print("Ha introducido, ", contNumPrimos, "numeros primos")
print(listaNumDiv.__len__())