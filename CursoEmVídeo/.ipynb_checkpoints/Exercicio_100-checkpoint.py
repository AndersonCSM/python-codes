# Exercicio_100
numeros = list()


def sorteia(lista):
    from random import randint
    
    for c in range(0,5):
        lista.append(randint(1,10))
    
    print(lista)


def somaPar(lista):   
    soma = 0
    for c in range(0, len(numeros)):
        if lista[c] % 2 == 0:
            soma += lista[c]
    
    print(f'A soma dos valores pares da lista é {soma}')


sorteia(numeros)
somaPar(numeros)
