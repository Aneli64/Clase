'''
Lee dos cadenas de un formulario, que representan la parte entera y decimal de un importe,
conviértelo en un valor float y aplícale el iva de l21% y muestra el total a pagar (iva incluido)
'''

cadena1 = input("parte entera -> ")
cadena2 = input("parte decimal -> ")

cadenaFinal = float(cadena1 + "." + cadena2)
cadenaConIva = round(cadenaFinal + (cadenaFinal * 0.21), 2)
print(cadenaConIva)
