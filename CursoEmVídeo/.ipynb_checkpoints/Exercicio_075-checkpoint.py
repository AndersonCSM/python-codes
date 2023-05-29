# Exercicio_075
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('digite o quarto valor: '))

tupla = (n1,n2,n3,n4)
contP = 0
cont9 = 0

for c in tupla:
    if c == 9:
        cont9 += 1
    
    if c % 2 == 0:
        contP += 1

if cont9 > 0:
    print(f'O valor 9 apareceu {cont9} vezes')

else:
    print('Não foram digitados valores 9')

if 3 in tupla:
    print(f' O valor 3 está na posição: {tupla.index(3)+1}')

else:
    print('Não foram informados valores de número 3')

if contP > 0:
    print(f'A quantidade de números pares é de {contP}')

else:
    print('Não foram digitados valores pares')
    
# Solução do professor
num = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), 

int(input('Digite um valor: ')), int(input('Digite um valor: ')), 
int(input('Digite um valor: ')))

print(f'Os valores digitados foram {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')

else:
    print('O valor três não foi digitado')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')
