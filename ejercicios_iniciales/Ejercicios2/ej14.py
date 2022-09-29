'''Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
Dicha calificación se compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final.'''

califParc1 = float(input("Introduzca la nota de su primer parcial: "))
califParc2 = float(input("Introduzca la nota de su segundo parcial: "))
califParc3 = float(input("Introduzca la nota de su tercer parcial: "))
califExamFin = float(input("Introduzca la nota de su examen final: "))
califTrabFin = float(input("Introduzca la nota de su trabajo final: "))

promedioCalif = (califParc1+califParc2+califParc3)/3

notaFinal = round((promedioCalif*0.55)+(califExamFin*0.3)+(califTrabFin*0.15))

print("Su calificacion final es: ", notaFinal)


