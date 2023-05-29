# Exercicio_055
maior = float
menor = float

for c in range(0,5):
    peso = float(input(f'informe o peso da pessoa {c+1} \n'))
    
    if c == 0:
        menor = peso
        maior = peso
    
    else:
        if peso > maior:
            maior = peso
        
        elif peso < menor:
            menor = peso

print('O maior peso foi de {}kg e o menor foi de {}kg'.format(maior, menor))
