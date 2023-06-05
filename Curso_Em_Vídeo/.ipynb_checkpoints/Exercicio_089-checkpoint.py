# Exercicio_089
ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? S/N \n ')).strip().upper()[0]
    
    if resposta in 'N':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    opção = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    
    if opção == 999:
        print('fim')
        break
    
    if opção <= len(ficha)-1:
        print(f'Notas de {ficha[opção][0]} são {ficha[opção][1]}')

print('<<< Volte Sempre >>>')
