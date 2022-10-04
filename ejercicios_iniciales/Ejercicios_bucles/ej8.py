'''
Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo.

1

3 1

5 3 1

7 5 3 1

9 7 5 3 1

'''

numero = str(input("Introduzca un numero -> "))

for i in range(1,numero.__len__()):
    print(numero[numero.__len__()-i])

