'''SUMAR DOS CADENAS GRANDES'''

cadena1 = str(input("cadena -> "))
cadena2 = str(input("cadena -> "))
cadenaResultado = ""
cadenaMin = min(cadena2, cadena1)
cadenaMax = max(cadena2, cadena1)
resto = 0

'''
# Añadimos ceros a la lista minima (no olviar usar condicional en el caso de que sean iguales no añada ceros * la diferencia, ya que no hay diferencia de len)
cadenaMin += "0" * (len(cadenaMax) - len(cadenaMin))
cadenaFinalMin = cadenaMin[cadenaMin.index("0"):] + cadenaMin[0:cadenaMin.index("0")]
'''

for i in range(len(cadenaMax), 0, -1):
    numeroSumado = int(cadenaMin[i-1]) + int(cadenaMax[i-1]) + resto
    if numeroSumado > 9:
        resto = 1
        numeroSumado -= 10
        cadenaResultado += str(numeroSumado)
        numeroSumado = 0
    else:
        cadenaResultado += str(numeroSumado)
        resto = 0

cadenaFinal = ""
for item in reversed(cadenaResultado):
    cadenaFinal += item

print(cadenaFinal)
