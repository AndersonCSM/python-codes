# Exercicio_032
import datetime
ano = int(input('Insira um ano: '))

if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
    print("o ano é bissexto")
else:
    print("O ano não é bissexto")

# Resolução do professor
from datetime import date

ano = int(input('Insira um ano: '))

if ano == 0:
    ano = date.today().year
if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
    print("o ano é bissexto")
else:
    print("O ano não é bissexto")
