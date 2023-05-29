# Exercicio_018
import math

graus = float(input("informe o ângulo \n"))
angulo = graus * 2 * math.pi / 360 
print("o cosseno é {:.2f}, o seno é {:.2f} e a tangente {:.2f}".format(math.cos(angulo), math.sin(angulo), math.tan(angulo))) 
