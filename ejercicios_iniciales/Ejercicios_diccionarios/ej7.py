'''
Escribir un programa que cree un diccionario simulando una cesta de la
compra. El programa debe preguntar el artículo y su precio y añadir el par al
diccionario, hasta que el usuario decida terminar. Después se debe mostrar
por pantalla la lista de la compra y el coste total, con el siguiente formato
'''

producto = input("Producto -> ")
precio = float(input("Precio -> "))

listaCompra = {}
while producto != "fin":
    listaCompra[producto] = precio
    producto = input("Producto -> ")
    precio = float(input("Precio -> "))

for c, v in listaCompra.items():
    print(f"{c} a {v} euros")

print(f"Total de la compra -> {sum(listaCompra.values())}")