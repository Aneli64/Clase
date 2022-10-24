'''
Crear una función que devuelva si un año es bisiesto.
'''


def bisiesto(año):
    if año % 4 == 0 or año % 100 == 0 or año % 400 == 0:
        return True
    else:
        return False


print(bisiesto(2020))
