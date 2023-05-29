# Exercicio_081
lista = []
c = 0

while True:
    lista.append(float(input(f'Informe o {c}º número \n')))
    c +=1

    controle = ' '
    
    while controle not in 'SN':
        controle = str(input('Quer continuar? [S/N] \n')).strip().upper()[0]
       
        if controle == 'N':
            break

print('='*40)
print(f'Foram digitados {len(lista)} números')
print(f'a lista é: {sorted(lista, reverse=True)}')

if 5 in lista:
    print(f'O cinco está presente e na posição {lista.index(5)}')

else:
    print('O cinco não está presente')

print('='*40)
print('fim')
