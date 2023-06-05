# Exercicio_044
preço = float(input('qual o valor normal do produto? '))
print('=-='*20)

print('1- à vista {}{}{}: {}{}{} de desconto'.format('\033[0;34m', 'dinheiro ou cheque' ,'\033[m', '\033[0;33m', '10%','\033[m'))
print('2- à vista no {}{}{}: {}{}{} de desconto'.format('\033[0;34m', 'cartão' ,'\033[m', '\033[0;33m', '5%','\033[m'))
print('3- Em até {}{}{} preço normal'.format('\033[0;34m', '2x no cartão' ,'\033[m'))
print('4- {}{}{} no cartão: {}20{} de juros{} de juros'.format('\033[0;34m', '3x ou mais' ,'\033[m', '\033[0;33m', '%' ,'\033[m'))
print('=-='*20)

count=int(input('forma de pagamento? '))
if count == 1:
    print('O preço a se pagar é de R${:.2f}'.format(preço*0.9 ))
elif count == 2:
    print('O preço a se pagar é de R${:.2f}'.format(preço * 0.95))
elif count == 3:
    print('O preço a se pagar é de R${:.2f}'.format(preço))
elif count == 4:
    print('O preço a se pagar é de R${:.2f}'.format(preço*1.2))
else:
    print('A opção informada não está listada nas formas de pagamento')
