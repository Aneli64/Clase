'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.
'''

frase = str(input("Introduzca una frase: \n"))
letra = str(input("Introduzca una letra para saber cuantas veces esta contenida en su frase: \n"))

contLetra = 0

for i in frase:
    if letra == i:
        contLetra += 1

if contLetra == 1:
    print("Su letra ha aparecido ", contLetra, " vez")
else:
    print("Su letra ha aparecido ", contLetra, " veces")
