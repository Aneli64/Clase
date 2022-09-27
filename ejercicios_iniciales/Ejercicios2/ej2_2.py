'''Ejercicio 11
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas
horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.'''
from math import trunc

minutosIn = float(input("Introduce minutos: "))

horas = trunc(minutosIn/60)
minutos = trunc(minutosIn%60)
segundos = trunc(minutos%60)


print(horas, minutos, segundos)

''' SACAR HORAS, MINUTOS Y SEGUNDOS (FALTA TERMINARLO)
segundosIn = float(input("Introduce segundos: "))

horas = segundosIn/3600
minutos = horas%3600

print(horas, minutos)
'''

# Hacer casa con dias y hacerlo al reves (de dias a segundos, y de segundos a dias)