'''
Leemos una cadena y una palabra objetivo.
Si la cadena tiene un tamaño menor a la palabra lanzar una excepción con el mensaje
“la cadena no puede ser menor a la palabra”, y salimso del programa.
Busca de la cadena la palabra que más se parezca a la palabra objetivo.
Una palabra se parece más a otra si coinciden más letras comenzando
desde el principio(en el momento que una letra no coincida no seguimos comparando).
'''

cadena = input("cadena: \n")
palabraObjetivo = input("palabra objetivo: \n")

listaCadena = cadena.split(" ")
cont = 0
listaContadores = []

palabMaxCoinc = ""
numMaxCoinc = 0

for item in listaCadena:
    for i in range(0, len(palabraObjetivo)):
        if i == len(item):
            break
        else:
            if item[i] == palabraObjetivo[i]:
                cont += 1
            else:
                listaContadores.append(cont)
                if listaContadores[-1] == max(listaContadores):
                    numMaxCoinc = listaContadores[-1]
                    palabMaxCoinc = item
                cont = 0

print(palabMaxCoinc, numMaxCoinc)

'''
cadena = input("cadena: \n")
palabraObjetivo = input("palabra objetivo: \n")

palabra = ""
cont = 0
palabraMax = ""
numPalabraMax = 0
listaCont = []
palabraMaxFinal = 0

for i in range(0, len(cadena)): #otro bucle hasta que aparezca espacio???
    palabra += cadena[i]
    if cadena[i] == " ":
        listaCont.append(numPalabraMax)
        if numPalabraMax > listaCont[-1]:
            palabraMax = palabra
            palabraMaxFinal = numPalabraMax
            palabra = ""
    if cadena[i] == palabraObjetivo[i]:
        cont += 1
    else:
        if cont > numPalabraMax:
            numPalabraMax = cont
            cont = 0

print(palabraMax, palabraMaxFinal)
'''