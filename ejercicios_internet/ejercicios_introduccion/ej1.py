'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra
por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g
y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.'''

payasos = int(input("Introduzca el numero de payasos que desea adquirir: "))
muñecas = int(input("Introduzca el numero de muñecas que desea adquirir: "))

payasoG = 112
muñecaG = 75

print("El peso total de su pedido sera de: ", (payasos*payasoG)+(muñecas*muñecaG), " gramos")