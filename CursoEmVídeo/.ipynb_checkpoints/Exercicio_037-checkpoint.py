# Exercicio_037
print('=-='*10)
num = int(input("informe um número inteiro para conversão: "))

print('=-='*10)
escolha = int(input("agora escolha entre as seguintes opções de conversões: \n 1- binário \n 2- octal \n 3- hexadecimal \n"))

print('=-='*10)
if escolha == 1:
    print("a transformação do número {0} para binário é: \'{1:b}\'".format(num, num))
elif escolha == 2:
    print("a transformação do número {} para octal é: \'{:o}\'".format(num, num))
elif escolha == 3:
    print("a transformação do número {} para hexadecimal é \'{:x}\'".format(num, num))
else:
    print("o número inserido não corresponde a uma transformações disponível")

# O modelo do professor para transformar e remover os dois digitos iniciais:
print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
