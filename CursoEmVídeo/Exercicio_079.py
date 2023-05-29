# Exercicio_079
lista = []
p = 0

while True:
    c = float(input(f'Insira o valor da posição {p} \n'))
    
    if c not in lista:
        lista.append(c)

    p += 1
    controle = ' '
    
    while controle not in 'SsNn':
        controle = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if controle == 'N':
        break

print('='*30)
print(f'Os valores ÚNICOs em ordem crescente são {sorted(lista)}')
print('fim')

# Solução do Professor
numb = list()

while True:
    n = int(input('Digite um número: '))

    if n not in numb:
        numb.append(n)
        print('número adicionado')
    
    else:
        print('Valor duplicado, não pode ser adicionado a lista')   
   
    r = str(input('quer continuar? [S/N]')).strip().lower()[0]
    
    if r in 'Nn':
        break

print('-'*30)
print(f'Os número digitados fora: {sorted(numb)}')
