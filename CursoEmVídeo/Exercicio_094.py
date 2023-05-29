# Exercicio_094
galera = list()
pessoa = dict()
soma = média = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper[0]
        
        if pessoa['sexo'] in 'MF':
            break
        
        print('Erro, por favor, digite apenas M ou F.')
   
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    
    while True:
        resposta = str(input('Quer continuar? [S/N]')).upper[0]
        if resposta in 'SN':
            break
        
        print('Erro, responda apenas S ou N.')
        
    if resposta == 'N':
        break

print('-='*30)
print(f'Foram cadastrado {len(galera)} pessoas.')

média = soma / len(galera)

print(f'A média das idades é de {média:5.2f} anos.')
print(' As mulheres cadastradas foram', end='')

for p in galera:
    if p['sexo'] in 'Ff':
        print(f'p["nome"] ', end='')

print()
print('Lista de pessoas que estão acima da média: ')

for p in galera:
    if p['idade'] >= média:
        print('', end='')
        print(' ')
        
        for k, v in p.itens():
            print(f'{k} = {v};', end='')

print('<< ENCERRADO >>')
