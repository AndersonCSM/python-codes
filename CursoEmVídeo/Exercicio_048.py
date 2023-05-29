# Exercicio_048
soma = 0

for c in range(1,501):
    if (c % 2 != 0) and c % 3 == 0:
        soma += c

print(soma)
print('fim')

# Solução do professor
soma = 0 # acumulador
cont = 0 # contador
for c in range(1, 501, 2): #já pega os números ímpares
    if  c % 3 ==0: # divisíveis por três
        soma += c
        cont += 1

print(soma)
print(cont)
