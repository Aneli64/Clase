sensor = input("Sensor -> ")
letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
ubicacion = ""
temperatura = ""
temperaturaMayor = 0.0
ubicacionTempMayor = ""

sensor += "F"
for i in range(0, len(sensor)-1):
    if sensor[i] in letras:
        ubicacion += sensor[i]
    else:
        temperatura += sensor[i]
        if sensor[i + 1] in letras:
            print("lugar: ", ubicacion, "temperatura: ", temperatura)
            if float(temperatura) > temperaturaMayor:
                temperaturaMayor = float(temperatura)
                ubicacionTempMayor = ubicacion
            ubicacion = ""
            temperatura = ""

print("LA MAYOR TEMPERATURA ES", ubicacionTempMayor, "temperatura", temperaturaMayor)
