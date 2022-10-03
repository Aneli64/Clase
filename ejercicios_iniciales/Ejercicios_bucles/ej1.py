'''
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''

palabra = input("Introduzca una palabra a repetir 10 veces -> ")

repetir = (palabra + "\n") * 10
print(repetir)

'''
for i in range(0, 10):
    print(palabra + "\n")
'''