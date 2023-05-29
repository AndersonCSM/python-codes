# Exercicio_040
n1 = float(input('informe a primeira nota \n'))
n2 = float(input('informe a segunda nota \n'))

média =float((n1+n2)/2)
if média < 5:
    print("reprovado")
elif 5 <= média <= 6.9:
    print('Recuperação')
else:
    print('Aprovado') 
