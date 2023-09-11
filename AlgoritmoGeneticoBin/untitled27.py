# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:49:41 2023

@author: Windows10
"""
def function(x, y):
    return (x**3 + 2*y**4)**0.5

qtd_genes = len(bin_populacao) # quantidade de variÃ¡veis que foram usadas para formar o cromossomo
qtd_char = len(filhos[0]) // qtd_genes # quantidade de caracteres por cromossomo Ãºnico
    
genes = [[] for _ in range(qtd_genes)] # Lista com os cromossomos

for i in range(qtd_genes):
    for gene in filhos: # percorre um range com a quantidade de variÃ¡veis
        partes = gene[i * qtd_char : (i + 1) * qtd_char] # fatia o gene com a quantidade de caracteres
        genes[i].append(int(partes, 2)) # transforma em inteiro e adiciona na lista gene



# Validar se o filho foi melhor que o pai e vale a pena substitui-lo
bin_populacao =[['1010', '0001', '0011', '1001', '0111'], ['0110', '0011', '1101', '0010', '0100']]
filhos_att = ['00010011', '01010010']
func = function

pais = ['00010010', '01010011']