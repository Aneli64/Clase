import random


def aleatorio(lista):  # Def que llena nuestro bingo de numeros aleeatorios que no se repiten entre si
    numerosSal = []  # Lista de numeros ya salidos (asi evitamos repeticion)
    for i in range(0, 3):
        for j in range(0, 4):
            numero = random.randint(1, 20)
            while numero in numerosSal:
                numerosSal.append(numero)
                numero = random.randint(1, 20)
            lista[i].append(numero)
            numerosSal.append(numero)
    return lista


def mostrarCarton(lista):
    return f"\n {lista[0]} \n {lista[1]} \n {lista[2]}"


# Def Bucle para tener todos los valores en una lista respectivamente (para su facil y mejor manejo futuro)
def valoresCarton(lista):
    valores = []
    for i in range(0, len(lista)):
        for j in range(0, len(lista[i])):
            valores.append(lista[i][j])
    return valores


bingo1 = [[], [], []]
bingoF1 = aleatorio(bingo1)

bingo2 = [[], [], []]
bingoF2 = aleatorio(bingo2)

cont1 = 20
cont2 = 20
numerosDisp = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               16, 17, 18, 19, 20}
print(mostrarCarton(bingoF1))
print(mostrarCarton(bingoF2))
while cont1 != 0 or cont2 != 0:  # borra esta guarrada
    siguiente = input("Presione una tecla para generar un numero aleatorio: ")
    numeroBingo = random.choice(list(numerosDisp))
    print("Numero cantado -> ", numeroBingo)

    if numeroBingo in valoresCarton(bingoF1):  # hacer funcion borrar() para poner la X
        for i in range(-1, len(bingoF1)):
            for j in range(-1, len(bingoF1[i])):
                if bingoF1[i][j] == numeroBingo:
                    bingoF1[i][j] = 0
    if numeroBingo in valoresCarton(bingoF2):
        for i in range(-1, len(bingoF2)):  # PORQUE SIGUE SIN BORRAR ALGS NUMEROS??!
            for j in range(-1, len(bingoF2[i])):
                if bingoF2[i][j] == numeroBingo:
                    bingoF2[i][j] = 0
    numerosDisp.remove(numeroBingo)
    print(mostrarCarton(bingoF1))
    print(mostrarCarton(bingoF2))
    # una vez que salga linea que no vuelva a salir
    for item in bingoF1:
        if item == [0, 0, 0, 0]:
            print("¡Jugador 1 ha cantado linea!")
    for item in bingoF2:
        if item == [0, 0, 0, 0]:
            print("¡Jugador 2 ha cantado linea!")

    if sum(valoresCarton(bingoF1)) == 0:
        print("BINGO J1!")
        break
    if sum(valoresCarton(bingoF2)) == 0:
        print("BINGO J2!")
        break

# print(mostrarCarton(bingoF1))
# print(mostrarCarton(bingoF2))
