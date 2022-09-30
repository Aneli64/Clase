'''Escribir un programa que almacene la cadena de caracteres contraseña en
una variable, pregunte al usuario por la contraseña e imprima por pantalla
si la contraseña introducida por el usuario coincide con la guardada en la v
ariable sin tener en cuenta mayúsculas y minúsculas.
'''

password = "hola"
passwordIN = input("Introduzca su contraseña para acceder")

if passwordIN == password:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")