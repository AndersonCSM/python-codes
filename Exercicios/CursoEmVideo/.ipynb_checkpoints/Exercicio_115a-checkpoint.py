# Exercicio_115a

def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(f'{txt:^42}')
    print(linha())


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        
        except(ValueError, TypeError):
            print('\033[31m ERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        
        else:
            return n


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    
    print(linha())
    opc = leiaint('Sua opção: ')
    
    return opc
