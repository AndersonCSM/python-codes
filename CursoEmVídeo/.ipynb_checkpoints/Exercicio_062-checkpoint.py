# Exercicio_062
n1 = int(input('Informe o número para a PA: '))
razão = int(input('informe a razão da PA: '))
c = termos =1

while termos != 0:
    termos = int(input('Quantos termos você quer vê? '))
    c = 1
    
    while c <= termos:
        print (n1+(c-1)*razão, end=" ")
        c +=1

print('fim')

# Solução do professor
print('gerador de PA')
print('-='*10)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0

mais = 10 #SEMPRE IRÁ MOSTRAR OS 10 PRIMEIROS TERMOS, FALHA NA LÓGICA DO PROFESSOR

while mais != 0:
    total += mais

    while cont <= total:
        print('{} > '.format(termo), end=' ')
        termo += razão
        cont += 1
    
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    print('Foram mostrados {}'.format(total))
