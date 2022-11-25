import random


def aleatorio(conjunto):
    numerosSal = []
    for i in range(0, 15):
        numero = random.randint(1, 90)
        while numero in numerosSal:
            numerosSal.append(numero)
            numero = random.randint(1, 90)
        conjunto.add(numero)
        numerosSal.append(numero)
    return set


carton1 = set()
carton2 = set()
aleatorio(carton1)
aleatorio(carton2)

while len(carton1) != 0 and len(carton2) != 0:
    numerosYasalidos = []
    numeroCantado = random.randint(1, 90)
    print("Numero cantado -> ", numeroCantado)
    print(f"Lista jugador1 -> {carton1} \n Lista jugador2 -> {carton2}")
    if numeroCantado in carton1:
        carton1.remove(numeroCantado)
    if numeroCantado in carton2:
        carton2.remove(numeroCantado)
    if numeroCantado not in numerosYasalidos:
        numerosYasalidos.append(numeroCantado)

if len(carton1) == 0:
    print("Ganador jugador 1!")
    for item in carton1:
        print(item)
if len(carton2) == 0:
    print("Ganador jugador 2!")
    for item in carton2:
        print(item)
