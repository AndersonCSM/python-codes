# Exercicio_098
from time import sleep

def contador(inicio, fim, passo):
    if inicio == fim == passo == 0:   
        print('Contagem de 1 até 10 em 1 em 1: ')
        
        for c in range(0, 10):
            print(c+1, end=' ')
            sleep(0.5)         
        print ( )
      
        print('Contagem de 10 até 0 de 2 em 2: ')
        
        for c in range(10, -1, -2):
            print (c, end=' ' )
            sleep(0.5) 
        print()
    
    else:
        print('Sua contagem personalizada é:')
        print(f'De {inicio} até {fim} com passo de {passo} em {passo}')
        if passo <= 0:
            for i in range(inicio, fim-1, passo):
                print(i, end= ' ')
                sleep(0.5) 
        
        else:
            for i in range(inicio, fim+1, passo):
                print(i, end= ' ') 
                sleep(0.5)           

                
contador(0, 0, 0)

print('Agora é sua vez, faça um contador!')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

if passo == 0:
    passo = 1

contador(inicio,fim,passo)

# Solução do professor
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    
    if p == 0:
        p= 1  

    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = 1
        
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('Fim')
    
    else:
        cont = 1
        
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5) 
            cont -= p
        
        print('Fim') 
    
    print('-=-'*20)


# Programa principal
contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez de personalizar a contagem!')

ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('passo: '))

contador(ini,fim,pas)
