# Exercicio_072
numero = ('zero','dois','três','quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete ', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20 \n'))

while (num < 0) or (num > 20):
    num = int(input('Número inválido, digite novamente \n'))

print(f' você digitou {numero[num]}')
print('fim')

# Solução do Professor
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    
    if 0 <= num <= 20:
        break
    
    print('tente novamente. ', end='')
