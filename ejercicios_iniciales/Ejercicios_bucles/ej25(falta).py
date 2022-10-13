'''
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga
(en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición:
se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más
'''

frase = input("Introduzca una frase: \n")
palabrasEnFrase = []

fraseList = frase.split(" ")

for item in fraseList:
    palabrasEnFrase.append(len(item))
maximo = max(palabrasEnFrase)

print(maximo)