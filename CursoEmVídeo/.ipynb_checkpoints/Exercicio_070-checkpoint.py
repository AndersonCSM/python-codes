# Exercicio_070
print('='*20)
print('Supermercado bigbom')
print('='*20)

total = custoMil = 0
barato = str
contador = 1

while True:
    nome = str(input('Qual o nome do produto? '))
    custo = float(input('Quanto custo o produto em R$? '))

    total += custo
   
    if custo > 1000:
        custoMil += 1

    if contador == 1:
        menor = custo
        barato = nome
        
        contador +=1

    if custo < menor: # Pode juntar com um OU junto com o if acima
        menor = custo
        barato = nome

    controle = ' '
    
    while controle not in 'SN':
        controle = str(input('quer continuar? [S/N]')).strip().upper()[0]
   
    if controle == 'N':
        break

print('='*20)
print(f'O total gasto foi de R${total:.2f}')
print(f'O total de produtos acima de mil reais foi de {custoMil} itens')
print(f'Ó nome do produto mais barato é: {barato}')
print('='*20)
