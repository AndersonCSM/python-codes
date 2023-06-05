# Exercicio_056
idadeTotal= 0
maisVelho = 0
nomeVelho = str
jovens = 0

for c in range(0,4):
    print('-------{} Pessoa ------'.format(c+1))
    nome = str(input('informe o nome da pessoa {} \n'.format(c+1)))
    idade = int(input('Infome a idade da pessoa \n'))
    sexo = str(input('''informe o sexo: 
   [M] - MASCULINO
   [F] - FEMININO \n''')).strip().upper()
   
    idadeTotal += idade
    # Uma idéia seria colocar um if c == 0 para anotar o primeiro valor do mais velho
    if idade >= maisVelho and sexo == 'M':
        maisVelho= idade 
        nomeVelho = nome
   
if sexo == 'F' and idade < 20:
    jovens += 1

print('A média da idade do grupo é {}'.format(idadeTotal/4))
print('O homem mais velho se chama {}'.format(nomeVelho))
print('A quantidade de mulheres que tem menos de 20 anos é de {}'.format(jovens))
