partida = [["1", "2", "0"],
           ["4", "0", "6"],
           ["0", "8", "9"]]

if [partida[0][0], partida[1][1], partida[2][2]] == ["0", "0", "0"] or [partida[0][2], partida[1][1], partida[2][0]] == ["0", "0", "0"]:
    print("Hola")
else:
    print("Adios")