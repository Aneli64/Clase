'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
y el valor será con los datos del cliente en una lista
(nombre, dirección, teléfono, correo, preferente True o False),
donde preferente tendrá el valor True si se trata de un cliente preferente.
El programa debe preguntar al usuario por una opción del siguiente menú:
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente,
(4) Listar todos los clientes, (5) Listar clientes preferentes,
(6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
'''

# Hacer funciones para que quede mas limpio

entradaMenu = int(input("Elija una opcion -> (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar "
                        "todos los clientes, (5) Listar clientes preferentes, (6) Terminar \n"))

dicDatos = {}
datosCliente = []

while entradaMenu != 6:
    if entradaMenu == 1:
        nifcliente = input("Introduzca su NIF -> ")
        nombre = input("Nombre -> ")
        direccion = input("Direccion -> ")
        telefono = input("telefono -> ")
        correo = input("correo -> ")
        preferente = bool(input("preferente -> ")) # Mirar esto, no va la opcion 5 del menu
        datosTemp = [nifcliente, nombre, direccion, telefono, correo, preferente]

        datosCliente.extend(datosTemp)
        dicDatos[nifcliente] = datosTemp
    elif entradaMenu == 2:
        nifAeliminar = input("Introduzca un NIF para eliminar sus datos -> ")
        if nifAeliminar in dicDatos.keys():
            del dicDatos[nifAeliminar]
        else:
            print("NIF no encontrado...")
    elif entradaMenu == 3:
        datosAmostrar = input("Introduzca un NIF para mostrar sus datos -> ")
        if datosAmostrar in dicDatos.keys():
            print(f'Datos del NIF ({datosAmostrar}): \n {dicDatos[datosAmostrar]}')
        else:
            print("NIF no encontrado...")
    elif entradaMenu == 4:
        for c, v in dicDatos.items():
            print(f"Datos del NIF {c}: \n {v}")
    elif entradaMenu == 5: # Este es el unico que falla
        for c, v in dicDatos.items():
            if v[preferente]:
                print(f"Datos del NIF {c}: \n {v}")
    entradaMenu = int(
        input("Elija una opcion -> (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar "
              "todos los clientes, (5) Listar clientes preferentes, (6) Terminar \n"))
