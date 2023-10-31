# Exercicio_078
lista = []

for c in range(0,5):
    lista.append(float(input(f'informe o valor {c+1}: ')))

print(f'O maior foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor foi {min(lista)} na posição {lista.index(min(lista))}')

# Solução do Professor
for i, v in enumerate(lista): #O i representa o índice e o v o valor do item na lista
   
    if v == maior:
        print(f'{i}...', end= ' ')
