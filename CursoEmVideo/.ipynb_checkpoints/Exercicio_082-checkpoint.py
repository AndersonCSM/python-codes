# Exercicio_082
lista = []
impar = []
par = []
c = 0

while True:
    lista.append(float(input(f'Digite um valor na posição {c} \n')))

    if lista[c] % 2 == 0:
        par.append(lista[c])
    
    else:
        impar.append(lista[c])
    
    c += 1 
    controle = ' '
    
    while controle not in 'sn':
        controle = str(input('Quer continuar? [S/N]\n')).strip().lower()[0]
    
    if controle == 'n':
        break

print('As listas são:')
print(f'A lista um: {sorted(lista)}')
print(f'A lista dos pares: {sorted(par)}')
print(f'A lista dos impares: {sorted(impar)}')
print('Fim')

# Solução do professor
numero = [] 
while True:
    numero.append(float(input('Informe um valor a ser armazenado\n')))
    controle = ' '
    
    while controle not in 'SN':
        controle = str(input('Quer continuar? [S/N] \n')).strip().upper()[0]
    if controle == 'N':
        break
par = []
impar = []

for c, valor in enumerate(numero):
    if valor % 2 ==0:
        par.append(valor)
    else:
        impar.append(valor)

print('=-='*20)
print(numero)
print(par)
print(impar)
print('=-='*20)
