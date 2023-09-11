# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 12:49:35 2023

@author: AnD_B
"""
"""
Classe roleta para melhorar a leitura do código
"""
import random

class Roleta:
    
    # Construtor padrão
    def __init__(self, aptidao, maximizar=False):
        self.intervalos = self._gerar_roleta(aptidao, maximizar)
    
    # Método que irá gerar as probabilidades e os intervalos da roleta
    def _gerar_roleta(self, aptidao, maximizar=False):
        probabilidades = []
        # Checa se o objeto é maximizar ou minimizar a função
        if maximizar:
            for e in aptidao:
                # se for maximizar, percorre cada elemento da lista e calcula sua
                # probabilidade no todo e adiciona a lista de probabilidades
                probabilidades.append(e/sum(aptidao))
        else:
            # se for minimizar, é preciso criar uma lista de aptidão inversa e
            # calcular a probabilidade no todo e adiciona a lista de probabilidades
            aptidao_inversa = [1/a for a in aptidao]
            for e in aptidao:
                probabilidades.append((1/e)/sum(aptidao_inversa))
        # Com as probabilidades se monta a roleta
        # a roleta deve possui n-1 intervalos, sendo n a quantidade de probabilidades
        per_roleta = [p*360 for p in probabilidades]
        pedaco = 0 # variável que será usada para calcular os pontos de intervalos
        roleta = [0] # inicia a lista roleta com o intervalo inferior, 0
        
        # Cria a roleta com os pontos de intervalo
        for i in range(len(per_roleta)):
            pedaco += per_roleta[i] # soma cada parte da roleta ao pedaco para definir os pontos
            roleta.append(pedaco)
        
        # Cria a lista com os intervalos
        intervalos = [] # lista dos intervalos
        for i in range(1, len(roleta)): # ao invés de percorrer de (0, roleta+1) se faz (1, roleta)
            intervalos.append((roleta[i-1], roleta[i])) # cada intervalo é definido pelo limite anterior e o atual

        return intervalos
    
    # Método para identificar em qual intervalo da roleta o número informado caiu
    def check_intervalo(self, valor):
        if 0 <= valor <= 360:
            for i, (inicio, fim) in enumerate(self.intervalos):
                if inicio < valor <= fim:
                        return i, (inicio, fim)
        else:
            return None
    
    # Método para identificar em qual intervalo da roleta o número informado caiu
    def check_intervalo_aleatorio(self):
        valor = random.randint(0, 360)
        if 0 <= valor <= 360:
            for i, (inicio, fim) in enumerate(self.intervalos):
                if inicio < valor <= fim:
                        return i, (inicio, fim)
        else:
            return None