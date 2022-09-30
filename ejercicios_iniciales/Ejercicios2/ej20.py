'''Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados
por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer
un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas
velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el
vehículo más rápido al otro.
'''

velCoch1 = float(input("Introduzca la velocidad del primer coche: "))
velCoch2 = float(input("Introduzca la velocidad del segundo coche: "))
distancia = float(input("Distancia: "))

tiempo = 0

while velCoch2 < distancia:
    velCoch2 += velCoch2
    distancia += velCoch1
    tiempo += 1
    
print("Ha tardado ", tiempo*60, " minutos en alcanzarle")
