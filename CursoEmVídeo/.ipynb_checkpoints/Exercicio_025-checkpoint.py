# Exercicio_025
nome = input("insira seu nome \n")
nome = nome.upper().strip().split()
print("Você possui silva no nome: {}".format("SILVA" in nome))

# Resolução diferente do professor
nome = input("insira seu nome")
print("Você possui silva no nome: {}".format("SILVA" in nome.upper()))
