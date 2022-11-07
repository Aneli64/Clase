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
asigSize = int(input("Numero de asignaturas a introducir -> "))

for i in range(0, asigSize):
    nota = int(input("Introduzca su nota -> "))
    listaAsigNotas.append(nota)
    asig = str(input("Introduzca su asignatura -> "))
    listaAsigNotas.append(asig)


for i in range(0, len(listaAsigNotas), 2):
    if int(listaAsigNotas[i]) >= 5:
        listaAsigNotas.remove(listaAsigNotas[i])
        listaAsigNotas.remove(listaAsigNotas[i-1])

print(listaAsigNotas)