'''Escriba un programa que pida un número entero mayor que cero
y que escriba sus divisores.
'''

check = False

while check != True:
    numero = int(input("Introduzca un numero mayor que 0 -> "))
    if numero <= 0:
        print("Numero introducido no valido")
    else:
        check = True

listaDiv = []

for i in range(1, numero):
    if numero % i == 0:
        listaDiv.append(i)

print("Los divisores del numero ", numero, " son = ", listaDiv)