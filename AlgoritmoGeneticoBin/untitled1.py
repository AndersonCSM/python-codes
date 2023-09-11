# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:15:00 2023

@author: AnD_B
"""

import random

# função de aptidão do problema
def f(x, y):
    return (x**3 + 2*y**4)**0.5

# função de aptidão para teste
def f2(x):
    return x**2 - 12*x + 40

def separar():
    print(" ")
    print("#"*115)
    print(" ") 
    
# função principal
def BinGenetic(func, X=[], population=5, maximizar=False, mutation=0.05):
    # Elementos da população
    elements = []
    bin_elements = []
     
    maior = 0
    # Escolhendo individuo para população
    for _ in  range(len(X)):
        # ETAPA DE ESCOLHER OS INDIVÍDUOS
        individuos = random.sample(X[_], population)       
        elements.append(individuos)

        if max(individuos) > maior:
            maior = max(individuos)
        
    # ETAPA DE GERAR O NÚMERO BINÁRIO DOS INDIVÍDUOS
    for _ in range(len(X)): 
        qtd_bin_maior = len(bin(maior)[2:])
        aux = []
        
        for i in elements[_]:
            num = bin(i)[2:]
            qtd_bits_num = len(num)
            
            if qtd_bits_num == qtd_bin_maior:
                aux.append(num)
            else:
                ajuste = qtd_bin_maior - qtd_bits_num
                num = "0" * ajuste + num
                aux.append(num)
             
        bin_elements.append(aux[::])
        aux.clear()
        
        ###################### ainda falta
        if len(X) > 1:
            aux = []
            for i in range(population):
                bin_full = ""
                for lista in bin_elements:
                    bin_full += lista[i]
                aux.append(bin_full)
            bin_elements_ant = bin_elements.copy() # Acredito que vai precisar
            
            # Substituindo os elementos binarios
            bin_elements.clear()
            bin_elements.append(aux)
            # print(bin_elements_ant)
    
    # Aptidão
    if len(X) == 1:
        lista_aptidao = [func(x) for x in elements[0]]
    elif len(X) == 2:
        lista_aptidao = [func(x, y) for x, y in zip(elements[0], elements[1])]
    elif len(X) == 3:
        lista_aptidao = [func(x, y, z) for x, y, z in zip(elements[0], elements[1], elements[2])]
    
    
    
    # probabilidades
    probabilidades = []
    
    if maximizar:    
        for e in lista_aptidao:
            probabilidades.append(e/sum(lista_aptidao))
    else:
        aptidao_inversa = [1/a for a in lista_aptidao]
            
        for e in lista_aptidao:
            probabilidades.append((1/e)/sum(aptidao_inversa))
    
    # Montagem da roleta
    per_roleta = [p*360 for p in probabilidades]
    pedaco = 0
    roleta = [0]
    
    for i in range(len(per_roleta)):
        pedaco += per_roleta[i]
        roleta.append(pedaco)

    intervalos = []    
    for i in range(1, len(roleta)):
        intervalos.append((roleta[i-1], roleta[i]))

    def check_intervalo(valor, intervalos):
        for i, (inicio, fim) in enumerate(intervalos):
            if inicio < valor <= fim:
                return i
    
    
    
    # Escolha dos pais
    idc_p1 = check_intervalo(random.randint(0, 360), intervalos)
    idc_p2 = check_intervalo(random.randint(0, 360), intervalos)
    p1 = bin_elements[0][idc_p1]
    p2 = bin_elements[0][idc_p2]
    
    
    
    
    # Operador de Crossover
    ponto_corte = random.choice(range(1, len(p1)))
    f1 = p1[:ponto_corte] + p2[ponto_corte:]
    f2 = p2[:ponto_corte] + p1[ponto_corte:]
    
    # Operador de mutação
    def update_filho(s, index, char):
        return s[:index] + str(char) + s[index+1:]
    
    mutacao = random.random()
    filhos = [f1, f2] # Lista de filhos
    filhos_atualizados = [] # Lista para armazenar os filhos atualizados
    
    # Itera sobre os filhos e cria uma cópia atualizada
    for filho in filhos:
        filho_atualizado = ""
        for i in range(len(filho)):       
            if mutacao < mutation:
                char = random.choice(['0', '1'])
                filho_atualizado = update_filho(filho_atualizado, i, char)
        
        filhos_atualizados.append(filho_atualizado)
    
    for i in range(len(filhos_atualizados)):
        if len(filhos_atualizados[i]) != 0:
            filhos[i] = filhos_atualizados[i]
    
    # Confirmação de mutação
    if mutacao < mutation:
        print("Houve mutação")
        print(f"{mutacao}")
        print(" ")

    
    # Elitismo
    
    # Operador de separação
    def separar_filho(s, qtd_bin_maior):
        elementos = int(len(s) / qtd_bin_maior)
        conjunto = []
        for i in range(elementos):
            conjunto.append(int(s[i * qtd_bin_maior : (i + 1) * qtd_bin_maior], 2))
    
        return conjunto

    if len(X) == 1:
        num_filho = [int(x, 2) for x in filhos]
        lista_aptidao_filho = [func(x) for x in num_filho]
    
    elif len(X) == 2:
        # Separe os filhos e crie uma lista de listas
        num_filho = [separar_filho(filho, qtd_bin_maior) for filho in filhos]
        # Calcule a aptidão
        lista_aptidao_filho = [func(x, y) for x, y in zip(num_filho[0], num_filho[1])]
        
    elif len(X) == 3:
        # Separe os filhos e crie uma lista de listas
        num_filho = [separar_filho(filho, qtd_bin_maior) for filho in filhos]
        # Calcule a aptidão
        lista_aptidao_filho = [func(x, y, z) for x, y, z in zip(num_filho[0], num_filho[1], num_filho[3])]
    
                                 
    # Atualizar a população
    print("Elementos sorteados")
    print(elements)
    print("Representação Gene-binário")
    print(bin_elements)
    print("Lista de aptidão para os elementos")
    print(lista_aptidao)
    print("Probabilidades de sorteio")
    print(probabilidades)
    print("Filhos")
    print(filhos)
    print("Indice dos pais")
    print(idc_p1)
    print(idc_p2)
    print("Filhos")
    print(num_filho)
    print("Aptidão dos filhos")
    print(lista_aptidao_filho)

separar()
X = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
BinGenetic(f, X, 5)
separar()
X = [[1, 2, 3, 4, 5]]
BinGenetic(f2, X, 5)
separar()    
