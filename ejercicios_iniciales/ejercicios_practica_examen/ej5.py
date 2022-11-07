'''
Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene
multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
'''

numero = int(input("Numero -> "))

for i in range(1, numero):
    numero *= i

print(numero)

# Sucesion de Fibonacci
'''
n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(8):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
'''