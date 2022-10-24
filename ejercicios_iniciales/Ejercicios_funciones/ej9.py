'''
Crear un programa para jugar a adivinar un número entre 0 y 100. Debe ofrecer cinco oportunidades
e indicar ante un fallo si el objetivo es menor, mayor o está muy cerca (a 2 de distancia o menos).
Se debe utilizar una función para comprobar si el número es el acertado o no.
'''

def juego(numero):
    intentos = 4
    numeroIN = int(input("Introduzca un numero -> "))
    while intentos != 0:
        if numeroIN != numero:
            numeroIN = int(input("incorrecto, introduzca otro \n "))
            intentos -= 1
        else:
            return "Numero correcto"
    return "Fin de intentos, numero no acertado"

print(juego(40))
#Falta lo de si es mayor, menor o esta cerca