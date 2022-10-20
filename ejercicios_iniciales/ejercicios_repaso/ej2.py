'''
Rep2.Desarrolla una aplicación que pida al usuario una cadena y dos
letras. Después sustituirá una letra por otra. Primero sin replace y luego probar usarlo.
'''

frase = input("Frase: \n")
letra1 = input("primera letra: \n")
letra2 = input("segunda letra: \n")
nuevaFrase = ""

for i in range(0, len(frase)):
    if frase[i] == letra1:
        frase[i] == letra2
print(frase)
