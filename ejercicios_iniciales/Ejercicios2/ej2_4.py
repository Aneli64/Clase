'''Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
desea saber cuanto deberá pagar finalmente por su compra.'''

precioArt = float(input("Introduzca el precio de su articulo"))

desc = 0.15

precioConDescuento = precioArt - (precioArt*desc)

print("Su precio descontado seria de: ", precioConDescuento)
