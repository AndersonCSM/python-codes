# Exercicio_064
num = cont = acu = 0

while num != 999:
    num = int(input('digite um número inteiro, use o valor 999 para sair \n'))
    if num != 999:   
        acu += num
        cont += 1

print('Foram digitados {} números e a soma deles é {}'.format(cont, acu ))
