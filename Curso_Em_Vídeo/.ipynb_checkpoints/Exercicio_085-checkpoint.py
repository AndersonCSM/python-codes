# Exercicio_085
lista = []
impar = list()
par = list()

for c in range(0,7):
    num = int(input(f'digite o {c+1}º valor \n'))
  
    if num % 2 == 0:
        par.append(num)
    
    else:
        impar.append(num)

lista.append(par[:]) 
lista.append(impar[:])

print(f'Os valores pares são: {sorted(lista[0])}')
print(f'Os valores ímpares são: {sorted(lista[1])}')
print('fim')

# Solução do professor
num = [[], []]
valor = 0

for c in range(0,7):
    valor = int(input('Digite um valor: '))
  
    if valor % 2 == 0:
        num[0].append(valor)
    
    else:
        num[1].append(valor)

        print('='*30)
print(f'Todos os valores: {num}')
print(f'Os valores pares: {sorted(num[0])}')
print(f'Os valores impares{sorted(num[1])}')
