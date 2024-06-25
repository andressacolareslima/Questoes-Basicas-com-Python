lista = input("Digite três valores númericos: ")

valores = [int (i) for i in lista.split()]
ordenado = sorted(valores)

print (ordenado)