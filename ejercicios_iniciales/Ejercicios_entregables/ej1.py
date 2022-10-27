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

diaMax = max(dia1, dia2)
diaMin = min(dia1, dia2)
mesMax = max(mes1, mes2)
mesMin = min(mes1, mes2)
añoMax = max(año1, año2)
añoMin = min(año1, año2)

diasDiferencia = abs((dia1 + (mes1 * 30)) - (dia2 + (mes2 * 30)))
dias = abs((30 - dia1) - (30 - dia2))
añosDiferencia = abs(año1 -año2)
contMesesDiferencia = 0
diasDiferenciaTotal = diasDiferencia

while diasDiferenciaTotal - 30 >= 0:
    contMesesDiferencia += 1
    diasDiferenciaTotal -= 30

print("periodo entre fechas \n", diasDiferenciaTotal, "dias", contMesesDiferencia, "meses", añosDiferencia, "años")

