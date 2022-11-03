'''
https://plataforma.josedomingo.org/pledin/cursos/programacion_python3/curso/u29/
'''
'''
Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la 
siguiente información:

La temperatura media de cada día
Los días con menos temperatura
Se lee una temperatura por teclado y se muestran los días cuya 
temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.
'''

listaTempMin = []
listaTempMax = []
listaTempMedia = []

for i in range(0, 5):
    listaTempMin.append(int(input("Temperatura minima -> ")))
    listaTempMax.append(int(input("Temperatura maxima -> ")))
    listaTempMedia.append((listaTempMax[i] + listaTempMin[i]) / 2)

diaTempMin = min(listaTempMin).__index__()

print("Media de temperatura de cada dia -> ", listaTempMedia)
print("Dia con menos temperatura -> ", diaTempMin)