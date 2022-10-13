'''
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los
dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar,
mostrar cuántos de los números ingresados por el usuario fueron números pares.
'''

numero = str(input("Introduzca un numero: \n"))
cont = 0
listaCont = []
listaNum = []
while int(numero) != -1:
    sumaDig = 0
    for i in range(0, int(len(numero))):
        sumaDig += int(numero[i])
    listaNum.append(int(numero))
    listaCont.append(sumaDig)
    print("La suma de sus digitos es -> ", listaCont[cont])
    cont += 1
    numero = str((input("Introduzca otro numero: \n")))

print("Sale")

contPares = 0
contImpares = 0
for i in range(0, len(listaNum)):
    if i % 2 == 0:
        contPares += 1

print("Ha introducido ", contPares, " numeros pares")
