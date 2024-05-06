# Exercicio_090
aluno = dict()
aluno['nome'] = str(input('Nome do aluno \n'))
aluno['média'] = float(input(f'A média de {aluno["nome"]} \n'))

if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'

elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'recuperação'

elif aluno['média'] < 3:
    aluno['situação'] = 'reprovado'

for k, v in aluno.items():
    print(f'O campo {k} é {v}')
