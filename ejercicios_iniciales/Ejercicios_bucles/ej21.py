'''
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el
ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se
 debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si
 las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
'''

monto = float(input("Introduzca una compra: \n"))
total = monto

while monto != 0:
    if monto < 0:
        monto = float(input("Precio no valido, introduzca uno nuevo: \n"))
    elif monto > 0:
        monto = float(input("Ingrese nueva compra: \n"))
        total += monto
        print(monto)

if total > 1000:
    precioFinal = total - (total*0.10)
    print("Su importe total es -> ", precioFinal, " (Se le ha aplicado un descuento del 10%)")
else:
    print("Su importe total es -> ", total)