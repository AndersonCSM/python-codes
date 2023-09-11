# Função de aptidão do problema
def function(x, y):
    return (x**3 + 2*y**4)**0.5

# Função de aptidão para teste
def function2(x):
    return x**2 - 12*x + 40

teste = 2
if teste == 1:
    func = function2
    X = [[1, 2, 3, 4, 5, 9, 12, 25]]
else:
    func = function
    X = [[1, 2, 3, 4, 5, 9, 10, 7], [1, 2, 3, 4, 5, 6, 9, 13]]

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

def elitismo(filhos_att, gene_pais):
    qtd_bits = len(filhos_att[0]) / len(filhos_att)
    
    # Operador de separação
    
    def separar_filho(s, qtd_bin_maior):
        elementos = int(len(s) / qtd_bin_maior)
        conjunto = []
        for i in range(elementos):
            conjunto.append(int(s[i * qtd_bin_maior : (i + 1) * qtd_bin_maior], 2))
    
        return conjunto
    
    filhos = separar_filho(filhos_att, qtd_bits)
    
    aptidao_filhos = gen_aptidao(func, genes)
    
    
pais = ['11000101', '11110010']
# qtd_pais não tem nada a haver com o corte
# o corte tem haver com o tamanho do maior binário

filhos = ['00010011', '01010001']
