'''
Dada una matriz no vacía de enteros, devuelva el resultado de multiplicar los valores en orden.
Ejemplo:
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''


def grow(arr):
    cont = 1
    for item in arr:
        cont *= item
    return cont


print(grow([1, 2, 3, 4]))
