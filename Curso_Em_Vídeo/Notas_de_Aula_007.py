# Aula_21
def contador(i, f, p):
    """
    => Faz uma contagem demonstrando na tela
    i para inicio da contagem
    f para fim da contagem
    p para passo da contagem
    retunr: null
    function criada por Anderson Carlos
    """

    c = i
    while c <= i:
        print(f'{c}', end=' ')
        c += p
    
    print('Fim')


help(contador)


def somar(a=0,b=0,c=0):
    """
    Função somar, soma os parâmetros a, b e c, respectivamente.
    caso um parâmetros não seja informado, assumirá o valor de 0
    """
    s = a+b+c
    print(f'A soma vale {s}')


somar(3,2,5)
somar(8,4)
somar()


def test(b):
    # b e c é uma variável local
    # chamando o a global.
    
    global a
    b += 4
    c = 2
    
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# a sendo variável global
a = 5
test(a)
print(f'A fora vale {a}')


def somar(a=0,b=0,c=0):
    """
    Função somar, soma os parâmetros a, b e c, respectivamente.
    caso um parâmetros não seja informado, assumirá o valor de 0
    """
    s = a+b+c
    return s


r1 = somar(3,2,5)
r2= somar(8,4)
r3= somar()
print(f'os resultados foram {r1}, {r2} e {r3}')


def fatorial(num1):
    f= 1
    for c in range(num1, 0, -1):
        f *= c
    
    return f

f1 = fatorial(3)
f2 = fatorial(4)
f3 = fatorial(5)

print(f'Os resultados são {f1},{f2} e {f3}')


def par(num):
    if num % 2 ==0:
        return True
    else:
        return False


num = int(input('Digite um número: '))

if par(num):
    print('É par')
else:
    print('Não é par')
