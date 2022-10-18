'''
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga
(en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición:
se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más
'''

contLetra = 0
mayorPalabra = 0
frase = input("Introduzca una frase: \n")

for i in range(0, len(frase)):
    if frase[i] != " ":
        contLetra += 1
    else:
        if contLetra >= mayorPalabra:
            mayorPalabra = contLetra
            contLetra = 0

print("Su palabra mas grande mide -> ", mayorPalabra)
