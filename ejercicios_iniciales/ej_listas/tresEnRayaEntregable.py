'''
Realizar el juego del tres en raya:
Crea el juego del tres en raya para dos jugadores mostrando el tablero a cada jugada y
detectando cuando se realiza un tres en raya. (utilizar caracteres O para un jugador y X para
otro).
'''

# Turnos de cada jugador
def turnoJ1():
    if partida[int(input1[0])][int(input1[2])] == "X":
        partida[int(input1[0])][int(input1[2])] = "0"
        return True


def turnoJ2():
    if partida[int(input2[0])][int(input2[2])] == "X":
        partida[int(input2[0])][int(input2[2])] = "#"
        return True

#Formas de ganar
def ganaFila():
    if partida[0] == ["0", "0", "0"] or partida[1] == ["0", "0", "0"] or partida[2] == ["0", "0", "0"]:
        return True


def ganaColumna():
    if partida[0] == ["0", "0", "0"]:
        return True


def ganaDiagonal():
    if partida[0] == ["0", "0", "0"]:
        return True


# Condicion de finalizar partida
def finPartida():
    if ganaFila() or ganaColumna() or ganaDiagonal():
        return True


# Codigo:
partida = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]
print("\n", partida[0], "\n", partida[1], "\n", partida[2])

# introducir variable guia??? -> 0,0 | 0,1 | 0,2 | 1,0 | 1,1 | 1,2 | 2,0 | 2,1 | 2,2
# introducir try ex para opciones de bucle fuera de rango


while not finPartida():
    input1 = input("J1: Introduzca posicion -> ")
    input2 = input("J2: Introduzca posicion -> ")
    if turnoJ1():
        turnoJ1()
        print("\n", partida[0], "\n", partida[1], "\n", partida[2])
    else:
        input1 = input("Posicion j1 ya alterada, introduzca una nueva -> ")

    if turnoJ2():
        turnoJ2()
        print("\n", partida[0], "\n", partida[1], "\n", partida[2])
    else:
        input2 = input("Posicion j2 ya alterada, introduzca una nueva -> ")

print("*** FIN PARTIDA ***")
