'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y
todos los ingredientes que lleva.
'''

ingredientes = ["Pimiento", "Tofu", "Peperoni", "Jamon", "Salmon"]
vegetariana = ["Pimiento", "Tofu", "Peperoni"]
no_vegetariana = ["Jamon", "Salmon"]

print("Ingredientes disponibles -> ", ingredientes)

eleccion = input("Eliga un solo ingrediente de los mostrados [mozzarella y tomate ya incluidos] \n")
if eleccion in vegetariana:
    print("Su pizza es vegetariana")
elif eleccion in no_vegetariana:
    print("Su pizza no es vegetariana")
else:
    print("Ingrediente no disponible")