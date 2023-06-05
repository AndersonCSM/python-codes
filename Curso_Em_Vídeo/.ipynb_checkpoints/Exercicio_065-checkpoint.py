# Exercicio_065
contador = 0
acumulador = 0
numero = 0
validador = 'S'

while validador != 'N':
    numero = int(input('Informe um número inteiro \n'))
    validador = str(input('Quer continuar S/N? \n')).strip().upper()
    contador += 1
    acumulador += numero
    
    if contador == 1:
        maior = numero
        menor = numero
    
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero

print('A média entre os números é {}'.format(acumulador/contador))
print('O menor valor é {} e o maior valor {}'.format(menor, maior))
