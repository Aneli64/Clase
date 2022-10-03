'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
los años que ha cumplido (desde 1 hasta su edad).'''

edad = int(input("Introduzca su edad -> "))

for i in range(0, edad):
    print("Ha cumplido ", i, " años", "\n")