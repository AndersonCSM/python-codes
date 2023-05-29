# Exercicio_026
frase = str(input("Insira sua frase \n")).strip().lower()

print("a quantidade de letras a que aparecem é de: {}".format(frase.count('a')))
print("O índice da primeira letra a é a {}".format(frase.find('a')+1))
print("O índice da última letra é {}".format(frase.rfind('a')+1))

# Resolução do professor
frase = str(input("digite uma frase: ")).upper()

print("a quantidade de letras A é de: {}".format(frase.count("A")))
print("A primeira letra a aparece na posição {".format(frase.find("A"+1)))
print("O índice da última letra é {}".format(frase.rfind('A')+1))
