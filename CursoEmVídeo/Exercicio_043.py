# Exercicio_043
altura = float(input('informe sua altura: '))
massa = float(input('informe seu peso: '))
imc = massa / (altura ** 2)

if 0 < imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade morbida')
