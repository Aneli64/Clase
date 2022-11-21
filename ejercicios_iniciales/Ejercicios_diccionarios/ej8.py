'''
Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas. El programa debe crear un
diccionario con las palabras y sus traducciones. Después pedirá una frase en español y
utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el
diccionario debe dejarla sin traducir.
'''

dicEspIng = {}
palabraTraduc = input("Introduzca una palabra en español y su traduccion (Formato -> hola:hello | 'fin' para salir): \n")

while palabraTraduc != "fin":
    palabraEsp = palabraTraduc.split(":")[0]
    palabraIng = palabraTraduc.split(":")[1]
    dicEspIng[palabraEsp] = palabraIng
    palabraTraduc = input("Introduzca una palabra en español y su traduccion (Formato -> hola:hello | 'fin' para "
                          "salir): \n")

fraseEspañol = input("Introduzca una frase en español para ser traducida palabra por palabra: \n")
palabrasEsp = fraseEspañol.split(" ")

listaPalabrasTraducidas = []
for item in palabrasEsp:
    if item in dicEspIng.keys():
        listaPalabrasTraducidas.append(dicEspIng[item])
    else:
        listaPalabrasTraducidas.append(item)

print(listaPalabrasTraducidas)