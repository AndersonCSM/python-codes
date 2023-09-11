# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:26:05 2023

@author: Windows10
"""
# Função de aptidão do problema
def function(x, y):
    return (x**3 + 2*y**4)**0.5


# Função de aptidão para teste
def function2(x):
    return x**2 - 12*x + 40

# Função auxiliar do algoritmo: 3
def gen_aptidao(func, populacao):
    """
    Calcula a aptidão da população para a função passada.
    
    Entrada:
    func -> function(): Função de aptidão escolhida
    população -> [[]]: lista de lista da população
    
    Saída:
    lista_aptidao -> []: lista com os valores de aptidão
    """
    size = len(populacao) # ler a quantidade de listas da população
    
    if size == 1:
        lista_aptidao = [func(x) for x in populacao[0]]
    else:
        lista_aptidao = [func(*args) for args in zip(*populacao)]
 
    return lista_aptidao

def elitismo(filhos, bin_populacao, func):
    qtd_genes = len(bin_populacao) # quantidade de variÃ¡veis que foram usadas para formar o cromossomo
    qtd_char = len(filhos[0]) // qtd_genes # quantidade de caracteres por cromossomo Ãºnico
        
    genes = [[] for _ in range(qtd_genes)] # Lista com os cromossomos

    for gene in filhos: # percorre cada gene da lista filhos
        for i in range(qtd_genes): # percorre um range com a quantidade de variÃ¡veis
            partes = gene[i * qtd_char : (i + 1) * qtd_char] # fatia o gene com a quantidade de caracteres
            genes[i].append(int(partes, 2)) # transforma em inteiro e adiciona na lista gene
    
    # chamada para aplica na funÃ§Ã£o de aptidÃ£o
    aptidao = gen_aptidao(func, genes)
    
    # Validar se o filho foi melhor que o pai e vale a pena substitui-lo
    
    return [genes, aptidao]
    
n = 2
if n == 1:
    filhos_att = ['01001', '00010']
    bin_populacao = [['11001', '01001', '00001', '00010', '01100']]
    func = function2
else:
    bin_populacao =[['1010', '0001', '0011', '1001', '0111'], ['0110', '0011', '1101', '0010', '0100']]
    filhos_att = ['00010011', '01010010']
    func = function
    pais = ['00010010', '01010011']


def att(filhos_att, pais, bin_populacao, func, maximizar):
    f = elitismo(filhos_att, bin_populacao, func) 
    p = elitismo(pais, bin_populacao, func)
    
    replace = []
    
    f_apt = f[1]
    p_apt = p[1]
    
    f_num = f[0]
    
    for j in range(len(f_apt)):
        if maximizar:
            if f_apt[j] > p_apt[j]:
                replace.append([j, f_apt[j]])
        else:
            if f_apt[j] < p_apt[j]:
                replace.append([j, f_apt[j]])
    
    melhor = []
    for k in range(len(replace)):
        index = replace[k][0]
        
        for w in range(len(f_num)):
            melhor.append(f_num[w][index])
    
    #print(f)
    #print(p)
    
    return melhor

sol = att(filhos_att, pais, bin_populacao, func, False)
