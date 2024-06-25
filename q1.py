idade = int (input("Digite a idade desejada: "))

if idade <= -1 :
    print("Idade inválida, tente novamente. ")
elif idade == 1:
        print (f"Sua idade é {idade} ano. Portanto, é menor de idade. ")
elif idade < 18 :
        print (f"Sua idade é {idade} anos. Portanto, é menor de idade. ")
else:
        print (f"Sua idade é {idade} anos. Portanto, é maior de idade. ")