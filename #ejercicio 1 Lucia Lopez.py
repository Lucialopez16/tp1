#ejercicio 1 Lucia Lopez

#Si la materia tiene como promedio un 8 o más Materia promocionada.
#Si la materia tiene como promedio una nota menor a 8 pero mayor o igual a 6 Materia aprobada.
#Si la materia tiene como promedio una nota menor que 6: Materia desaprobada.
valor_de_materias= 0
while valor_de_materias!=7:
    valor_de_materias = int(input("ingrese la cantidad de materia:"))

print("hola")

print ("ingrese las notas\ nOrden de carga: \n1 Matematica \n2 Biologia \n3 Quimica \n4 historia \n5 tecnologia \n6 economia \n7 construccion de la ciudadania")
cursadamatematica=0
cursadabiologia=0
cursadaquimica=0
cursadahistoria=0
cursadatecnologia=0
cursadaeconomia=0
cursadaconstrucciondelaciudadania=0
cursadageneral=0

nota1m = float(input("ingrese la primer nota de matematica: "))
nota2m = float(input("ingrese la segunda nota de matematica: "))
nota3m = float(input("ingrese la tercera nota de matematica: "))
promediom = (nota1m + nota2m + nota3m)/3

if promediom >= 8: 
    print("tu promedio es de: ", promediom) 
    print("promocionaste matematica")
    cursadamatematica = promediom 

elif promediom <8 and promediom >=6: 
    print("tu promedio es de: ", promediom)
    print("aprobaste matematica pero rendis el final")

else :
    print("tu promedio es de: ", promediom)
    print("desaprobaste matematica")

nota1b = float(input("ingrese la primer nota de biologia: "))
nota2b = float(input("ingrese la segunda nota de biologia : "))
nota3b = float(input("ingrese la tercera nota de biologia : "))
promediob = (nota1b + nota2b + nota3b)/3

if promediob >= 8: 
    print("tu promedio es de: ", promediob) 
    print("promocionaste biologia")
    cursadabiologia = promediob 

elif promediob <8 and promediob >=6: 
    print("tu promedio es de: ", promediob)
    print("aprobaste biologia pero rendis el final")

else :
    print("tu promedio es de: ", promediob)
    print("desaprobaste biologia")

nota1q = float(input("ingrese la primer nota de quimica: "))
nota2q = float(input("ingrese la segunda nota de quimica : "))
nota3q = float(input("ingrese la tercera nota de quimica : "))
promedioq = (nota1q + nota2q + nota3q)/3

if promedioq >= 8: 
    print("tu promedio es de: ", promedioq) 
    print("promocionaste quimica")
    cursadaquimica = promedioq

elif promedioq <8 and promedioq >=6: 
    print("tu promedio es de: ", promedioq)
    print("aprobaste quimica pero rendis el final")

else :
    print("tu promedio es de: ", promedioq)
    print("desaprobaste quimica")

nota1h = float(input("ingrese la primer nota de historia: "))
nota2h = float(input("ingrese la segunda nota de historia : "))
nota3h = float(input("ingrese la tercera nota de historia : "))
promedioh = (nota1h + nota2h + nota3h)/3

if promedioh >= 8: 
    print("tu promedio es de: ", promedioh) 
    print("promocionaste historia")
    cursadahistoria = promedioh

elif promedioh <8 and promedioh >=6: 
    print("tu promedio es de: ", promedioh)
    print("aprobaste historia pero rendis el final")

else :
    print("tu promedio es de: ", promedioh)
    print("desaprobaste historia")

nota1t = float(input("ingrese la primer nota de tecnologia: "))
nota2t = float(input("ingrese la segunda nota de tecnologia : "))
nota3t = float(input("ingrese la tercera nota de tecnologia : "))
promediot = (nota1t + nota2t + nota3t)/3

if promediot >= 8: 
    print("tu promedio es de: ", promediot) 
    print("promocionaste tecnologia")
    cursadatecnologia = promediot

elif promediot <8 and promediot >=6: 
    print("tu promedio es de: ", promediot)
    print("aprobaste tecnologia pero rendis el final")

else :
    print("tu promedio es de: ", promediot)
    print("desaprobaste tecnologia")

nota1e = float(input("ingrese la primer nota de economia: "))
nota2e = float(input("ingrese la segunda nota de economia : "))
nota3e = float(input("ingrese la tercera nota de economia : "))
promedioe = (nota1e + nota2e + nota3e)/3

if promedioe >= 8: 
    print("tu promedio es de: ", promedioe) 
    print("promocionaste economia")
    cursadaeconomia = promedioe

elif promedioe <8 and promedioe >=6: 
    print("tu promedio es de: ", promedioe)
    print("aprobaste economia pero rendis el final")

else :
    print("tu promedio es de: ", promedioe)
    print("desaprobaste economia")

nota1c = float(input("ingrese la primer nota de construccion de la ciudadania: "))
nota2c = float(input("ingrese la segunda nota de construccion de la ciudadania : "))
nota3c = float(input("ingrese la tercera nota de construccion de la ciudadania : "))
promedioc = (nota1c + nota2c + nota3c)/3

if promedioc >= 8: 
    print("tu promedio es de: ", promedioc) 
    print("promocionaste construccion de la ciudadania")
    cursadaconstrucciondelaciudadania = promedioc

elif promedioc <8 and promedioc >=6: 
    print("tu promedio es de: ", promedioc)
    print("aprobaste construccion de la ciudadania pero rendis el final")

else :
    print("tu promedio es de: ", promedioc)
    print("desaprobaste construccion de la ciudadania")

promediog = (promediom + promediob + promedioq + promedioh + promediot + promedioe + promedioc)/7
if promediog >= 8: 
    print("tu promedio es de: ", promediog) 
    print("aprobaste el año con promocion")
    cursadageneral = promediog

elif promediog <8 and promediog >=6: 
    print("tu promedio es de: ", promediog)
    print("aprobaste el año pero tuviste que rendir finales")

else :
    print("tu promedio es de: ", promediog)
    print("desaprobaste el año")
    print("el proximo va a ser mejor")
print("fin")