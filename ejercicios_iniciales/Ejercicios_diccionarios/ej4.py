'''
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla
la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes. 11 enero 2022
“01” enero
“02” febrero
fecha =input(“introduce una fecha con formato dd/mm/aaaa” )
fechaLista=fecha.split(“/”)
'''

fecha = input("fecha -> ")
listaFecha = fecha.split("/")
diccionarioMeses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
                    7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre", }

print(f"{listaFecha[0]} de {diccionarioMeses[listaFecha]} {listaFecha[2]}")