'''
Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso
al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga
sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos
numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea).
Finalmente, informar cuántas líneas completas se ingresaron.
'''

libro = input("Libro: \n")
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

while libro != "*":
    contNum = 0
    linComp = 0
    if libro != "/":
        for i in range(0, len(libro)):
            if libro[i] in numeros:
                contNum += 1
                linComp += 1
        libro = input("Libro: \n")
    else:
        print("Linea completa. Aparecen ", contNum, "digitos numericos")

print("Fin. Se leyeron ", linComp, "lineas completas")
