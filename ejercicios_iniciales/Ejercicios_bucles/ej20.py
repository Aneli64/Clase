'''
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase).
Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide,
indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar.
Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
'''

frase = input("Introduzca una frase: \n")
letra = input("Introduzca una letra para comprobar si se encuentra en la frase: \n")

for i in range(0, len(frase)):
    if letra == frase[i]:
        print("En la posicion", i, "se encuentra una coincidencia con su letra")
        break
    else:
        print("No hay coincidencia en la posicion ", i)