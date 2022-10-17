'''
Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre
un mensaje cada vez que un número no sea mayor que el primero.
'''

numeros = int(input("Cantidad de numeros a introducir: \n"))
primerNumero = int(input("Primer numero comparativo: \n"))

for i in range(0, numeros):
    numero = int(input("Introduzca un numero: \n"))
    if numero < primerNumero:
        print("Su numero es menor que el primero")
    else:
        print("Su numero es mayor o igual que el primero")


