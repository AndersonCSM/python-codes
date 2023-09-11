# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:38:47 2023

@author: Windows10
"""
# def update_populacao():
best = [[99, 88], [99, 88]]
populacao = [[10, 7, 3, 4, 2], [3, 1, 4, 5, 6]]
maximizar = False
piores = []
filhos_att = ['00010001', '10100010']
qtd_melhores = len(best[0])
aptidao = [32.12475680841802, 1.7320508075688772, 16.941074346097416, 239.7185850116757, 51.536394906900505]
f = aptidao.copy()

if maximizar:
    for i in range(qtd_melhores):
        num = min(f)
        piores.append(num)
        f.remove(num)  
else:
    for i in range(qtd_melhores):
        num = max(f)
        piores.append(num)
        f.remove(num)

index = []
for pior in piores:
    index.append(aptidao.index(pior))

nova_populacao = []
for i in range(len(populacao)):
    for j in range(qtd_melhores):
        populacao[i][index[j]] = best[i][j]
        


