'''
Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso
al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga
sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos
numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea).
Finalmente, informar cuántas líneas completas se ingresaron.
'''

libro = input("Libro: ")
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
contNumeros = 0
contLineas = 0

while libro != "*":
    for i in range(0, len(libro)):
        if libro[i] == "/":
            contLineas += 1
            print("Linea completa. Aparecen", contNumeros, "digitos numericos")
        elif libro[i] in numeros:
            contNumeros += 1
    contLineas += 1
    libro = input("Libro: ")

print("Fin. Se leyeron", contLineas + 1, "lineas completas")
