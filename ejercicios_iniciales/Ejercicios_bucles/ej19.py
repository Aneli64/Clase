'''
Mostrar un menú con tres opciones: 1-sumar dos números, 2- restar dos números, 3-finalizar programa.
A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige
una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada
cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto.
Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
'''

eleccion = input("Introduzca una opcion: |1-sumar dos números   2- restar dos números   3-finalizar programa.| \n")

while eleccion != "3":
    if eleccion =="1" or eleccion == "2":
        if eleccion == "1":
            print("Ha elegido sumar dos numeros. \n")
            primerNum = int(input("Introduzca un numero: "))
            segunNum = int(input("Introduzca un segundo numero: "))
            print("La suma de su numeros es -> ", primerNum + segunNum)

        elif eleccion == "2":
            print("Ha elegido restar dos numeros. \n")
            primerNum = int(input("Introduzca un numero: "))
            segunNum = int(input("Introduzca un segundo numero: "))
            print("La resta de sus numeros es -> ", primerNum - segunNum)
    else:
        print("Opcion no disponible")
    eleccion= input("Y ahora que quiere hacer: ")
print("Salir")