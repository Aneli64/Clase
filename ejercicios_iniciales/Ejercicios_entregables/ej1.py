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

diaF1 = dia1 + (30 * mes1)
diaF2 = dia2 + (30 * mes2)

diferenciaAños = max(año2, año1) - min(año2, año1)
diasFinales = (diferenciaAños * 360) + abs(diaF1 - diaF2)

print("Su diferencia de dias son -> ", diasFinales)
print("Su diferencia de fechas es -> ", )