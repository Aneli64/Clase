'''
Solicitar al usuario que ingrese los nombres de alumnos de programación y los de FOL.
informar de los nombres de todos los alumnos sin repeticiones
informar de los alumnos que estén en las dos asignaturas
informar de los que estén en programación pero no en FOL.
'''

alumnosProg = input("Nombre alumno de programacion -> ")
alumnosFol = input("Nombre alumno de Fol -> ")

conjProg = set(alumnosProg.split(" "))
conjFol = set(alumnosFol.split(" "))

print(conjProg | conjFol)
print(conjProg & conjFol)
print(conjProg ^ conjFol)
