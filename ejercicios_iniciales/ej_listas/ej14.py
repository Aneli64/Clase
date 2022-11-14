'''
Pide los datos de una camiseta talla y color y comprueba que la talla sea S M L XL y
el color introduce los valores posibles en una tupla
'''

tallas = ("S", "M", "L", "X")
colores = ("verde", "rojo", "amarillo")

print(f"Tallas disponibles -> {tallas} \n "f"Colores disponibles -> {colores}")
camisetaTalla = input("Introduce una talla: ")
camisetaColor = input("Introduce un color: ")

while camisetaTalla not in tallas:
    camisetaTalla = input("Talla no valida, introduzca una nueva: ")

while camisetaColor not in colores:
    camisetaColor = input("Color no valido, introduza uno nuevo: ")

print(f"Camiseta talla {camisetaTalla} de color {camisetaColor} disponible")