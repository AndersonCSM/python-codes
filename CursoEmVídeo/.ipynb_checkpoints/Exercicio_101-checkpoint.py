# Exercicio_101
def voto(idade=0):
    if idade < 16:
        return print('NEGADO')
    
    elif (idade >= 16 and idade <= 18) or idade >= 80:
        return print('OPCIONAL')
    
    elif idade > 18 and idade <80:
        return print('OBRIGATÓRIO')

voto()

# Solução do professor
def voto(ano):
    from datetime import date
    
    atual = date.today().year
    idade = atual - ano
    
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# Programa principal
nasc = int(input('Em que ano você nasceu?'))

print(voto(nasc))
