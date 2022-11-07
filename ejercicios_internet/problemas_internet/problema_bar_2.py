
D = []
A = []
M = []
I = []
C = []
comidas = [D, A, M, I, C]

venta = str(input("Venta -> "))
while venta != "N 0":
    if venta.split(" ")[0] == "D":
        D.append(float(venta.split(" ")[1]))
    elif venta.split(" ")[0] == "A":
        A.append(float(venta.split(" ")[1]))
    elif venta.split(" ")[0] == "M":
        M.append(float(venta.split(" ")[1]))
    elif venta.split(" ")[0] == "I":
        I.append(float(venta.split(" ")[1]))
    elif venta.split(" ")[0] == "C":
        C.append(float(venta.split(" ")[1]))
    venta = str(input("Venta -> "))

maxVenta = max(sum(D), sum(A), sum(M), sum(I), sum(C))
minVenta = min(sum(D), sum(A), sum(M), sum(I), sum(C))

mediaVentas = 0
for i in range(0, len(comidas)):
    if len(comidas[i]) > 0:
        mediaVentas += (sum(comidas[i]) / len(comidas[i]))
mediaVentas /= len(comidas)

mensaje = ""
comidaMaxVenta = ""
comidaMinVenta = ""

for item in comidas:
    if item == maxVenta.__index__():
        comidaMaxVenta = item
    if item == minVenta.__index__():
        comidaMinVentaVenta = item

if (sum(D) / len(D)) > mediaVentas:
    mensaje = "SI"
elif (sum(D) / len(D)) < mediaVentas:
    mensaje = "NO"

print(comidaMaxVenta, comidaMinVenta, mensaje)
