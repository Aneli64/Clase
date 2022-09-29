'''Pide al usuario dos pares de números x1,y2 y x2,y2,
que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.'''
import math

x1 = int(input("Escribe la coordenada x1: "))
x2 = int(input("Escribe la coordenada x2: "))
y1 = int(input("Escribe la coordenada y1: "))
y2 = int(input("Escribe la coordenada y2: "))

resultado = math.sqrt((x1-x2).__pow__(2)+(x1-x2).__pow__(2))

print(resultado)