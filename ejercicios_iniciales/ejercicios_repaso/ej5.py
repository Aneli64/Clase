'''
Rep5
Crea un programa que lea dos  cadenas y las mezcle en una tercera, ejemplo:
'''

cadena1 = input("primera cadena: \n")
cadena2 = input("segunda cadena: \n")
cadenaRes = ""
maxCadena = max(len(cadena1), len(cadena2))
minCadena = min(len(cadena1), len(cadena2))
rango = maxCadena - minCadena

for i in range(0, maxCadena):
    cadenaRes += cadena1[i] + cadena2[i]

for i in range(rango, len(maxCadena)):
    cadenaRes += maxCadena[i]
print(cadenaRes)
print(rango)
print(maxCadena)
print(minCadena)