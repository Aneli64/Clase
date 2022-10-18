'''
Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno,
pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
'''

lista1 = []
lista2 = []
lista3 = []

while len(lista1) < 5:
    valorLista1 = int(input("Valor para lista1 -> "))
    lista1.append(valorLista1)

while len(lista2) < 5:
    valorLista2 = int(input("Valor para lista2 -> "))
    lista2.append(valorLista2)

for i in range(0, 5):
    lista3.append(lista1[i]+lista2[i])

print(lista1)
print(lista2)
print(lista3)