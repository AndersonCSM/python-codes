# Exercicio_053
frase = str(input('digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = junto[::-1] irá ler o string de trás pra frente usando fatiamento
if inverso == junto:
    print('temos um palindromo')
else:
    print('não é um palindromo')

print(junto, inverso)
