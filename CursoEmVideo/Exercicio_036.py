# Exercicio_036

# entradas
casa = float(input("Qual o valor da casa que você irá comprar? \n"))
salario = float(input("Qual o valor do salário? \n"))
tempo = int(input("em quantos anos você irá pagar o empréstimo? \n"))

#processamento
meses = tempo * 12 #anos em dias
parcela = salario * 0.3 #calcula o valor da parcela que pode pagar
empréstimo = casa / meses #calcula quanta será o valor do empréstimo por mês

#decisão
if empréstimo <= parcela:
    print("seu empréstimo foi aprovado com parcelas de R${:.2f} em {} meses".format(empréstimo, meses))
else:
    print("O empréstimo foi rejeitado.")
