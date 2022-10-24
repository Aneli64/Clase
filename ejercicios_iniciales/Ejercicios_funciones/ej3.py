'''
Crear una función que calcule la distancia entre dos puntos en el plano.
'''
import math

def distanciaPuntos(x1, x2, y1, y2):
    resultado = math.sqrt((x1-y1).__pow__(2)+(x2-y2).__pow__(2))
    return resultado

print(distanciaPuntos(5,5,5,6))

