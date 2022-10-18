'''
Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que
introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará
cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:

Todos lo alumnos mayores de edad.
Los alumnos mayores (los que tienen más edad)
'''

nombAlumnos = []
edadAlumnos = []
alumnosMayorDeEdad = []
alumnosMayores = []

nombre = str(input("Introduzca el nombre del alumno: \n"))

while nombre != "*":
    edad = int(input("Introduzca su edad: \n"))

    nombAlumnos.append(nombre) #Esto sigue siendo un poco guarro campeon
    edadAlumnos.append(edad)

    nombre = str(input("Introduzca el nombre del alumno: \n"))

for i in range(0, len(edadAlumnos)):
    if edadAlumnos[i] >= 18:
        alumnosMayorDeEdad.append(nombAlumnos[i])

for i in range(0, len(edadAlumnos)):
    if edadAlumnos[i] == max(edadAlumnos):
        alumnosMayores.append(nombAlumnos[i])

print("Los alumnos mayores de edad son -> ", alumnosMayorDeEdad)
print("El o los alumno(s) con mas edad es o son -> ", alumnosMayores)