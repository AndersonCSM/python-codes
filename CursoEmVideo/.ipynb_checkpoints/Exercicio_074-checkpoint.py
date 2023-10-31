# Exercicio_074
from random import randint

n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)
tupla = (n1, n2, n3, n4, n5)

menor = maior = 0

for c in range(0,len(tupla)):
    if c == 0:
        maior = tupla[c]
        menor = tupla[c]
    
    else:  
        if tupla[c] > maior:
            maior = tupla[c]
        
        if tupla[c] < menor:
            menor = tupla[c]

print(tupla)   
print(f'O menor é {menor}')
print(f'O maior é {maior}')

# Solução do Professor
from random import randint

n = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(f'Os valores sorteadors foram {n}')
print(f'O maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')