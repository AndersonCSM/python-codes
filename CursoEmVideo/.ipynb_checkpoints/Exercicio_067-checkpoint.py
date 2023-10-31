# Exercicio_067
print('-'*20)
print('Tabuada, digite número negativo para sair')
print('-'*20)

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    
    if num < 0:
        break
    
    cont = 1

    while cont <= 10:
        print(f'{num} x {cont:2} = {num*cont}')
        cont += 1

print('fim')   
