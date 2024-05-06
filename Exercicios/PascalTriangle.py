def printer(lista=[]):
    size = len(lista)
    for i in range(size):
        print(lista[i])
    print(" ")


def triangulo_1(size=1):
    lista = []
    aux = []
    for i in range(0, size):
        for j in range(0, size):
            aux.append(0)
        lista.append(aux[::])
        aux.clear()

    for i in range(0, size):
        lista[i][0] = 1
        for j in range(0, size):
            if i == j:
                lista[i][j] = 1
            elif j < i and j != 0:
                lista[i][j] = (
                    lista[i - 1][j - 1] + lista[i - 1][j] + lista[i - 2][i - (j + 1)]
                )
    return printer(lista)


def triangulo_2(size=1):
    lista = []
    aux = []

    for i in range(0, size):
        if i != 0:
            aux.append(1)
        for j in range(0, size):
            if i == j:
                aux.append(1)
            elif j < i and j != 0:
                aux.append(
                    lista[i - 1][j - 1] + lista[i - 1][j] + lista[i - 2][i - (j + 1)]
                )
        lista.append(aux[::])
        aux.clear()

    return printer(lista)


triangulo_1(10)
triangulo_2(10)

"""
2 e 1
lista[2-1][1-1] + lista[2-1][1] + lista[2-2][i-(j+1)]
lista[1][0] + lista[1][1] + lista[0][2-(1+1)]

3 e 1
lista[3-1][1-1] + lista[3-1][1] + lista[3-2][i-(j+1)]
lista[2][0] + lista[2][1] + lista[1][3-(1+1)]

4 e 2
lista[i-1][j-1] + lista[i-1][j] + lista[i-2][i-(j+1)]
lista[3][1] + lista[3][2] + lista[2][4-(2+1)]

3, 2      3,1   2,1
"""
