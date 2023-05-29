# Exercicio_107
from utilidades import moeda

valor = float(input('Digite um valor em R$. \n'))

print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentando 10% de {valor} temos {moeda.aumentar(valor,10)}')
print(f'Diminuindo 13% de {valor} temos {moeda.diminuir(valor,13)}')
