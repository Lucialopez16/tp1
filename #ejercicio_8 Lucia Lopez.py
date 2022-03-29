#ejercicio_8 Lucia Lopez

#nombre y apellido
vocales = 0
while vocales < 3:
    nombre = input("ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    nombrecompleto = nombre + apellido 
    vocales = 0
    for letra in nombrecompleto.lower():
        if letra == "a" or letra == "e" or letra =="i" or letra =="o" or letra =="u":
            vocales += 1

#año de nacimiento
error = 1
while error > 0:
    año_de_naciento = input("ingrese su año de nacimiento: ")
    error = 0
    while len(año_de_naciento) != 4:
        año_de_naciento = input("ingrese su año de nacimiento: ")

    for caracter in año_de_naciento:
        if caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter =="4" or caracter == "5": 
           continue
        else:
            error += 1
#contraseña
caracter_especial = 0

while caracter_especial < 1:
    caracter_especial = 0
    contraseña = input("ingrese una contraseña: ")
    while len(contraseña) <8 or len(contraseña) >16:
        contraseña = input("ingrese una contraseña: ")
    for caracter in contraseña:
        if caracter == "!" or caracter =="“" or caracter == "#" or caracter == "$" or caracter == "%" or caracter == "&":
            caracter_especial += 1

print(f"¡hola {nombre}{apellido}!")
