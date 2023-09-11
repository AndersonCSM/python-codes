# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:27:44 2023

@author: Anderson Carlos da Silva Morais
"""
# Bibliotecas usadas
import random
from Roleta import Roleta
import copy

# Função de aptidão do problema
def function(x, y):
    return (x**3 + 2*y**4)**0.5


# Função de aptidão para teste
def function2(x):
    return x**2 - 12*x + 40


def separar_filho(s, qtd_bin_maior):
    elementos = int(len(s) / qtd_bin_maior)
    conjunto = []
    for i in range(elementos):
        conjunto.append(int(s[i * qtd_bin_maior : (i + 1) * qtd_bin_maior], 2))

    return conjunto


# Função auxiliar do algoritmo: 1
def pop_and_max(X, p):
    """
    Função que cria uma lista de lista com o tamanho da população informada e
    retorna o maior elemento da lista de lista.
    
    Entrada:
    X -> [[]]: lista de lista de números(int)
    p -> int: quantidade de elementos
    
    Retorno:
    populacao -> [[]]: lista de lista com tamanho p da população
    maior -> int: maior inteiro presente nas listas
    
    """
    size_entrada = len(X)
    maior = 0
    populacao = []
    
    # Achando o maior individuo da população e montando a população
    for lista in range(size_entrada):
        individuos = random.sample(X[lista], p) # Escolheu a quantidade p de individuos para a população    
        populacao.append(individuos)

        if max(individuos) > maior:
            maior = max(individuos)
        
    return populacao, int(maior)


# Função auxiliar do algoritmo: 2
def binario(populacao, maior):
    """
    Transforma uma lista de lista numérica em números binários com a quantidade
    de bits do maior número, que é informado.
    
    Entrada:
    populacao -> [[]]: lista de lista de números(int)
    maior -> int: maior elemento inteiro da população
    
    retorno:
    bin_populacao -> [[]] lista de lista de string representando binários
    """
    
    size = len(populacao) # Tamanho da população
    qtd_bits = len(bin(maior)[2:]) # quantidade de bits do maior 
    aux = [] # lista auxiliar
    bin_populacao = [] # lista para a populacao em binário
    
    # Percorre cada lista da população
    for i in range(size):
        # percorre cada elemento da população transformando em binário
        for j in populacao[i]:
            num = bin(j)[2:] # Transforma em binário
            bits_num = len(num) # conta a quantidade de bits
            # Verifica se a quantidade de bits é adequada, senão ajusta
            if bits_num == qtd_bits: 
                aux.append(num)
            else:
                ajuste = qtd_bits - bits_num
                num = "0" * ajuste + num
                aux.append(num)
    
        bin_populacao.append(aux[::]) # adiciona os elementos binários a respectiva lista
        aux.clear() # Limpa para próxima iteração
    
    return bin_populacao


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


# Função auxiliar do algoritmo: 4
def binario_genetico(bin_populacao):
    """
    Função responsável por transforma a população de números binários em genes
    Essa operação é importante para quando a população é formada por mais de um
    conjunto de genes, ou seja, mais de uma variável.
    
    Entrada:
    bin_população -> [[]]: lista de lista com os binários das variáveis
    
    Saída:
    aux ou bin_população[0] -> []: lista simples contendo os genes
    """
    size = len(bin_populacao[0]) # quantidade de elementos da lista

    if size > 1: # Se tiver mais de uma lista
        aux = []    
        for i in range(size): # percorre os indices dos elementos 
        # com indice zero ele irá concatenar os elementos de indice zero das listas percorridas
            bin_full = "" # reseta os elementos para a próxima concatenação
            for lista in bin_populacao: # percorre as listas, concatenando os elementos de indice i
                bin_full += lista[i]
            aux.append(bin_full) # adiciona em uma lista
        
        return aux
    
    else: # Se não tiver apenas desempacota
        return bin_populacao[0]


# Função auxiliar do algoritmo: 5
def pais(qtd, gene_populacao, r=Roleta):
    lista = []
    
    c = 0
    while c != qtd:
        indice = r.check_intervalo_aleatorio()[0]

        if gene_populacao[indice] not in lista:
            lista.append(gene_populacao[indice])
            c += 1
    
    return lista


# Função auxiliar do algoritmo: 6
def crossover(pais):
    """
    Função responsável pelo crossover dos elementos, esse procedimento se mostrou ostensivo
    sendo dividido em blocos para maior legibilidade.
    Entrada:
    genes_pais -> [[]]: lista de lista dos genes dos pais
    
    Saida:
    genes_filhos -> [[]]: lista de lista com os filhos
    
    """
    """
    Bloco 1
    
    Realiza o fatiamento dos genes de maneira aleatória e de acordo com o tamanho
    dos genes. Define n - 1 pontos de corte aleatório e fatia cada gene nos respectivos
    pontos de corte, adicionando-os a um lista. Todos os elementos e genes estão
    associados devido aos indices.
    """
    
    genes_cortados = [] # lista dos genes cortados
    qtd_pais = len(pais) # quantidade de pais
    size = len(pais[0]) # quantidade de caracteres, entendesse que todos os pais tem o mesmo tamanho
    
    indices_corte =sorted(random.sample(range(1, size), qtd_pais - 1)) # pontos de corte aleatório
    # quantidade de pontos de corte n - 1
    
    for pai in pais: # percorre cada pai para fatia-lo
        partes = []
        anterior = 0 # corte anterior
        for indice in indices_corte: # percorre os pontos de corte
            partes.append(pai[anterior:indice]) # adiciona a lista a fatia do pai correspondente ao intervalo de corte
            anterior = indice # atualiza o intervalo de corte anterior
        
        partes.append(pai[anterior:]) # Adiciona o resto que ficou de fora do corte
        genes_cortados.append(partes) # Adiciona todos os cortes a lista dos genes
    
    """
    Bloco 2
    
    Função mais auxiliar, responsável em separar os genes de cada pai de acordo
    com o ponto de cortes, basicamente irá adicionar todos os primeiros genes
    cortados a uma lista, e assim sucessivamente para o n genes cortados
    """
    size_corte = len(genes_cortados) # quantidade de listas de cortes
    qtd_corte = len(genes_cortados[0]) # quantidade de elementos por corte
        
    genes_indice = [] # lista dos genes agrupados por indice       
    for j in range(qtd_corte): # percorre cada elemento ex: [0, 1, 2]
        aux = [] # list auxiliar
        for i in range(size_corte ): # percorre cada lista de gene
            aux.append(genes_cortados[i][j]) # adiciona o elemento de cada lista com o mesmo indice
        
        genes_indice.append(aux) # adiciona a lista auxiliar a lisa final
    
    """
    Bloco 3
    
    Responsável por montar os filhos com a combinação de genes dos pais de maneira que cada
    filho seja uma combinação única dos pais, sem que se repita em dois filhos um mesmo gene. 
    """
    genes_cortadoss = copy.deepcopy(genes_indice)
    qtd_filhos = len(pais)

    genes_disponiveis = copy.deepcopy(genes_cortadoss)
    
    filhos = []
    genes_remover = []
    qtd_genes = len(genes_cortadoss)
    
       
    while len(filhos) < qtd_filhos:
        
        filho = "" # reseta a combinação filho
        for i in range(qtd_genes):
            gene = random.choice(genes_disponiveis[i])
            genes_remover.append(gene)
            
            filho += gene # concatenação do filho
        
        for i in range(qtd_genes):
            genes_disponiveis[i].remove(genes_remover[i])  
        genes_remover.clear()
        
        filhos.append(filho) # adiciona a combinação filho pronta
    
    return filhos # retorna os filhos gerados


# Função auxiliar do algoritmo: 7
def mutation(filhos_entrada, taxa_mutacao):
    """
    Representa o operador de mutação para os genes filhos
    se o valor aleatório for menor que a taxa de mutação que é um valor entre [0, 1]
    ocorre mutação nos genes.
    
    Entradas:
    filhos_entrada -> []: Lista com os filhos
    taxa_mutacao -> float: número que define se vai haver mutação ou não
    
        
    Saída:
    filhos -> []: lista contendo os filhos com mutação aleatória
    """
    
    filhos = filhos_entrada[:] # Deep copy dos filhos para atualizar os elementos
    mutacao = random.random() # Valor numérico que representa os número da mutação
    filhos_atualizados = [] # lista auxiliar para armazenar o filho atualizado
    
    # Função lambda responsável por atualizar uma parte do gene 
    update_filho = lambda s, index, char: s[:index] + char + s[index+1:]
    
    # Itera sobre os genes filhos e cria uma cópia atualizada
    for filho in filhos: # percorre os filhos
        filho_atualizado = "" # usado para cada filho
        for i in range(len(filho)): # percorre cada gene do filho
            if mutacao < taxa_mutacao: # verifica a condição de mutação para o gene
                char = random.choice(['0', '1']) # se verdadeiro, escolhe um gene aleatório
                filho_atualizado = update_filho(filho_atualizado, i, char) # atuailiza o gene filho
        
        filhos_atualizados.append(filho_atualizado) # adiciona o gene filho a uma lista auxiliar
    
    # Percorre os elementos atualizados
    for i in range(len(filhos_atualizados)):
        if len(filhos_atualizados[i]) != 0: # Se existem filhos atualizados, ou seja, modificados
        # a lista de filhos será atualizada com esses elementos
            filhos[i] = filhos_atualizados[i]
        
        # Se ocorrer mutação, será printado no prompt informando que houve mutação
        if mutacao < taxa_mutacao:
            print("Houve mutação")
            print(f"{mutacao}")
            print(" ")
            
    # Retorna os filhos
    return filhos


# Função auxiliar do algoritmo: 8
def auxiliar1(filhos, bin_populacao, func):
    """
    Função auxiliar responsável por separar os genes em valores numéricos e
    calcular a aptidão para cada gene.
    Entrada:
    filho -> []: lista dos filhos
    bin_populacao -> [[]]: populacao, será usada para descobrir o ponto de corte
    do gene filho caso tenha sido gerado a partir de combinação dos pais
    func -> function(): função de aptidão para calcular a aptidão dos genes
    
    Saída:
    [genes, aptidao] -> [[int, int], [float, float]]: retorna uma lista contendo
    os genes em inteiro e o valor deles na função de aptidão
    """
    qtd_genes = len(bin_populacao) # quantidade de variÃ¡veis que foram usadas para formar o cromossomo
    qtd_char = len(filhos[0]) // qtd_genes # quantidade de caracteres por cromossomo Ãºnico
        
    genes = [[] for _ in range(qtd_genes)] # Lista com os cromossomos

    for gene in filhos: # percorre cada gene da lista filhos
        for i in range(qtd_genes): # percorre um range com a quantidade de variÃ¡veis
            partes = gene[i * qtd_char : (i + 1) * qtd_char] # fatia o gene com a quantidade de caracteres
            genes[i].append(int(partes, 2)) # transforma em inteiro e adiciona na lista gene
    
    # calcula a aptidão para os genes
    aptidao = gen_aptidao(func, genes)
    
    # retornar os genes e suas aptidões
    return [genes, aptidao]


# Função auxiliar do algoritmo: 9
# A partir desse ponto o código para de ser generalizado para n variáveis
def att(filhos_att, pais, bin_populacao, func, maximizar):
    """
    Função auxiliar que serve para identificar se os filhos são melhores que os pais
    para realizar essa operação ele precisa saber quem são os pais e os seus valores
    na função de aptidão, além de saber se a operação é relativa a maximizar ou minimizar um valor
    Entrada:
        filhos_att -> []: lista com os filhos gerados em binário
        pais -> []: lista com os pais em binário
        bin_populacao -> [[]]: lista de listas com a população em binário
        func -> function(): função de aptidão
        maximizar -> Bool: booleano informando se deseja maximizar o valor(True/False)
        
    Saída:
        melhor = []: lista com os melhores individuso
    
    """
    f = auxiliar1(filhos_att, bin_populacao, func)  # Usa a função auxiliar para descobrir
    # os valores numéricos e seu valor de aptidão para os filhos
    p = auxiliar1(pais, bin_populacao, func) # o mesmo só que para os pais
    
    replace = [] # lista de controle para descobrir o melhor individuo e seu indice
    
    f_apt = f[1] # valor de aptidão dos filhos
    p_apt = p[1] # valor de aptidão dos pais
    
    f_num = f[0] #
    
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
            melhor.append([f_num[w][index]])
    
    if len(melhor) == 0:
        melhor = f_num
    
    print(f)
    print(p)
    
    return melhor

# Parâmetros iniciais
teste = 2
if teste == 1:
    func = function2
    X = [[1, 2, 3, 4, 5, 9, 12, 25]]
else:
    func = function
    X = [[1, 2, 3, 4, 5, 9, 10, 7], [1, 2, 3, 4, 5, 6, 9, 13]]

p = 5
maximizar = False
taxa_mutacao = 0.05
qtd_pais = 2

# Inicio da função
###############################################################################
# Gera a população com tamanho p
populacao, maior = pop_and_max(X, p) 

# Gerando a representação binária dos indivíduos como Strings
bin_populacao = binario(populacao, maior)

# Gerando o gene da população
gene_populacao = binario_genetico(bin_populacao)
 
# Calcula a função de aptidão para a população
aptidao = gen_aptidao(func, populacao)

# Cria o objeto roleta com os valores de aptidão
roleta = Roleta(aptidao, maximizar)

# Gerando o gene dos pais
gene_pais = pais(qtd_pais, gene_populacao, roleta) 

# Realizando o crossover
filhos = crossover(gene_pais)

# Realizando mutação
filhos_att = mutation(filhos, taxa_mutacao)

# (Verificando se existe um filho melhor)
best = att(filhos_att, gene_pais, bin_populacao, func, maximizar)

# Atualizar a população
# Montar uma população nova de mesmo tamanho, excluindo os piores  de tamanho dos melhores

