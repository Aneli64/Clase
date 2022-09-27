'''Ejercicio 10
Calcular la media de tres números pedidos por teclado.'''
from statistics import mean

valor = float(input('Introduzca un primer valor: '))
valor2 = float(input('Introduzca un segundo valor: '))
valor3 = float(input('Introduzca un tercer valor: '))

print((valor+valor2+valor3)/3)