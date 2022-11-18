'''
Escribir un programa que guarde el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa
no está en el diccionario.
'''

diccionario = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
divisa = input("Introduzca una divisa -> ")
print(diccionario[divisa])

