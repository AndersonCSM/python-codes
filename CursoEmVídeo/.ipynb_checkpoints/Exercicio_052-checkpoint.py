# Exercicio_052
div = 0
num = int(input('informe um número para saber se ele é primo  \n'))
for c in range(1,num+1):
    if (c != 1) and (num % c == 0):
        div += 1

if div == 1:
    print('É primo')
else:
    print('não é primo')

# Resolução do professor
cont = 0
num = int(input('digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')

    print('{}'.format(c), end = ' ')

print('\n \033[m o número {} foi divisível {} vezes'.format(num, cont))

if cont == 2:
    print("O número é primo")
else:
    print('o número não é primo')
