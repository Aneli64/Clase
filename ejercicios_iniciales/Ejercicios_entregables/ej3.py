matricula = input("Matricula -> ")
listaMatricula = []

while matricula != "0":
    listaMatricula.append(matricula)
    matricula = input("Matricula -> ")

contAntiguas = 0
contNuevas = 0
j = 4

for i in range(1, len(listaMatricula)):
    if listaMatricula[0][4:7] == listaMatricula[i][4:7]:
        numero = int(listaMatricula[0][0:3]) - int(listaMatricula[i][0:3])
        if numero < 0:
            contNuevas += 1
        else:
            contAntiguas += 1

    else:
        for k in range(1, len(listaMatricula)):
            for x in range(4, 7):
                if listaMatricula[k][x] == listaMatricula[0][j]:
                    j += 1
                else:
                    if str(listaMatricula[k][x]) > str(listaMatricula[0][j]):
                        contNuevas += 1
                        break
                    else:
                        contAntiguas += 1
                        break

print(contAntiguas, contNuevas)