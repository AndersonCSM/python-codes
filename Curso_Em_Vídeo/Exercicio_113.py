# Exercicio_113
def validador():
    try:
        i = int(input('Digite um número inteiro \n'))
        f = float(input('Digite um número fracionado \n'))

    except KeyboardInterrupt:
        print('O usuário não digitou valores')        
        return validador()

    except (ValueError, TypeError):
        print('Valores inválido, por favor insirar números.')
        return validador()

    except Exception as error:
        print(f'O erro encotrado foi {error.__cause__}')
        return validador()

    else:
        print(f'O valor inteiro foi {i} e o fracionado {f}')


validador()

# Solução do professor
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


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        
        except(ValueError, TypeError):
            print('\033[31m ERRO: por favor, digite um número real válido.\033[m')
            continue
        
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        
        else:
            return n     

num = leiaint('Digite um valor \n')
print(f'O valor digitado foi {num}')

num2 = leiafloat('Difite um real \n')
print(f'O valor real foi {num2}')
