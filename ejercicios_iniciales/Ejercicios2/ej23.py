'''Escribir un algoritmo para calcular la nota final de un estudiante, considerando
que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0.
 Imprime el resultado obtenido por el estudiante.
'''

listaRespuestas = []
puntosTotales = 0

for i in range(0, 10):
    respuesta = input("Introduzca la respuesta [CORR/INCORR/VAC]: ")
    listaRespuestas.append(respuesta)
    if respuesta == "CORR":
        puntosTotales += 5
    elif respuesta == "INCORR":
        puntosTotales -= 1
    elif respuesta == "VAC":
        puntosTotales += 0

print("Sus puntos totales son: ", puntosTotales)
