
numPruebas = int(input("Numero de pruebas - > "))
entradas = []
while numPruebas > 0:
    entrada = input("Entrada -> ")
    entradas.append(entrada)
    numPruebas -= 1

login = 0
listaLogin = []
maxEntrada = 0
listaValFinal = []

for item in entradas:
    for ent in item:
        if ent == "I":
            login += 1
        elif ent == "O":
            listaLogin.append(login)
            maxEntrada = max(listaLogin)
            login = 0
    listaValFinal.append(maxEntrada)
    maxEntrada = 0


print(listaValFinal)