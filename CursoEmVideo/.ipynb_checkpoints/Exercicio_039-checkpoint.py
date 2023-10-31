# Exercicio_039
import datetime

anoatual = datetime.date.today().year
sexo = str(input('qual o seu sexo? F- femino, M - masculino \n')).upper().strip()
if sexo == 'M':
    ano = int(input("Informe o ano de nascimento: "))
    if anoatual - ano < 18:
        tempo = int(18 - (anoatual - ano))
        print("Você ainda irá se alistar, faltam {} anos".format(tempo))
        print(f'O seu alistamento irá ocorre em {anoatual + (18-(anoatual-ano))}')
    elif anoatual - ano == 18:
        print("Esta na hora de se alistar")
    else:
        tempo = int((anoatual - ano)- 18)
        print("o prazo de alistamento já passou em {} anos".format(tempo))
        print(f'Ele ocorreu em {anoatual-((anoatual - ano)-18)}')    
else:
    print("Você é do sexo feminino e não precisa se alistar")
