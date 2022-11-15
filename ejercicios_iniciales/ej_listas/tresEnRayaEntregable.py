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


# Formas de ganar
def ganaFila():
    if partida[0] == ["0", "0", "0"] or partida[1] == ["0", "0", "0"] or partida[2] == ["0", "0", "0"]:
        return True


def ganaColumna():  # revisar esto para entenderlo
    for i in range(0, len(partida)):
        if [fila[i] for fila in partida] == ["0", "0", "0"] or [fila[i] for fila in partida] == ["#", "#", "#"]:
            return True


def ganaDiagonal():  # intentar resumir esto
    if [partida[0][0], partida[1][1], partida[2][2]] == ["0", "0", "0"] or [partida[0][2], partida[1][1],
                                                                            partida[2][0]] == ["0", "0", "0"] \
            or [partida[0][0], partida[1][1], partida[2][2]] == ["#", "#", "#"] or [partida[0][2], partida[1][1],
                                                                                    partida[2][0]] == ["#", "#", "#"]:
        return True


# Condicion de finalizar partida
def finPartida():
    if ganaFila() or ganaColumna() or ganaDiagonal():
        return True


# Codigo:
partida = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]
print("\n", partida[0], "\n", partida[1], "\n", partida[2])
excep = False
# introducir variable guia??? -> 0,0 | 0,1 | 0,2 | 1,0 | 1,1 | 1,2 | 2,0 | 2,1 | 2,2
# introducir try ex para opciones de bucle fuera de rango u otras excepciones posibles
while not finPartida():
    input1 = input("J1: Introduzca posicion -> ")
    input2 = input("J2: Introduzca posicion -> ")
    if turnoJ1():
        turnoJ1()
        print("\n", partida[0], "\n", partida[1], "\n", partida[2])
    else:
        excep = True
        break
    if turnoJ2():
        turnoJ2()
        print("\n", partida[0], "\n", partida[1], "\n", partida[2])
    else:
        excep = True
        break

if excep:
    print("*** FIN PARTIDA *** \n Partida finalizada por un error de seleccion de ficha")
else:
    print("*** FIN PARTIDA ***")