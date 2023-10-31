# Exercicio_041
from datetime import date

atual = date.today().year
anoN = int(input('informe o ano de nascimento para saber a categoria do nadador: '))
idade = atual - anoN

if idade <= 9:
    print('mirim')
elif 9 < idade <= 14:
    print('infantil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <= 25:
    print('Sênior')
else:
    print('master')
