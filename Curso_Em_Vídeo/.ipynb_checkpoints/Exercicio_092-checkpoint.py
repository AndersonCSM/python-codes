# Exercicio_092
import datetime
dados = dict()
anoAtual = datetime.date.today().year

dados['nome'] = str(input('Informe o nome \n'))
ano = int(input('informe o ano de nascimento \n'))

dados['idade'] = anoAtual - ano

ctps = int(input('Carteira de trabalho (0 caso não tenha) \n'))

if ctps != 0:
    dados['contrato'] = int(input('ano de contratação \n'))
    dados['salário'] = float(input('Salário R$ \n'))
    aposentadoria = dados['contrato']+35

print(dados)

for k, v in dados.items():
    print(f'{k} é {v}')

if ctps != 0:
    print(f'Aposentadoria em {aposentadoria}')

# Solução do professor
from datetime import datetime

dados = dict()

dados['nome']= str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('=-'*30)

for k,v in dados.items():
    print(f' {k} tem o valor {v}')
