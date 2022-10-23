'''
Leemos día, mes, año de tipo entero (para simplificar todos los meses los consideraremos de
30 días y todos los años de 365 días para toda la actividad) para dos fechas.
(no tiene por qué ser la primera fecha anterior a la segunda)
Calcularemos el periodo de tiempo entre las fechas ,no importa que fecha sea menor devuelve
el periodo de tiempo entre ambas como valor absoluto
'''

dia1 = int(input("Dia -> "))
mes1 = int(input("Mes -> "))
año1 = int(input("Año -> "))

dia2 = int(input("Dia -> "))
mes2 = int(input("Mes -> "))
año2 = int(input("Año -> "))

diaF = dia1 - dia2
mesF = mes1 - mes2
añoF = año1 - año2

print(abs(diaF), "dias/", abs(mesF), "meses/", abs(añoF), "años")