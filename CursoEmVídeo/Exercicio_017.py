# Exercicio_017
import math

catOps = float(input("informe o valor do cateto oposto \n"))
catAdj = float(input("informe o valor para o cateto adjacente \n"))
print("a hipotenusa é {:.2f}".format(math.sqrt(((catOps**2)+(catAdj**2)))))

from math import hypot

co = float(input("informe o cateto oposto \n"))
ca = float(input("informe o cateto adjacente \n"))

print("a hipotenusa é {:.2f}".format(hypot(co,ca)))