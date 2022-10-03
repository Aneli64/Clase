'''
Hacer un método que según la nota float leída, devuelva una calificación:
 Si la nota es menor que 5 ->	"suspenso".
 Si la nota está entre 5 y 6 ->	"aprobado".
 Si la nota está entre 6 y 7 ->	"bien".
 Si la nota está entre 7 y 8 ->	"notable".
 Si la nota es mayor que 8  ->	"sobresaliente".
Añadir un método main a la clase para probar el método.
'''

nota = float(input("Introduzca su nota para saber su calificacion -> "))
calificaciones = ["suspenso","aprobado","bien","notable","sobresaliente"]

if nota < 5.0:
    print(calificaciones[0])
elif 5.0 < nota < 6:
    print(calificaciones[1])
elif 6.0 < nota < 7:
    print(calificaciones[2])
elif 7.0 < nota < 8:
    print(calificaciones[3])
elif nota > 8.0:
    print(calificaciones[4])
