'''
BA1-Realizar un programa que lea nombre, y 5 calificaciones(en un bucle) y presente el promedio de
un alumno, pregunte si desea continuar, en caso afirmativo pregunte por otro alumno, de lo contrario
imprima:
a) La cantidad de alumnos;
b)El promedio del grupo;
c) Cantidad de alumnos con promedio mayor a 8.
si alguna nota es menor de 0 y mayor de 10 lanzar una excepción.
'''

nombre = input("Nombre: \n")
califLIst = []
promedioList = []
numAlumnos = 0
promedioMayor8 = 0

opcion = input("¿Desea continuar? |si|-|no| \n")
while opcion != "no":
    for i in range(0, 5):
        calif = float(input("Nota -> "))
        califLIst.append(calif)
    promedioList.append(sum(califLIst) / len(califLIst))
    califLIst.clear()
    numAlumnos += 1
    print("Promedio del alumno -> ", promedioList[len(promedioList)-1])
    opcion = input("¿Desea continuar? |si|-|no| \n")
    if opcion == "no":
        break
    else:
        nombre = input("Nombre: \n")
for item in promedioList:
    if item >= 8:
        promedioMayor8 += 1

print("Promedio grupo -> ", round(sum(promedioList)/len(promedioList), 2), "\n", "numero de alumnos -> ", numAlumnos, "\n", "alumnos con promedio mayor que 8 -> ", promedioMayor8)
