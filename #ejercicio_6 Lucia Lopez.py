#ejercicio_6  Lucia Lopez 

from tkinter import N


sep = "-"
n = []
sep = " - "
a = 6
print ("Cuantos nombres quieres escribir: ")
cantidadn = int(input())
i = 0
while i < cantidadn:
    print ("Ingrese el nombre de uno de sus amigos " ,i + 1 )
    nombre = (input())
    n.append (nombre)
    i += 1

n.sort()

print (*n, sep = "-")

print("fin")