# Exercicio_115b

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    
    except FileNotFoundError:
        return False
    
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome, 'wt+') 
        #tanto o open, como close são funcões do python
        # o 'rt' para leitura o 'wt' para escrita, o + corresponde a criar um novo arquivo, logo escrever um novo arquivo
        a.close()
    
    except:
        print('Houve um ERRo na criação do arquivo')
    
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerarquivo(nome):
    from ex115 import cabeçalho
    
    try:
        a = open(nome, 'rt')
    
    except:
        print('Erro ao ler o arquivo')
    
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    
    except:
        (print('Houve um erro na abertura do arquivo'))
    
    else:
        try:
            a.write(f'{nome}; {idade} \n')
        
        except:
            print('Houve um erro na hora de escrever os dados')
        
        else:
            print(f'Novo registro de {nome} adicionado')
        
        finally:
            a.close()
