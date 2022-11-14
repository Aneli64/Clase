'''
Leeremos la calificación de 5  asignaturas de un alumno introduciendolas en una lista,
entre SUSPENSO APROBADO BIEN NOTABLE SOBRESALIENTE introducir en un tupla para
comprobar que sea correcta cada  una. Mostrar cuántos suspensos tiene.
Para entrega
'''

asignaturas = []
notas = "SUSPENSO", "APROBADO", "BIEN", "NOTABLE", "SOBRESALIENTE"
print(f"Formato de notas -> ")
contSusp = 0
while len(asignaturas) < 5:
    asig = input("Introduzca una nota -> ")
    if asig not in notas:
        break
    else:
        if asig == "SUSPENSO":
            contSusp += 1
            asignaturas.append(asig)
        else:
            asignaturas.append(asig)

print(f"Tiene {contSusp} suspensos")