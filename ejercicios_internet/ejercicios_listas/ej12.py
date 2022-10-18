'''
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado.
Copia los elementos de la lista en otra lista pero en orden inverso,
y muestra sus elementos por la pantalla.
'''

listaCadenas = []
listaCadenasInv = []
palabra = " "

for i in range(0, 5):
    cadena = (input("Introduzca un conjunto de caracteres: \n"))
    listaCadenas.append(cadena)

for item in listaCadenas:
    for i in reversed(item):
        palabra += i
    listaCadenasInv.append(palabra)
    palabra = " "

print(listaCadenasInv)