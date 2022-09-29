'''Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un
 algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final
 las dos variables.
'''

A = input("Introduce el valor de A: ")
B = input("Introduce el valor de B: ")

C=B
B=A
A=C

print("Valor de A --> ", A, "Valor de B --> ", B)

