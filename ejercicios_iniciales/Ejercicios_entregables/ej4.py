numPruebas = int(input("Numero de pruebas - > "))

listaParejas1 = []
listaParejas2 = []

while numPruebas > 0:
    pareja1 = input("Introduzca las primeras dos parejas -> ")
    listaParejas1.append(pareja1)

    pareja2 = input("Introduzca las segundas dos parejas -> ")
    listaParejas2.append(pareja2)
    numPruebas -= 1

valores1 = []
valores2 = []

for i in range(0, len(listaParejas1)):
    for item in range(int(listaParejas1[i].split(" ")[0]), int(listaParejas1[i].split(" ")[1])+1):
        valores1.append(item)
    for item in range(int(listaParejas2[i].split(" ")[0]), int(listaParejas2[i].split(" ")[1])+1):
        valores2.append(item)

for item in valores1:
    if item == valores2:
        print("SOLAPADOS")
    else:
        print("SEPARADOS")
