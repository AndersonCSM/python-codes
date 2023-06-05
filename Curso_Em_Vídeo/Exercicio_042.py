# Exercicio_042
n1 = float(input('informe a primeira medida do lado do triângulo: '))
n2 = float(input('informe a segunda medida do lado do triângulo: '))
n3 = float(input('informe a medida do terceiro lado do triângulo: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print("forma um triângulo")
    if n1 == n2 == n3:
        print('O triângulo é equilátero')
    elif n1 != n2 != n3 != n1:
        print('O triângulo é escaleno')
    else:
        print('O triângulo é isósceles')
else:
    print("não forma um triângulo")
