'''Pide al usuario dos números y muestra la “distancia” entre ellos
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
'''

valor1 = int(input("VALOR 1 = "))
valor2 = int(input("VALOR 2 = "))

res1 = valor1 - valor2
res2 = valor2 - valor1

if valor1 >= valor2:
    print("Su distancia es de: ", res1)
else:
    print("Su distancia es de: ", res2)
