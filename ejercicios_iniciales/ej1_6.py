'''Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por
pantalla el precio final del artículo.'''

artSinIVA = float(input("Introduzca el precio del articulo sin IVA = "))

precioFinal = artSinIVA + (artSinIVA * 0.10)

print(precioFinal)