'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
'''

cuenta = float(input("Introduzca los ahorros de su cuenta: "))

ahorrosPrimerAno = round(cuenta + (cuenta*0.04),2)
ahorrosSegundoAno = round(ahorrosPrimerAno + (ahorrosPrimerAno*0.04),2)
ahorrosTercerAno = round(ahorrosSegundoAno + (ahorrosSegundoAno*0.04),2)

print("Los ahorros de su cuenta alfinal de los proximos 3 años son los siguientes: ", "Ano 1: ", ahorrosPrimerAno, "Ano 2: ", ahorrosSegundoAno, "Ano 3: ", ahorrosTercerAno)