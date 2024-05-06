# Exercicio_084
# Faltou listar os mais pesados, não apenas um

lista = []
temp = list()

while True:
    temp.append(str(input('Informe seu nome \n')))
    temp.append(float(input('Informe seu peso \n')))
   
    lista.append(temp[:])
    temp.clear()

    controle = ' '
    controle = str(input('quer continuar? [S/N] \n')).strip().upper()[0]
    
    if controle == 'N':
        break

print(lista)
print(f'Foram cadastrados ao todo {len(lista)} pessoas')

maior = menor = c = 0

for p in lista:
    if c == 0:
        maior = p[1]
        nomeMax = p[0]      
        menor = p[1]
        nomeMin = p[0]
        c += 1
    
    elif p[1] > maior:
        maior = p[1]
        nomeMax = p[0]
    
    elif p[1] < menor:
        menor = p[1]
        nomeMin = p[0]   

print(f'O mais pesado foi {nomeMax} com {maior:.2f}Kg')
print(f'O menos pesado foi {nomeMin} com {menor:.2f}Kg')
print('fim')

# Solução do professor
temp = []
prin = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
 
    if len(prin) == 0: #verificar se não foi cadastrado nada ainda e assimilar o maior e menor aos maiores valores
        maior = menor = temp[1]
    
    else:
        if temp[1] > maior: #funciona, pois logo irá da um clear e o índice 1 da lista temp irá ficar vazia
            maior = temp[1]
        
        if temp[1] < menor:
            menor = temp[1]
    
    prin.append(temp[:]) #passa a lista temp para a principal
    temp.clear() #limpa a lista temp para ser usada novamente, com índices resetados
    resp = str(input('Quer continuar? [S/N] \n')).strip().upper()[0]
    
    if resp in 'Nn':
        break

print('=='*30)
print(f'os dados foram {prin}')
print(f'foram cadastrados {len(prin)}')
print(f'O maior peso foi {maior}', end='')

for p in prin:
    if p[1] == maior:
        print(f' [{p[0]}]', end=' ')

print()
print(f'O menor peso foi {menor}', end='')

for p in prin:
    if p[1] == menor:
        print(f' [{p[0]}]', end=' ')
