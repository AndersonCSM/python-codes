# Exercicio_077
palavras = ('aprender','gratis','programar','futuro','Python','curso','free','programador')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
