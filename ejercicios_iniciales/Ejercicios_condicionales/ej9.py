'''
crear un programa  'Ascensor' que estará en una planta leida por teclado o
aleatoria y pregunte si quieres subir o bajar ‘S’ o ‘B’ y en tal caso cuántos pisos,
para impedir que vaya por debajo de la planta 0 (si se intenta, quedaría en la planta 0)
y que suba más allá de la planta 10 (Si se intenta quedaría en la planta 10).
nota si queres hacerlo con una planta aleatoria
'''

import random

piso_inicio = random.randint(0, 10)
print("Su piso de inicio es -> ", piso_inicio)

subirBajar = input("Desea subir o bajar [S, B] -> ")
if subirBajar == "S":
    subirPiso = int(input("Introduzca los pisos que desea subir -> "))
    piso_final = piso_inicio + subirPiso
elif subirBajar == "B":
    bajarPiso = int(input("Introduzca los pisos que desea bajar -> "))
    piso_final = piso_inicio - bajarPiso
else:
    print("Opcion no disponible")

if piso_final > 10:
    piso_final = 10
    print("Se encuentra en el piso 10 (No puede subir mas de la planta 10)")
elif piso_final < 0:
    piso_final = 0
    print("Se encuentra en el piso 0 (No puede bajar mas de la planta 0)")
else:
    print("Se encuentra en el piso ", piso_final)