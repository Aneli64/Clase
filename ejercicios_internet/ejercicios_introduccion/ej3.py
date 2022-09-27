'''Una panadería vende barras de pan a 3.49€ cada una.
El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
'''

precioPanDia = 3.49
precioPanNoDia = precioPanDia - (precioPanDia*0.6)

numeroDePanesDia = int(input("Introduzca el numero de panes del dia que desea comprar: "))
numeroDePanesNoDia = int(input("Introduzca el numero de panes no del dia que desea comprar: "))

precioTotalPanesDia = round(numeroDePanesDia * precioPanDia)
precioTotalPanesNoDia = round(numeroDePanesNoDia * precioPanNoDia)
print("El importe total a pagar seria de:", (precioTotalPanesDia + precioTotalPanesNoDia), "(precio total del pan del dia = ", precioTotalPanesDia, ")", "(precio total pan no del dia = ", precioTotalPanesNoDia, ")")