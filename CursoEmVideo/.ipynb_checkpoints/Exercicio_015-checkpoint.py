# Exercicio_015
km = float(input("informe a quantidade de Km rolados \n"))
dias = int(input("informe a quantidade de dias usados \n"))
preco = ((0.15*km)+(60*dias))
print("O preço total a se pagar é de R${:.2f}".format(preco))
