# Exercicio_087
Lmatriz = []
Cmatriz = list()
soma = terceira = 0

for i in range(0,3):
    for j in range(0,3):
        num = int(input(f'Insira o valor para a posição [{i}, {j}] \n'))
   
        if num % 2 == 0:
            soma += num
        
        if i == 2:
            terceira += num
        
        Cmatriz.append(num)
    Lmatriz.append(Cmatriz[:])
    Cmatriz.clear()

for i in range(0,3):
    for j in range(0,3):
        print(f'[{Lmatriz[i][j]:^5}]', end='')
    print()

print(f'A soma dos números pares da matriz são: {soma}')
print(f'A soma da terceira linha da matriz é {terceira}')
print(f'O valor máximo da terceira linha é {max(Lmatriz[2])}')

# Solução do professor
matriz = [[0,0,0,], [0,0,0,], [0,0,0,]]
soma = maior = terceira = 0

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digiten o valor da posição [{i}, {j}] \n'))

print('='*15)

for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
        
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
    print()

print('-=-'*30)
print(f'A soma dos números pares é {soma}')

for i in range(0,3):
    terceira += matriz[i][2]

print(f'A soma da terceira linha é {terceira}}')

for c in range(0, 3):
    if c == 0:
        maior == matriz[1][c]
    
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'O maior valor da linha dois é {maior}')
