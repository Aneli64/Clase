'''
Escriba un programa que pida dos números enteros y escriba
qué números son pares y cuáles impares desde el primero hasta el segundo.
'''

numero1 = int(input("Introduzca un numero entero -> "))

numeroMayor = False

while numeroMayor == False:
    numero2 = int(input("Introduzca un numero entero mayor que el anterior -> "))
    if numero2 > numero1:
        numeroMayor = True
    else:
        print("Le he pedido un numero entero mayor que ", numero1)

for i in range(numero1, numero2):
    if i % 2 == 0:
        print("El numero ", i, " es par")
    else:
        print("El numero ", i, " es impar")
