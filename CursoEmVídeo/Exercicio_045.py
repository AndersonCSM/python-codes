# Exercicio_045
import random
from time import sleep

escolhas = ['pedra', 'tesoura', 'papel'] #escolha do computador
pc = random.choice(escolhas)

print(pc)
print('=-='* 20) #amostra das opções
print('1-Pedra') 
print('2-tesoura')
print('3-Papel')
print('=-='* 20)
jogador = int(input('Você está jogando pedra, papel tesoura contra o computador, faça sua escolhe e tente vencê-lo! \n'))

jogador = escolhas[jogador-1] #Escolha de decisões
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

# Tomada de decisões
if jogador == 'pedra' and pc == 'tesoura' or jogador == 'tesoura' and pc == 'papel' or jogador == 'papel' and pc == 'pedra':
    print(f"você venceu, você escolheu {jogador} e o computador {pc}")
elif jogador == pc:
    print(f"Empate, vocês escolheram a mesma coisa que foi {jogador}")
else:
    print(f"você perdeu, vocÊ escolheu {jogador} e o computador {pc}")
