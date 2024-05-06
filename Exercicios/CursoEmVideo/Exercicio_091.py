# Exercicio_091
from random import randint
from time import sleep
from operator import itemgetter

jogo = { 
'jogador1': randint(1,5),
'jogador2': randint(1,5),
'jogador3': randint(1,5),
'jogador4': randint(1,5),
'jogador5': randint(1,5)
}

print('valores sorteados')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado ')
    sleep(1)

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
