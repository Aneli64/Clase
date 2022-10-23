'''
De una cadena de caracteres de entrada, queremos conocer el número de
ocurrencias de cada carácter, cuál es la media de ocurrencia de los
caracteres y que carácter tiene una ocurrencia mayor,y la más próxima a la
media.
'''

cadena = input("Cadena: \n")
listaLetras = []
contLetras = []
cadenaOrdenada = sorted(cadena)
cont = 1

for item in cadena:
    if item not in listaLetras:
        listaLetras.append(item)

for i in range(0, len(cadenaOrdenada)-1):
    if cadenaOrdenada[i] != cadenaOrdenada[i+1]:
        contLetras.append(cont)
        cont = 1
    else:
        cont += 1

#Añadimos manualmente el contador del ultimo elemento de la lista, ya que no puede comparar
# i con i+1 al estar este ultimo fuera de la lista
contLetras.append(len(cadenaOrdenada) - sum(contLetras))

media = sum(contLetras) / len(contLetras)
mayorOcurrencia = sorted(listaLetras)[len(listaLetras)-1]
print(sorted(listaLetras))

print("Mayor ocurrencia ", mayorOcurrencia, "con ", max(contLetras))
'''REHACER DE NUEVO, SOLO FUNCIONA CON EL CASO DE EJEMPLO DEL EJ'''