def soma (x,y):
    return x + y
def subtracao (x,y):
    return x - y
def multiplicacao (x,y):
    return x * y
def divisao (x,y):
    if y!=0:
        return x / y
    else:
        return ("Operação inválida, o dividendo não pode ser 0")
def quatro_operacoes ():
    print ("Operações disponíveis: ")
    print ("Digite 1 para somar")
    print ("Digite 2 para subtração")
    print ("Digite 3 para multiplicação")
    print ("Digite 4 para divisão")

    while True:
        selecao = input("Qual a operação que deseja realizar?")
        if selecao in  ['1', '2', '3', '4'] :
            num1 = float (input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            if selecao == '1':
                print (f'{soma(num1,num2)}')
            elif selecao =='2':
                print (f'{subtracao(num1,num2)}')
            elif selecao == '3':
                print (f'{multiplicacao(num1,num2)}')
            elif selecao == '4':
                erro = divisao(num1,num2)
                if erro == "Operação inválida, o dividendo não pode ser 0":
                    print (erro)
                else :
                    print (f'{erro:.2f}')
        break
quatro_operacoes()
