'''
Escribir un programa que pida al usuario un texto y muestre por pantalla el número de
veces que contiene cada letra.
'''

texto = input("Texto -> ")

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cont = 0
listaLetras = []
listaCont = []

for item in abecedario:
    if item in abecedario and item not in listaLetras:
        cont += 1
        listaLetras.append(item)
