'''Diseñar un algoritmo que nos diga el dinero que
tenemos (en euros y céntimos) después de pedirnos cuantas monedas
tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
'''
from math import trunc

monedas2 = int(input("monedas de 2€ --> "))
monedas1 = int(input("monedas de 1€ --> "))
monedas50 = int(input("monedas de 50cent --> "))
monedas20 = int(input("monedas de 20cent --> "))
monedas10 = int(input("monedas de 10cent --> "))

centimos = (((monedas2*2)+monedas1)*100) + (monedas50*50)+(monedas20*20)+(monedas10*10)

print("Su dinero total es: ", trunc(centimos/100), " euros" , centimos%100, " centimos")