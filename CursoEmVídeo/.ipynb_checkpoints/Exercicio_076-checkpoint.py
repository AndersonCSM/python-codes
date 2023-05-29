# Exercicio_076
lista = ('lápis', 1.75,
'caderno', 15.00,
'borracha', 2,
'Estojo', 20,
'Transferidor', 4.20,
'mochila', 124.20)

print('-'*40)
print('Listagem de Preços')
print('-'*40)

for p in range(0,len(lista)):
    if p % 2 == 0:
        print(f'{lista[p]:.<30}', end = ' ')
    else:
        print(f'R$ {lista[p]:>7.2f}')

print('-'*40)
