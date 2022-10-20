'''
Rep1.Realiza una aplicación que pida el nombre y los 2 apellidos de un
usuario y genere su nombre de usuario formado por la inicial de su
nombre y las tres primeras letras de sus dos apellidos.
'''

nombre = input("Nombre: \n")
apellido1 = input("Primer apellido: \n")
apellido2 = input("Segundo apellido: \n")

print(nombre[0] + apellido1[0:3] + apellido2[0:3])