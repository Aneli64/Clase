'''
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga
(en caso de haber más de una, mostrar la primera) y cuántas palabras había.
Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
'''

frase = input("Frase -> ")

listaPalabras = frase.split(" ")
palabra = ""
maxLenPalabra = 0
for item in listaPalabras:
    if len(item) > maxLenPalabra:
        palabra = item
        maxLenPalabra = len(item)

print("La palabra mas larga es -> ", palabra)

'''
#Esta no funciona ???
frase = input("Frase -> ")
contPalabra = 0
palabra = ""
palabraMax = 0
palabraFinal = ""

for item in frase:
    if item != " ":
        contPalabra += 1
        palabra += item
    else:
        if contPalabra > palabraMax:
            palabraMax = contPalabra
            palabraFinal = palabra
            #palabra = frase[frase.index(item):frase.index(" ")]
    contPalabra = 0
    palabra = ""

print("La palabra mas larga es -> ", palabraFinal)
'''











