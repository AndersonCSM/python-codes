# Exercicio_058
import random

tentativas = 1
numpc = random.randint(0,10)

print(numpc)
num = int(input('Tente adivinhar o número que o computador está pensando \n'))
while num != numpc :
    num = int(input('Errou, tente novamente \n'))
    tentativas += 1

print('você acertou o número com {} tentativas'.format(tentativas)) 
