# Exercicio_063
numero = 0
anterior = 1
anterior2 = 0
contador = 1 #tem que começar de um número a menos porque o 1 sempre irá aparecer
sequência = int(input('Quantos números você quer vê da sequência de Fibonacci: '))

while contador < sequência:
    numero = anterior + anterior2
    
    if contador == 1: #condição para imprimir o 1 pela primeira vez, poderia ser colocado fora do while
        print(numero, end=' ')
    print(numero, end=' ')   
    
    anterior2 = anterior
    anterior = numero
    
    contador += 1

# Resolução do Professor
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

n = int(input('Quantos termos você quer vê? '))
t1 = 0
t2 = 1

print('~~'*15)
print('{} > {}'.format(t1, t2), end= ' ')
cont = 3

while cont <= n:
    t3 = t2 + t1
    print(' > {}'.format(t3), end=" ")
    t1 = t2
    t2 = t3
    cont += 1

print(' fim')
