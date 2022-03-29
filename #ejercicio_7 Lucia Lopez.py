#ejercicio_7 Lucia Lopez
import string


nombre1 = []

nombre1 = (input("ingrese su nombre: "))
nombre12 = (input("ingrese su apellido: "))
nombre13 = float(input("ingresa tu edad: "))
if nombre13 <35:
    print("")
nombre14 = float(input("ingresa la cantidad de dinero que tenes en tu billetera: "))
nombre15 = float(input("ingrese del 0 al 10 la cantidad de habre que tiene: "))

if nombre13 <35:
    print("hola ", nombre1, "eres una persona joven ya que tienes", nombre13)
elif nombre13 >34 and nombre14 > 500 and nombre15 > 5:
    print("hola", nombre1, nombre12, "¿hoy hay asado?")
elif nombre13 < 18 and nombre14 < 100 and nombre15 >= 7:
    print("hola", nombre1, nombre12, "¿hoy vas a comer a lo de tus padres?")


