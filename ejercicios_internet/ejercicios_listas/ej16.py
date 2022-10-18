'''
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4)
y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas.
Para simplificarlo vamos a suponer que febrero tiene 28 días.
'''

meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
nombreMeses = ["Enero" , "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
               "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input("Introduzca un numero para saber su mes y dias: \n"))

for i in range(0, 12):
    if mes not in meses:
        mes = int(input("Mes erroneo, introduzca uno de nuevo: \n"))
    elif mes == meses[i]:
        print("Su mes es", nombreMeses[i], "y tiene", dias[i], "dias")