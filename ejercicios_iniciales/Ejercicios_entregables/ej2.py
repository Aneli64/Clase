'''
De una cadena de caracteres de entrada, queremos conocer el número de
ocurrencias de cada carácter, cuál es la media de ocurrencia de los
caracteres y que carácter tiene una ocurrencia mayor,y la más próxima a la
media.
'''

cadena = input("Cadena: \n")
listaLetras = []
contLetras = []

for item in cadena:
    if item not in listaLetras:
        listaLetras.append(item)

print(listaLetras)