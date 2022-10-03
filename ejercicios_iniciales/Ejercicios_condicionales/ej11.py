''' leer los valores de tres números y  mostrarlos ordenados ascendente (casa)'''

cont = 0
numeros = []
numerosOrd = []

while cont != 3:
    numeros.append(input("Introduzca un numero -> "))
    cont += 1

print("Numeros -> ", numeros)

for i in range(0, 3):
    if numeros[i] == max(numeros):
        numerosOrd.append(numeros[0])
        numeros.remove(numeros[i])
print("Numeros ordenados -> ", numerosOrd)

#REVISAR