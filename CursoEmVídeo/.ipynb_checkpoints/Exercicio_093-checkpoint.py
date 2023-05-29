# Exercicio_093
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input (f'Quantas partidas o {jogador["nome"]} jogou? '))

for c in range(0, total):
    partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('=-'*30)
print(jogador)
print('=-'*30)

for k, v in jogador.items():
    print(f'{k} tem o vlaor {v}')

print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i+1}, fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols.')
