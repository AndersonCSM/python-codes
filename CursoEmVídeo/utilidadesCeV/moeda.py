def aumentar(valor=0, per=0, form=False):
    r = valor + valor * (per / 100)
    return r if form is False else moeda(r)


def diminuir(valor=0, per=0, form=False):
    r = valor - valor * (per / 100)
    return r if form is False else moeda(r)


def dobro(valor=0, form=False):
    r = valor * 2
    if form:
        r = moeda(r)
    return r


def metade(valor=0, form=False):
    r = valor / 2
    if form:
        r = moeda(r)
    return r


def moeda(valor):
    r = f"R${valor:.2f}"
    return r.replace(".", ",")


def resumo(valor=0, aum=0, dim=0):
    print("-" * 20)
    print("{:^20}".format("RESUMO DO VALOR"))
    print("-" * 20)
    print(f"Preço analisado: {moeda(valor):<10}")
    print(f"Dobro do preço:  {dobro(valor, True):<10}")
    print(f"Metade do preço: {metade(valor, True):<10}")
    print(f"{aum}% de aumento:  {aumentar(valor,aum,True):<10}")
    print(f"{dim}% de redução:  {diminuir(valor,dim,True):<10}")
