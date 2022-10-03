'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión cada año
que dura la inversión.

# Formula para calcular El capital tras un año.

amount *= 1 + interest / 100

# En donde:

# - amount: Cantidad a invertir

# - interest: Interes porcentual anual
'''

cantidad = int(input("Introduzca una cantidad a invertir -> "))
interesAnual = int(input("Introduzca su interes anual -> "))
numeroAños = int(input("Introduzca el numero de años -> "))

capitalObt = 0

for i in range(0, numeroAños):
    capitalObt += cantidad + (cantidad*(interesAnual/100))
    print("Capital obtenido -> ", capitalObt, "[", i+1, " año]")