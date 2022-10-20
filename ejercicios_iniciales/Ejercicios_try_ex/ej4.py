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

opcion = input("¿Desea continuar? |si|-|no| \n")
while opcion != "no":
    for i in range(0, 5):
        calif = float(input("Nota -> "))
        califLIst.append(calif)

print("Promedio del alumno -> ", sum(califLIst)/len(califLIst))