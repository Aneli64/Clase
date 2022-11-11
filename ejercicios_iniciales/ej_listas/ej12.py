'''
Escribir un programa que almacene las matrices
A=((1,2,3),(4,5,6),(7,8,9)) y B=((−1,0,0),(1,1,1),(2,1,2)) en  listas
y muestre por pantalla las propias matrices con los números separados por espacios,
la suma de ambas, transponer filas por columnas su producto. Nota: Para representar matrices
mediante listas usar listas anidadas, representando cada vector fila en una lista.
(7,5,8  13,11,17   19,17,26)
'''

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[-1, 0, 0], [1, 1, 1], [2, 1, 2]]
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, len(A)):
    for j in range(0, len(A[i])):
        C[i][j] = (A[i][j] * B[i][j])

print(C)
