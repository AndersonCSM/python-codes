# Exercicio_086
Lmatriz = []
Cmatriz = list()

for i in range(0,3):
    for j in range(0,3):
        num = int(input(f'Insira o valor para a posição [{i}, {j}] \n'))
        Cmatriz.append(num)
    
    Lmatriz.append(Cmatriz[:])
    Cmatriz.clear()

for i in range(0,3):
    for j in range(0,3):
        print(f'[ {Lmatriz[i][j]} ]', end='')
    print('')

print('{:-^30}'.format('Fim'))

# Solução do professor
matriz = [[0,0,0,], [0,0,0,], [0,0,0,]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digiten o valor da posição [{i}, {j}] \n'))

print('='*15)
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
    
    print()
