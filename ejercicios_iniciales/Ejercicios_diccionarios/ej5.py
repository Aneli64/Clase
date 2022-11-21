'''
Escribir un programa que almacene el diccionario con las horas de las
asignaturas de un curso leeremos por teclado asignatura y horas hasta que el
usuario escriba fin {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por
pantalla los créditos de cada asignatura en el formato <asignatura> tiene
<créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y
<créditos> son sus créditos. Al final debe mostrar también el número total de
créditos del curso.
'''

asig = input("Asignatura -> ")
horas = input("Horas -> ")

dicAsig = {}
while asig != "fin":
    dicAsig[asig] = horas
    asig = input("Asignatura -> ")
    horas = input("Horas -> ")

for c, v in dicAsig.items():
    print(f"{c} tiene {v} horas")