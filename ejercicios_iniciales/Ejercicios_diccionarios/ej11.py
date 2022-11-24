"nif;nombre;email;teléfono;teléfono,descuento\n"
"01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan JoséMartínez;juanjo@mail.com;664888233;5.2\n98376547F;CarmenSánchez;carmen@mail.com;667677855;15.7"

entrada = input("directorio -> ")
lista = entrada.split(";")
dicClientes = {}

listaAtrib = []
listaClaves = []
for i in range(0, len(lista)):  # Corregir lo del clear()
    if i % 4 != 0:
        listaAtrib.append(lista[i])
    else:
        #dicClientes[lista[i]] = listaTempAtrib
        listaClaves.append(lista[i])

listaAtribClave = []
for i in range(0, len(listaClaves), 4):
    for j in range(0, len(listaAtrib)):
        listaAtribClave.append(listaAtrib[j])
    dicClientes[listaClaves[i]] = listaAtribClave
    listaClaves.clear()

print(dicClientes)
