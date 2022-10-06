'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.
'''

triangulo = int(input("Introduzca un numero para realizar el triangulo -> "))

'''for i in range(1, triangulo+1):
    print("*" * i)'''

cont = 1
while cont != triangulo+1:
    print("*" * cont)
    cont += 1