# Exercicio_073
times = ('Bragantino', 'Atlético-PR', 'Palmeiras', 'Fortaleza', 'Bahia', 'Santos', 'Atlético-GO', 'Atlético-MG', 'Fluminense', 'Flamengo', 'Corinthians', 'Ceará', 'Internacional', 'Juventude', 'Sport', 'Cuiabá', 'São Paulo', 'Chapecoense', 'América-MG', 'Grêmio')

print('=='*20)
print(f'Os 5 primeiors colocados são {times[:5]}')
print('=='*20)
print (f' os últimos 4 colocados são {times[-4:]}')
print('=='*20)
print(f' Os times em ordem alfábetica: {sorted(times)}')
print('=='*20)

chapeco = (times.index('Chapecoense')+1)
print(f'Chapecoense está na posicão {chapeco}')
print('=='*20)
