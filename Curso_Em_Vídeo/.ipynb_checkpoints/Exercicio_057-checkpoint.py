# Exercicio_057
sexo = str(input('Informe seu sexo: ')).upper().strip()
while sexo != ('M' or 'F'):
    sexo = (input('Informe seu sexo, novamente \n')).upper().strip()

print('O sexo informador foi Masculino'if sexo == 'M'else 'O sexo informado foi feminino')

# Solução do professor
sexo = str(input('informe seu sexo: M/F: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informação inválida, insira novamente o sexo: ')).strip().upper()[0]

print('O sexo {} foi registrado com sucesso'.format(sexo))
