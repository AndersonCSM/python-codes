# Exercicio_104
def leiaint(num):
    if type(num) == int:
        return print(f'O valor [{num}] foi aceito por ser um número')
    
    else:
        return print(f'O valor [{num}] não é um número e por isso foi rejeitado')


num = str(input('informe um valor '))

if num.isnumeric():
    num = int(num)

leiaint(num)

# Solução do professor
def leiaInt(msg):
    ok = False
    valor = 0
    
    while True:
        n = str(input(msg))
        
        if n.isnumeric():
            valor = int(n)
            ok = True
        
        else: 
            print('\033[0;31m ERRO! Digite um número inteiro válido.\033[m')
        
        if ok:
            break
    
    return valor


n = leiaInt('Digite um número: ')

print(f'Você acabou de digitar o número {n}')
