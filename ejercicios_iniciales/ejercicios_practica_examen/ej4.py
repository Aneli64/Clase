'''
Solicitar al usuario que ingrese una frase y luego imprimir
un listado de las vocales que aparecen en esa frase (sin repetirlas).
'''

frase = input("Frase -> ")
vocalesAparecidas = ""

for item in frase:
    if item in "aeiou" and item not in vocalesAparecidas:
        print(item)
        vocalesAparecidas += item


frase = input("Frase -> ")
contVocales = 0

for item in frase:
    if item in "aeiou":
        contVocales += 1

print("Cantidad de vocales -> ", contVocales)