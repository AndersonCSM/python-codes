# Exercicio_069
print('-=-'*20)
print('Cadastro de pessoas')
print('-=-'*20)

maiores = homens = mulheres = 0

while True:
    idade = int(input('Informe a idade: '))

    sexo = ' '
    while sexo not in 'FnMn':
        sexo = str(input('informe o sexo: [F/M] ')).strip().upper()[0]

    if idade >= 18:
        maiores += 1
    
    if sexo == 'M':
        homens += 1
    
    if sexo == 'F' and idade < 20:
        mulheres += 1

    escolha = ' '
    
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    
    if escolha == 'N':
        break

print (f'A quantidade de pessoas de maior é de {maiores} pessoas')
print(f'Foram cadastrados {homens} homens')
print(f'Foram cadastradas {mulheres} mulheres com menos de 20 anos')
