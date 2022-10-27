
numPruebas = int(input("Numero de pruebas - > "))

listaParejas1 = []
listaParejas2 = []

while numPruebas > 0:
    pareja1 = input("Introduzca las primeras dos parejas -> ")
    listaParejas1.append(pareja1)

    pareja2 = input("Introduzca las segundas dos parejas -> ")
    listaParejas2.append(pareja2)
    numPruebas -= 1

for i in range(0, len(listaParejas1)):
    for item in listaParejas1[i]:
        if item in range(int(listaParejas1[i].split(" ")[0]), int(listaParejas1[i].split(" ")[1])) == any(item) in range(int(listaParejas2[i].split(" ")[0]), int(listaParejas2[i].split(" ")[1])):
            print("SOLAPADOS")
        else:
            print("SEPARADOS")

print(listaParejas1)
print(listaParejas2)
print(len(listaParejas1))