'''
diseña el algoritmo contrario que de una cantidad te diga cuantas monedas de cada se deveulven.

Ejemplo 15.90

7 monedas de 2€

1 de 1 €

1 de 50 céntimos

2 de 20 céntimos
'''

dinero = float(input("Introduzca su dinero para saber su cambio -> "))

cont2 = 0
cont1 = 0
cont50 = 0
cont20 = 0

while dinero-2 >= 0:
    cont2 += 1
    dinero -= 2

while dinero-1 >= 0:
    cont1 += 1
    dinero -= 1

while dinero-0.50 >= 0:
    cont50 += 1
    dinero -= 0.50

while dinero-0.20 >= 0:
    cont20 += 1
    dinero -= 0.20

print("Su dinero es ", cont2, " moneda(s) de 2 euros, ", cont1, " moneda(s) de 1 euro, ", "\n",
      cont50," moneda(s) de 50 centimos y ", cont20, " moneda(s) de 20 centimos")