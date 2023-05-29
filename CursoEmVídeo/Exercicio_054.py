# Exercicio_054
import datetime
maiores = 0
menores = 0
atual = datetime.date.today().year

for c in range(0, 7):
    nasc = int(input('informe a data de nascimento \n'))
    if atual - nasc >= 21:
        maiores += 1
    else:
        menor += 1

        print('no total existem {} pessoas de maior e {} pessoas de menor'.format(maiores, menores))
print('fim')
