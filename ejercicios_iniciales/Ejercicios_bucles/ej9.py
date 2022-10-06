'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

password = "hola"
passwordIN = str(input("Introduzca la contraseña: \n"))

while passwordIN != password:
    print("Contraseña incorrecta")
    passwordIN = str(input("Introduzca la contraseña: \n"))

print("Contraseña correcta")

