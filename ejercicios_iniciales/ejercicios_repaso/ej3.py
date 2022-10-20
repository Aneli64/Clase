'''
Rep3 .Desarrolla una aplicación que pida al usuario una cadena y una
letra. Después borrará todas las apariciones de dicha letra y mostrará
el número de letras borradas.
'''

cadena = input("Cadena: \n")
letra = input("Letra: \n")
contLetra = 0
nuevaCadena = ""

for i in range(0, len(cadena)):
    if cadena[i] == letra:
        contLetra += 1
    else:
        nuevaCadena += cadena[i]

print("Palabra con letras borradas -> ", nuevaCadena, "\n", "Numero de letras borradas -> ", contLetra)