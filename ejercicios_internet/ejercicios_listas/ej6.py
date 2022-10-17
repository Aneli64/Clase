'''
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
asignaturasMod = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for item in asignaturas:
    nota = float(input("Que nota ha sacado en " + item + "\n"))
    if nota > 5:
        asignaturasMod.remove(item)

print("Tiene que repetir las siguientes asignaturas: \n", asignaturasMod)
