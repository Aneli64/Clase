'''
Desarrolla una aplicación que lea una frase del teclado y una palabra. en caso de que alguna
de las dos esté vacía lanzar una excepción NameError  con el mensaje “no se permiten vacíos”
Después mostrará las veces que aparece dicha palabra en esa frase y los lugares.
'''

frase = input("Frase: \n")
palabra = input("Palabra: \n")
listaFrase = frase.split()
contP = 0

for i in range(0, len(listaFrase)):
    if listaFrase[i] == palabra:
        contP += 1
print("Su palabra sale ", contP, "veces")