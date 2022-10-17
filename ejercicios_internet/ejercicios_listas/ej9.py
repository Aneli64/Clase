'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal.
'''
'''
palabra = list(input("Palabra: \n"))
vocales = ["a", "e", "i", "o", "u"]
contA = 0
contE = 0
contI = 0
contO = 0
contU = 0

for item in palabra:
    if item == vocales[0]:
        contA += 1
    elif item == vocales[1]:
        contE += 1
    elif item == vocales[2]:
        contI += 1
    elif item == vocales[3]:
        contO += 1
    elif item == vocales[4]:
        contU += 1

print("Su palabra tiene: \n", "Vocales A -> ", contA, "\n", "Vocales E -> ", contE, "\n",  "Vocales I -> ", contI,
      "\n", "Vocales O -> ", contO, "\n", "Vocales U -> ", contU)
'''
#SOLUCION ALTERNATIVA MUCHO MEJOR (Solucion de ej de internet)
word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals:
    times = 0
    for letter in word:
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")

