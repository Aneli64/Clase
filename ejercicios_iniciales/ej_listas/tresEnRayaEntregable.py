'''
Realizar el juego del tres en raya:
Crea el juego del tres en raya para dos jugadores mostrando el tablero a cada jugada y
detectando cuando se realiza un tres en raya. (utilizar caracteres O para un jugador y X para
otro).
'''


def finPartida():
    if partida[0:2] == ["O", "0", "0"]:
        return True


partida = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]

print("\n", partida[0], "\n", partida[1], "\n", partida[2])

# introducir variable guia??? -> 0,0 | 0,1 | 0,2 | 1,0 | 1,1 | 1,2 | 2,0 | 2,1 | 2,2
# introducir try ex para opciones de bucle fuera de rango
input1 = input("Introduzca posicion -> ")
input2 = input("Introduzca posicion -> ")

while not finPartida():
    if partida[int(input1[0])][int(input1[2])] == "0" or partida[int(input1[0])][int(input1[2])] == "#":
        input1 = input("Posicion ya alterada, introduzca una nueva -> ")
    else:
        partida[int(input1[0])][int(input1[2])] = "0"
        print("\n", partida[0], "\n", partida[1], "\n", partida[2])
        if partida[int(input2[0])][int(input2[2])] == "0" or partida[int(input1[0])][int(input1[2])] == "#":
            input1 = input("Posicion ya alterada, introduzca una nueva -> ")
        else:
            partida[int(input2[0])][int(input2[2])] = "#"
            print("\n", partida[0], "\n", partida[1], "\n", partida[2])
