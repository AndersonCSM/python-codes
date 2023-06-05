# Exercicio_033
a = int(input("Informe o primeiro número: "))
b = int(input("Infome o segundo número: "))
c= int(input("informe o terceiro número: "))

menor = a
# menor
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c

# maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'o menor valor é {menor}')
print(f'o maior valor é {maior}')        
