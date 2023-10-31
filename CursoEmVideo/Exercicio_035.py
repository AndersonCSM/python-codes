# Exercicio_035
r1 = float(input('informe o tamanho da primeira reta: '))
r2 = float(input('informe o tamanho da segunda reta: '))
r3 = float(input("informe o tamanho da terceira reta: "))

if r1+r2 >r3 and r1+r3 > r2 and r2+r3> r1:
    print("os valores das retas formam um triângulo")
else:
    print("Os valores das retas não formam um triângulo")
