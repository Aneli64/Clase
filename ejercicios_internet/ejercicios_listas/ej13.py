'''
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
(comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media,
la nota más alta que ha sacado y la menor.
'''

listaNotas = []
nota = float(input("Introduzca una nota: \n"))

while len(listaNotas) < 5:
    if nota < 0 or nota > 10:
        nota = float(input("Nota no valida, introduzca otro valor: \n"))
    else:
        nota = float(input("Introduzca una nota: \n"))
        listaNotas.append(nota)

print("Notas -> ", listaNotas)
print("Promedio -> ", sum(listaNotas)/len(listaNotas))
print("Nota mas alta -> ", max(listaNotas), "Nota mas baja ->", min(listaNotas))
