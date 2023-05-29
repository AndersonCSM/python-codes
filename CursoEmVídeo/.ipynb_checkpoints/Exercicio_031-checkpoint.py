# Exercicio_031
distancia = float(input("Informe a distância da viagem em quilômetros: "))
if distancia <= 200:
    print("O valor a ser pago é de R${:.2f}".format(distancia*0.5))
else:
    print("O valor a ser pago na viagem é de R${:.2f}".format(distancia*0.45))
