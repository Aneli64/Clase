'''Los alumnos de un curso se han dividido en dos
grupos A y B de acuerdo al sexo y el nombre. El grupo A esta
formado por las mujeres con un nombre anterior a la M y los hombres con un nombre
posterior a la N y el grupo B por el resto. Escribir un programa que pregunte
al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''

nombre = input("Introduzca su nombre -> ")
sexo = input("Introduzca su sexo [ H / M ] -> ")

if nombre[0] < 'M' and sexo == 'M' or nombre[0] > 'N' and sexo == 'H':
    print("Grupo A")
else:
    print("Grupo B")