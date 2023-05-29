# Exercicio_099
def maior():
    lista = list()
    
    while True:
        lista.append(int(input('Informe um número: '))) 
        
        while True:
            resposta = str(input('Quer continuar? [S/N]')).upper()[0]
            
            if resposta in 'SsNn':
                break
            
            print('Apenas respostas com S ou N.')
        
        if resposta == 'N':
            break
    
    print(f'O maior valor da lista: {lista} é {max(lista)}')

maior()

# Solução do professor
from time import sleep

def maior(*num):
    cont = maior = 0
    print('\n Analisando os valores passados...')
    
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        
        if cont == 0:
            maior = valor
        
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 9, 1, 9 , 20, 0, 23)
