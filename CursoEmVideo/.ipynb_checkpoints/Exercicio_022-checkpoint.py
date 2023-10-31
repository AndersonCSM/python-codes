# Exercicio_022
nome = input("escreva seu nome \n")
print(nome.upper())
print(nome.lower())
listaNome = nome.split()
print("O total de letras é: {}".format(len(''.join(listaNome))))
print("O primeiro nome possui {} letras".format(len(listaNome[0])))

#O professor utilizou do seguinte modelo para contar o total de letras do nome. Total de caracteres menos a contagem de caracteres vazios(espaços).
print("seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))

#Para imprimir a quantidade de caracteres do primeiro nome, utilizou-se o artifício de procurar o caractere vazio(espaço) que separa os nomes e utilizar a posição dele como o número de caracteres
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))
