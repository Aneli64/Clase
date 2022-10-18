'''
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
'''
import random

lista = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
          random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
          random.randint(0, 10), random.randint(0, 10)]

print(lista)

for item in lista:
    print("elemento al cuadrado -> ", pow(item, 2), "\n", " elemento al cubo -> ", pow(item, 3))