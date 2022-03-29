#ejercicio_9 Lucia Lopez

print("------CALCULADORA------")
print("       menu\n")

entrada = 0
while entrada !=5: 
    print("1---> SUMA  2--->RESTA  3--->MULTIPLICACION  4--->DIVISION  5--->SALIR")
    entrada = int(input("ingrese una opcion: "))
    if entrada==1:
        print("SUMA")
        num1=float(input("ingrese valor: "))
        num2=float(input("ingrese valor: "))
        suma=num1+num2
        print("su resultado es: ", suma)
    elif entrada==2:
        print("RESTA")
        num1=float(input("ingrese valor: "))
        num2=float(input("ingrese valor: "))
        resta=num1-num2
        print("su resultado es: ", resta)
    elif entrada==3:
        print("MULTIPLICACION")
        num1=float(input("ingrese valor: "))
        num2=float(input("ingrese valor: "))
        multiplicacion=num1*num2
        print("su resultado es: ", multiplicacion)
    elif entrada==4: 
        print("DIVISION")
        num1=float(input("ingrese valor: "))
        num2=float(input("ingrese valor: "))
        division=num1/num2
        print("su resultado es: ",division )
    elif entrada==5:
        print("salir")
        break

