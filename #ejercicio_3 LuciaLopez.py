#ejercicio_3 LuciaLopez


def multiple(valor, multiple):
    """
    Funcion para calcular si el numero es multiplo
    utilizando el modulo de la division
    """
    return True if valor % multiple == 0 else False
 
# lista que contendra los valores multiples
multiples_3=[]

 
# bucle del 1 al 100
for i in range(1, 101):
 
    if multiple(i, 3):
        multiples_3.append(i)
 

print ("Los multiples de 3 son:", multiples_3)
