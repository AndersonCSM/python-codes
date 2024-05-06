# Exercicio_060
num = int(input('informe um número para o cálculo do seu fatorial: '))
c = num
fat = 1
while c != 0:
    print('{}'.format(c), end=' ')
    print(' X ' if c>1 else ' = ', end='')
    fat = fat * c
    c -= 1

print('{}! é {}'.format(num, fat))
