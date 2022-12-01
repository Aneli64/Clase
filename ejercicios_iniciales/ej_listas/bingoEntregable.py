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


def linea(lista):
    for item in lista:
        if item == [0, 0, 0, 0]:
            return True


def bingo(lista):
    suma = 0
    for item in lista:
        suma += item
    if suma == 0:
        return True

# ganador primera linea
def ganadorLinea(contLinea):
    if contLinea == 1:
        return True


# ganador partida (bingo)
def ganadorBingo(tableroBingo):
    if tableroBingo:
        return True


def borrar(lista, numeroCoinc):
    for i in range(-1, len(lista)):
        for j in range(-1, len(lista[i])):
            if lista[i][j] == numeroCoinc:
                lista[i][j] = 0


bingo1 = [[], [], []]
bingoF1 = aleatorio(bingo1)

bingo2 = [[], [], []]
bingoF2 = aleatorio(bingo2)

numerosDisp = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

# Variables que usaremos para que solo se cante una vez la linea, y para almacenar quien cantó esta primera linea
contLinea = 0
contLJ1 = 0
contLJ2 = 0

print(mostrarCarton(bingoF1))
print(mostrarCarton(bingoF2))

while bingo(valoresCarton(bingoF1)) != True or bingo(valoresCarton(bingoF2)) != True:
    siguiente = input("Presione una tecla para generar un numero aleatorio: ")
    numeroBingo = random.choice(list(numerosDisp))
    print("Numero cantado -> ", numeroBingo)

    if numeroBingo in valoresCarton(bingoF1):
        borrar(bingoF1, numeroBingo)
    if numeroBingo in valoresCarton(bingoF2):
        borrar(bingoF2, numeroBingo)

    numerosDisp.remove(numeroBingo)
    print(mostrarCarton(bingoF1))
    print(mostrarCarton(bingoF2))

    if linea(bingoF1) and contLinea != 1:
        print("¡Jugador 1 ha cantado linea!")
        contLinea += 1
        contLJ1 += 1
    if linea(bingoF2) and contLinea != 1:
        print("¡Jugador 2 ha cantado linea!")
        contLinea += 1
        contLJ2 += 1

if ganadorLinea(contLJ1):
    print("Jugador1 ganador de la primera linea")
if ganadorLinea(contLJ2):
    print("Jugador2 ganador de la primera linea")

if ganadorBingo(bingo(bingoF1)):
    print("Jugador1 ganador del bingo")
if ganadorBingo(bingo(bingoF2)):
    print("Jugador2 ganador del bingo")