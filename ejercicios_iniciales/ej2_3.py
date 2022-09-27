'''Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas,
el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas
que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.'''

sueldoBase = float(input("Introduzca su sueldo base: "))
com = 0.10

articulo1 = float(input("Introduzca el precio del primer articulo: "))
articulo2 = float(input("Introduzca el precio del segundo articulo: "))
articulo3 = float(input("Introduzca el precio del tercer articulo: "))

SalarioTotalMensual = sueldoBase + (articulo1*com + articulo2*com + articulo3*com)

print(SalarioTotalMensual)