# Exercicio_059
n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))
n3 = 0

while n3 != 5:
    n3= int(input('''
       #[1] Somar
       #[2] Multiplicar
       #[3] Maior
       #[4] Novos números
       #[5] Sair   '''))
    
    if n3 == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))

    elif n3 == 2:
        print('{} * {} = {}'.format(n1, n2, n1*n2))
    
    elif n3 == 3:
        if n1 > n2:
             print(f'O maior é {n1}')
        
        elif n2 > n1:
            print(f'O maior é {n2}')
        
        else:
            print('os números são iguais')
    
    elif n3 == 4:
        n1 = float(input('Insira novamento o primeiro valor: '))
        n2 = float(input('Insira novamente o segundo valor: '))
    
    elif n3 != 5:
        print('opção não é valida')

print('fim')  
