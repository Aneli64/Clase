'''
Crear una función que calcule la longitud de una circunferencia.
'''

# Con el diametro
def longCircunfDiam(diametro):
    res = 3.14 * diametro
    return res

# Con el radio
def longCircunfRadio(radio):
    res = 2 * 3.14 * radio
    return res

print(longCircunfDiam(8))
print(longCircunfRadio(4))