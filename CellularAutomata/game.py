from time import sleep
import numpy as np  # biblioteca para trabalhar matriz
import pygame  # biblioteca para desenhar o grid

"""
This project was part of my undergraduate thesis. It is divided into three main modules:

- Auxiliary Module: File containing functions that are not essential for the operation of the Game of Life but are used in the project's construction;
- Game Module: File with the main class of the Game of Life, covering all essential characteristics of the game;
- Project Module: File with the project's interface where all modules are organized and implemented.

In addition to this basic organization, there is also the main file and the 'img' folder for play/pause images.

PT-BR
Este projeto fez parte do meu trabalho de conclusão de curso. Ele está dividido em três módulos principais:

- Módulo Auxiliar: Arquivo de funções que não são essenciais para o funcionamento do Game of Life, mas que são usadas 
na construção do projeto;
- Módulo Game: Arquivo com a classe principal do Game of Life, abordando todas as características essenciais do jogo;
- Módulo Projeto: Arquivo com a interface do projeto onde todos os módulos são organizados e implementados de fato.

Além desta organização básica, há também o arquivo principal e a pasta 'img' para as 
imagens de play/pause.
"""


# Classe do jogo da vida com todas as rotinas e variáveis para o funcionamento do jogo
class Game:
    def __init__(self, width, height, scale, offset, padding, limit="fixed"):  # Construtor de inicialização
        self.width = width  # largura da tela
        self.height = height  # altura da tela
        self.scale = scale  # escala das células
        self.offset = offset  # distância entre as células
        self.padding = padding  # padding das bordas da tela
        self.limit = limit  # Tipo do limite da borda, relativo às regras do Jogo da Vida

        # linhas são calculadas com o comprimento
        self.columns = int((self.width - 2 * padding - offset)) // (self.scale + offset)
        # colunas com a altura
        self.rows = int((self.height - 2 * padding - offset)) // (self.scale + offset)
        self.size = (self.columns, self.rows)  # Tamanho do grid

        self.grid_array = np.zeros(shape=self.size, dtype=int)
        self.live = 0  # Inicializa a contagem de células vivas como 0
        self.dead = self.columns * self.rows  # Inicializa a contagem de células mortas como total de células

        self.timing = 1  # timing para atualização do grid
        self.gen = 1  # controle de geração do grid

    def clear(self):  # Função para limpar o grid, ou seja, define todas as células como mortas
        self.grid_array = np.zeros(shape=self.size, dtype=int)  # Basta definir tudo como zero
        self.check()  # Função para contar as células
        self.gen = 1  # redefine as gerações

    def check(self):  # Função para contar as células do grid
        self.live = np.count_nonzero(self.grid_array == 1)
        self.dead = np.count_nonzero(self.grid_array == 0)

    def random_grid(self):  # Função responsável por randomizar valores das células da malha
        self.clear()  # limpa o grid previamente
        self.grid_array = np.random.randint(low=0, high=2, size=self.size)
        self.check()  # contagem das células

    def runnable(self, off_color, on_color, surface, pause):
        """
        Função responsável pelo funcionamento do jogo por completo.

        Parameters
        ----------
        off_color : Tuple[int, int, int]
            Código RGB da cor para células mortas.
        on_color : Tuple[int, int, int]
            Código RGB da cor para células vivas.
        surface : pygame.Surface
            Objeto sobre o qual o jogo será desenhado.
        pause : bool
            Variável que controla a atualização do grid.

        Returns
        -------
        None
            Retorna o jogo.

        Notes
        -----
        - Percorre o grid desenhando os quadrados na posição correta.
        - Aplica as regras do jogo se não estiver pausado.
        - Aplica um timing para controle de atualização do grid.
        - Atualiza as gerações.
        - Aplica as regras do jogo da vida.
        - Atualiza o array do grid.
        - Chama o método `check` para atualizar a contagem de células.
        - github:

        """
        grid_array = self.grid_array.copy()

        for x in range(self.columns):  # Percorre o grid desenhado os quadrados na posição correta
            for y in range(self.rows):
                y_pos = self.padding + y * (self.scale + 1)  # 1 é o offset
                x_pos = self.padding + x * (self.scale + 1)  # 1 é o offset

                if grid_array[x][y] == 1:  # cor da célula de estado 1
                    color = on_color
                else:  # cor da célula de estado 0
                    color = off_color

                pygame.draw.rect(surface, color, [x_pos, y_pos, self.scale, self.scale])

        nextc = np.ndarray(shape=self.size, dtype=int)  # grid auxiliar para se aplicar as regras do jogo

        if not pause:  # Aplica as regras do jogo se não estiver pausado
            sleep(self.timing / 60)  # timing para controle de atualização do grid
            self.gen += 1  # atualização das gerações

            for x in range(self.columns):
                for y in range(self.rows):
                    state = self.grid_array[x][y]

                    # Condições da simulação
                    neighbours = self.get_neighbours(x=x, y=y, limit=self.limit, neighborhood="moore")

                    # Regras do jogo da vida
                    if state == 0 and neighbours == 3:
                        nextc[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        nextc[x][y] = 0
                    else:
                        nextc[x][y] = state

            self.grid_array = nextc  # Atualiza o array

        self.check()  # atualiza a contagem de células

    def handle_mouse(self, x, y, off=False):  # Modifica o valor de uma célula específica
        """
        Modifica o valor de uma célula específica.

        Parameters
        ----------
        x : int
            Posição em x na matriz.
        y : int
            Posição em y na matriz.
        off : bool, optional
            Valor booleano para definir o estado da célula.

        Returns
        -------
        None
            Atualiza o valor da célula na matriz.

        Notes
        -----
        - Calcula a posição corrigida na matriz.
        - Modifica o valor da célula na posição especificada com base no estado fornecido (1 para viva, 0 para morta).
        - Chama o método `check` para atualizar a contagem de células.

        """
        # calculando a posição corrigida
        _x = (x - self.padding) // (self.scale + 1)  # 1 é o offset
        _y = (y - self.padding) // (self.scale + 1)  # 1 é o offset

        if 0 <= _x < self.columns and 0 <= _y < self.rows:
            if not off:
                valor = 1
            else:
                valor = 0

            self.grid_array[_x][_y] = valor

        self.check()  # atualiza a contagem de células

    def get_neighbours(self, x, y, limit="fixed", neighborhood="moore"):
        """
        Função para calcular a quantidade de vizinhos de uma célula baseado na condição de fronteira e
        o tipo de vizinhança definido.

        Parameters
        ----------
        x : int
            Posição x na matriz.
        y : int
            Posição y na matriz.
        limit : str, optional
            Define a condição de fronteira da malha:
            - "fixed": fixo, a uma parede nas bordas.
            - "periodic": periódico, não existe uma borda, as células formam uma esfera.
        neighborhood : str, optional
            Tipo da vizinhança da célula:
            - "moore": células vizinhas com diagonais, 8 vizinhos.
            - "moore_extended": células estendidas, duas células em cada direção, incluindo diagonais, 24 vizinhos.

        Returns
        -------
        int
            Número de vizinhos da célula na posição especificada.

        Notes
        -----
        - Calcula a quantidade de vizinhos da célula na posição especificada.
        - Utiliza a condição de fronteira e o tipo de vizinhança fornecidos para determinar os vizinhos.
        """
        # Definindo o tipo de vizinhança e o limite na fronteira
        lim_inf, lim_sup = (-1, 2) if neighborhood == "moore" else (-2, 3)
        total = 0  # total de vizinhos

        if limit == "periodic":
            for n in range(lim_inf, lim_sup):
                for m in range(lim_inf, lim_sup):
                    x_edge = (x + n + self.columns) % self.columns
                    y_edge = (y + m + self.rows) % self.rows
                    total += self.grid_array[x_edge][y_edge]

        elif limit == "fixed":
            r = self.columns
            c = self.rows

            for n in range(lim_inf, lim_sup):
                for m in range(lim_inf, lim_sup):
                    x_edge = x + n
                    y_edge = y + m
                    if 0 <= x_edge < r and 0 <= y_edge < c:
                        total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total
