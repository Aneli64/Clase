"https://www.aceptaelreto.com/problem/statement.php?id=100"

numero = input("numero: ")
numeroMax = ""
numeroMin = ""
contIter = 0
listaValores = []

while numero != 6174:
    for item in reversed(sorted(str(numero))):
        numeroMax += item
    for item in sorted(str(numero)):
        numeroMin += item
    numero = int(numeroMax) - int(numeroMin)
    listaValores.append(numero)
    contIter += 1
    numeroMax = ""
    numeroMin = ""

print("Valores -> ", listaValores, "Numero de iteraciones necesarias: ", contIter)