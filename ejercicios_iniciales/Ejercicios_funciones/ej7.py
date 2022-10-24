'''
Crear una función que reciba como argumentos dos fechas, y devuelva como resultado
los años completos de diferencia entre las dos.
'''


def difFecha(fecha1, fecha2):
    fechaF = fecha1 - fecha2
    return abs(fechaF)


print(difFecha(2021, 2030))
