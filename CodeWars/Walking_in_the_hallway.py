'''
Eres un guardia de seguridad en una gran empresa, tu trabajo es vigilar las cámaras.
Cuando te aburres, decides hacer un juego con las personas que caminan en un pasillo en
una de las cámaras. A medida que muchas personas pasan por el pasillo, decides calcular
los pasos mínimos que tomarán antes de que 2 personas se crucen o entren en contacto entre sí
(suponiendo que todas las personas den un paso al mismo tiempo).
Las personas se representan como flechas, "<" para una persona que se mueve hacia la izquierda
y ">" para una persona que se mueve hacia la derecha y "-" para un espacio vacío
'''

def contact(hallway):
    # Good luck :D
    pass

#entrada = ">-----<-->--<-----"
entrada = ">---------------<--------------------------<-------->---------<------->----------<----<---->>----------<------->>>---------------<<------>"

people1 = entrada.index(">")
people2 = entrada.index("<")



'''
contDist = 0
listContDistancias = [] 
people1 = entrada.index(">")

for i in range(people1, len(entrada)):
    try:
        if entrada[i] == ">":
            contDist = 0
        if entrada[i + 1] != "<":
            contDist += 1
        else:
            listContDistancias.append(contDist)
            contDist = 0
    except IndexError:
        break

print(listContDistancias)
listContDistancias.remove(listContDistancias[-1])
distanciaF = min(listContDistancias)
print(distanciaF)
steps = 0
while distanciaF > 0:
    distanciaF -= 2
    steps += 1

print(steps)
'''