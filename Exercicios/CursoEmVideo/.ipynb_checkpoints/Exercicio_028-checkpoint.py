# Exercicio_028
import random

numpc = random.randint(0,5)
print("o numero é {}".format(numpc))
num = int(input("tente adivinhar um número entre 0 e 5 \n"))
if num == numpc:
    print("você acertou o número")
else:
    print("você errou o número")
