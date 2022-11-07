
diasSemana = ["MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]
cajaSemanal = []
ventas = ""

for i in range(0, 6):
    caja = float(input("Dinero -> "))
    cajaSemanal.append(caja)

mediaSemanal = sum(cajaSemanal) / len(cajaSemanal)
diaMax = ""
diaMin = ""

if cajaSemanal[-1] > mediaSemanal:
    ventas = "SI"
elif cajaSemanal[-1] == mediaSemanal:
    ventas = "EMPATE"
else:
    ventas = "NO"

for i in range(0, len(cajaSemanal)):
    if cajaSemanal[i] == max(cajaSemanal):
        diaMax = diasSemana[i]
    if cajaSemanal[i] == min(cajaSemanal):
        diaMin = diasSemana[i]

print(diaMax, diaMin, ventas)
