'''
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''

'''
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for item in asignaturas:
    nota = float(input("Que nota ha sacado en " + item + "\n"))
    notas.append(nota)

cont = 0
for i in range(0, len(notas)):
    if notas[i] >= 5:
        asignaturas.remove(asignaturas[i])
        
print("Tiene que repetir las siguientes asignaturas: \n", asignaturas)
'''

listaAsigNotas = []
notas = []
listaFinal = []
asigSize = int(input("Numero de asignaturas a introducir -> "))

for i in range(0, asigSize):
    asig = str(input("Introduzca su asignatura -> "))
    listaAsigNotas.append(asig)
    nota = int(input("Introduzca su nota -> "))
    notas.append(nota)

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, len(listaAsigNotas)):
    listaAsigNotas.append(notas[i])

for i in range(0, len(listaAsigNotas)):
    listaFinal.append(listaAsigNotas[i])
    if listaAsigNotas[i] in numeros:
        listaFinal.append(listaAsigNotas[i])

print(listaFinal)