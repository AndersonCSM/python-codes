def elitismo(filhos, bin_populacao):
    qtd_genes = len(bin_populacao) # quantidade de variáveis que foram usadas para formar o cromossomo
    qtd_char = len(filhos[0]) // qtd_genes # quantidade de caracteres por cromossomo único
        
    genes = [[] for _ in range(qtd_genes)] # Lista com os cromossomos

    for gene in filhos: # percorre cada gene da lista filhos
        for i in range(qtd_genes): # percorre um range com a quantidade de variáveis
            partes = gene[i * qtd_char : (i + 1) * qtd_char] # fatia o gene com a quantidade de caracteres
            genes[i].append(int(partes, 2)) # transforma em inteiro e adiciona na lista gene
    
    # chamada para aplica na função de aptidão
    
    
    # Validar se o filho foi melhor que o pai e vale a pena substitui-lo
    
    
    
    return genes

n = 1
if n == 1:
    filhos_att = ['01001', '00010']
    bin_populacao = [['11001', '01001', '00001', '00010', '01100']]
else:
    bin_populacao =[['1010', '0001', '0011', '1001', '0111'], ['0110', '0011', '1101', '0010', '0100']]
    filhos_att = ['00110100', '01010011']
    
x = elitismo(filhos_att, bin_populacao)
print(x)
