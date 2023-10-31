# Exercicio_066
soma = cont = 0

while True:
    num = int(input('Digite um número(Digite 999 para parar): '))
    
    if num == 999:
        break
    
    soma += num
    cont += 1

print(f'A soma dos números é {soma} e foram digitados {cont} números')
