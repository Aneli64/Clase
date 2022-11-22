'''
"nif;nombre;email;teléfono;teléfono,descuento\n

01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan JoséMartínez;juanjo@mail.com;664888233;5.2\n98376547F;CarmenSánchez;carmen@mail.com;667677855;15.7"
'''

entrada = input("directorio -> ")
lista = entrada.split(";")
dicClientes = {}

listaTemp = []
for i in range(0, len(lista)):  # Corregir las \n de por ahi en medio y lo del clear()
    if i % 4 != 0:
        listaTemp.append(lista[i])
    else:
        dicClientes[lista[i]] = listaTemp
        listaTemp.clear()


print(dicClientes)
