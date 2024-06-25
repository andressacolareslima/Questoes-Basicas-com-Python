import math
a = int (input("Digite o A:"))
b = int (input("Digite o B:"))
c = int (input("Digite o C:"))

delta = b*b - 4*a*c
if delta < 0 :
    print ("Não possuí solução real. ")
else : 
    calculo_raiz1 = ((-b + math.sqrt(delta))/ 2*a)
    calculo_raiz2 = ((-b - math.sqrt(delta))/ 2*a)
    print (f"Resultado X1: {calculo_raiz1:.2f}")
    print (f"Resultado X2: {calculo_raiz2:.2f}")


