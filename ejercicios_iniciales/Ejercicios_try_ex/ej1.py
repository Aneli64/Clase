'''
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance
la excepción NameError con el mensaje, "Incorrect Password!!"
'''

try:
    password = "pestillo"
    passwordIN = input("password -> ")
    if passwordIN != password:
        raise NameError
except NameError:
    print("Incorrect Password!!")
