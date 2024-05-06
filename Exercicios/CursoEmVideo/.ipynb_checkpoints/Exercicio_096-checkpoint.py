# Exercicio_096
def area(a,b):
    print(f'a área do seu terro é de {a*b}')


a = float(input("informe o comprimento do terreno. \n"))
b = float(input("informe a largura do terreno. \n"))

area(a,b)

# Solução do professor
def área(larg, comp):
    a = larg* comp
    
    print(f'A área de um terrenos {larg}x{comp} é de {a}m²')
   
 
print('Controle de Terrenos')
print('-'*20)

l = float(input('Largura(m): '))
c = float(input('Comprimento (m): '))

área(l, c)
