nota= int (input("Digite a primeira nota:"))
notas= int (input("Digite a segunda nota: "))

media =(nota + notas)/2
    
if media>=6.0:
        print (f"Sua média é {media:.2f}, você está aprovado.")
else:
        print (f"Sua média é {media:.2f}, você está reprovado.")