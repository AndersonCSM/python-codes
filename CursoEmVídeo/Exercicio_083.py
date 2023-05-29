# Exercicio_083
expressão = str(input('digite uma expressão \n'))

if expressão.count(')') == expressão.count('('):
    print('expressão válida')

else:
    print('expressão inválida')

print('fim')

# Solução do professor
expressão = str(input('Digite a expresão: '))
pilha = []

for simb in expressão:
    if simb == '(':
        pilha.append('(')
   
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
      
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressão válida')

else:
    print('Expressão inválida')
