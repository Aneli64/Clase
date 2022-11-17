import random


def aleatorio(lista):  # Def que llena nuestro bingo de numeros aleeatorios que no se repiten entre si
    numerosSal = []    # Lista de numeros ya salidos (asi evitamos repeticion)
    for i in range(0, 3):
        for j in range(0, 4):
            numero = random.randint(1, 20)
            while numero in numerosSal:
                numerosSal.append(numero)
                numero = random.randint(1, 20)
            lista[i].append(numero)
            numerosSal.append(numero)
    return lista


def cartonBingo(lista):
    return f"\n {lista[0]} \n {lista[1]} \n {lista[2]}"


bingo1 = [[], [], []]
bingoF1 = aleatorio(bingo1)

bingo2 = [[], [], []]
bingoF2 = aleatorio(bingo2)

valoresCarton1 = []
valoresCarton2 = []
# Bucles para tener todos los valores en una lista respectivamente (para su facil y mejor manejo futuro)
for i in range(0, len(bingoF1)):
    for j in range(0, len(bingoF1[i])):
        valoresCarton1.append(bingoF1[i][j])
for i in range(0, len(bingoF2)):
    for j in range(0, len(bingoF2[i])):
        valoresCarton2.append(bingoF2[i][j])

cont1 = 20
cont2 = 20
numerosYaCantados = []

while cont1 != 0 or cont2 != 0:
    input("Introduzca * -> ")
    numeroBingo = random.randint(1, 20)
    print("Numero cantado -> ", numeroBingo)
    if numeroBingo not in numerosYaCantados:
        numerosYaCantados.append(numeroBingo)
        if numeroBingo in valoresCarton1:
            bingoF1[str(bingoF1.index(numeroBingo)).split(",")[0]][str(bingoF1.index(numeroBingo)).split(",")[2]] = 0
            cont1 -= 1
            print(cartonBingo(bingoF1))
        if numeroBingo in valoresCarton2:
            bingoF2[str(bingoF2.index(numeroBingo)).split(",")[0]][str(bingoF2.index(numeroBingo)).split(",")[2]] = 0
            cont2 -= 1
            print(cartonBingo(bingoF2))

# print(cartonBingo(bingoF1))
# print(cartonBingo(bingoF2))

