# Exercicio_071
print('='*20)
print('Caixa Eletrônico 24H')
print('='*20)

num = int(input('Quanto você deseja sacar? '))
total = num
resto = 0
cinquenta = 0
vinte = 0
dez = 0
um = 0

cinquenta = total // 50
resto = total % 50

total = resto
vinte = total // 20
resto = total % 20

total= resto
dez = total // 10
resto = total % 10

total = resto
um = total
resto = 0

print(f'serão entregue as seguintes notas: {cinquenta} de cinquenta, {vinte} de vinte, {dez} de dez, {um} de um real')

# Solução do professor
print('='*30)
print('{:^30}'.format('Caixa 24h'))
print('='*30)

valor = int(input('Quanto você quer sacar? '))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    
    else:
        if totced > 0:
            print(f'total de {totced} cédulas de R${ced}')
        
        if ced == 50:
            ced = 20
        
        elif ced == 20:
            ced = 10
        
        elif ced == 10:
            ced = 1
        
        totced = 0
        
        if total == 0:
            break
print('fim')
