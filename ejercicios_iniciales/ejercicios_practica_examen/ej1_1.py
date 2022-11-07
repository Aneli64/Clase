'''
leer un número con decimales, y muestra la parte entera y la parte decimal separadas por una coma.
El ejercicio se considerará completo separando la parte entera de la decimal utilizando operaciones y conversiones (no utilizando una cadena para separar)
'''

numero = str(input("numero: "))
print(int(numero[:numero.index(".")]), ",", int(numero[numero.index(".")+1:len(numero)]))