#ejercicio 4 Lucia Lopez

#Escriba un programa que pida dos números y luego muestre si el primero es divisible por el segundo.

nombre = input("ingrese su nombre: ")
print("hola " + nombre + " buenas dias")

nota1 = float(input("ingrese el dividendo: "))
nota2 = float(input("ingrese el divisor: "))
if nota2 == 0:
    print("no se puede dividir por 0")
else: 
    print(nota1//nota2)
