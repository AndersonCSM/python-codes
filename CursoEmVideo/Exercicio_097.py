# Exercicio_097
def escreva(text):
    tamanho = len(str((text)))+4
    
    print('='*tamanho)
    print(f'  {text}')
    print('='*tamanho)


escreva(str(input('escreva uma mensagem \n')))
