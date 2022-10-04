'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

password = "hola"
check = False

while not check:
    passwordIN = str(input("Introduzca la contraseña: \n"))
    if passwordIN == password:
        check = True
        print("Password correcta, acceso permitido")
    else:
        check = False
        print("Password incorrecta, intentelo de nuevo")
