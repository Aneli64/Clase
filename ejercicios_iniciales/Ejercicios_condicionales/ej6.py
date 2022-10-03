'''
En una determinada empresa, sus empleados son evaluados al final de cada año.
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel               Puntuación
Inaceptable         0.0
Aceptable           0.4
Meritorio           0.6

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento,
y mostrar la cantidad de dinero que recibirá el usuario.
'''

# Posible bucle para que el usuario introduzca solo puntuaciones de 0.0, 0.4, 0.6 o superior
puntuacion = float(input("Introduzca su puntuacion -> "))

if puntuacion == 0.0:
    print("Puntuacion [Inaceptable], su salario es -> ", puntuacion * 2400.0)
elif puntuacion == 0.4:
    print("Puntuacion [Aceptable], su salario es -> ", puntuacion * 2400.0)
elif puntuacion >= 0.6:
    print("Puntuacion [Meritorio], su salario es -> ", puntuacion * 2400.0)
else:
    print("Puntuacion no valida")
