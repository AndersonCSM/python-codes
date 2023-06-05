# Exercicio_088
from random import randint
from time import sleep

matriz = []
tabela = list()
palpites = int(input('Quantos palpites você quer? \n'))
total = 1

while total <= palpites:
    cont = 0
    
    while True:
        num = randint(0,60)
        
        if num not in tabela:
            tabela.append(num)
            cont += 1
        
        if cont >= 6:
            break
    
    tabela.sort()
    matriz.append(tabela[:])
    tabela.clear()
    total += 1

for i, l in enumerate(matriz):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('fim')
