'''
Rep5
Crea un programa que lea dos  cadenas y las mezcle en una tercera, ejemplo:
'''

cadena1 = input("primera cadena: \n")
cadena2 = input("segunda cadena: \n")
cadenaRes = ""
minCadena = min(len(cadena1), len(cadena2))

for i in range(0, minCadena):
    cadenaRes += cadena1[i] + cadena2[i]
cadenaFinal = cadenaRes + cadena2[len(cadena1):len(cadena2)]

print(cadenaFinal)
