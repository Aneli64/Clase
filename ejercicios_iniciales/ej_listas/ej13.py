'''
Escribir un programa que guarde una lista de nombres de alumnos y una lista de nombre
de asignaturas y guardaremos en una lista de listas las notas de todos los alumnos en todas
las asignaturas. Imprimir boletín de notas de cada alumno.
por otro lado una estadística de cada asignatura.
'''

nombres = ["Paco", "Jose", "Laura"]
asignaturas = ["Mates", "Lengua", "Historia", "Fisica", "Quimica"]
notas = [[7.4, 4.6, 8.2, 9.3, 5.5], [5.4, 8.6, 3.2, 4.3, 1.5], [9.4, 6.6, 2.2, 5.3, 7.5]]

for i in range(0, len(nombres)):
    print("Nombre:", nombres[i])
    for j in range(0, len(notas[i])):
        print(f"asignatura: {asignaturas[j]}, nota: {notas[i][j]}")

notasMates = []
notasLengua = []
notasHistoria = []
notasFisica = []
notasQuimica = []

# for i in range(0, len(asignaturas)):
    # for j in range(0, len(notas[i])):