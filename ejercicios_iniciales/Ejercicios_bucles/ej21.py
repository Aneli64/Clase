'''
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el
ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se
 debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si
 las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
'''

monto = float(input("Introduzca una compra: \n"))
suma = 0

while monto != 0:
    if monto > 0:
        suma += monto
    monto = float(input("Introduzca uno nuevo: \n"))

if suma > 1000:
    precioFinal = suma - (suma*0.10)
    print("Su importe total es -> ", precioFinal, " (Se le ha aplicado un descuento del 10%)")
else:
    print("Su importe total es -> ", suma)