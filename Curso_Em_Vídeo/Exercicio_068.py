# Exercicio_068
from random import randint

print('=-='*20)
print('Jogando ímpar ou par')
print('=-='*20)

sequência = 0

while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    
    jogada = (jogador + computador) % 2 == 0 # se for par retornar True, se for ímpar retorna False

    if jogada and escolha =='P': # True and True = True
        print('=-='*20)
        print(f'você jogou {jogador} e o computador {computador}. A soma é de {jogador+computador}, sendo Par')
        print('Você acertou!!! Tente novamente')
        print('=-='*20)
        
        sequência += 1
   
    elif not jogada and escolha == 'I': # not False and True = True and True = True
        print('=-='*20)
        print(f'Você jogou {jogador} e o o computador {computador}. A soma é de {jogador+computador}, sendo Ímpar')
        print('Você acertou!!! Tente novamente')
        print('=-='*20)
        
        sequência += 1
   
    else:
        print('=-='*20)
        print('Você perdeu!')
        print(f'Você jogou {jogador} e o computador jogou {computador}. A soma é de {jogador+computador}')
        print('=-='*20)
        
        break 

print(f'A sequência de vitória foi de {sequência}')
