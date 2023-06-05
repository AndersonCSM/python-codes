# Exercicio_027
nome = str(input("Insira seu nome completo \n")).strip().split()
print(f"Seu primeiro nome é {nome[0]}")
Como o nome foi dividido, a função len irá ler as entradas da lista(cada nome que foi dividido 0,1,2,3...) ao invez de cada caractere
print("Seu último nome é {}".format(nome[len(nome)-1]))
