#ejercicio_5 Lucia Lopez

from ast import Num


numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))
numero3 = float(input("ingrese el tercer numero: "))

if numero1>numero2 and numero1>numero3:
    print("el numero mas grande es: ", numero1)
elif numero2>numero1 and  numero2>numero3:
    print("el numero mas grande es: ", numero2)
elif numero3>numero1 and numero3>numero2: 
    print("el numero mas grande es: ", numero3)
else: 
    print("los numeros son iguales")