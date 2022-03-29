#ejercicio_10 Lucia Lopez

import random
from socket import NI_NUMERICHOST

intentos_realizados=0
print("¡hola! ¿como te llamas?")
nombre=input()

número = random.randint(1, 25)
print("Bueno," + nombre +  ", estoy pensando en un número entre 1 y 25.")

while intentos_realizados<5: 
    print("intenta adivinar ")
    estimacion=input()
    estimacion=int(estimacion)

    intentos_realizados=intentos_realizados+1
    if estimacion <número:
        print("tu estimacion es muy baja")
    if estimacion>número: 
        print("tu estimacion es muy alta")
    if estimacion ==número:
        break
if estimacion == número:
    intentos_realizados=str(intentos_realizados)
    print("Buen trabajo ", nombre, "has adivinado mi numero en ", intentos_realizados, "intentos")

if estimacion !=número:
    número=str(número)
    print("has fallado porque el numero que estaba pensando era: ",número )
