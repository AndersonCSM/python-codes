import os
import pygame
import auxiliar as aux  # Recursos auxiliares do código
import game  # Recursos do Game of Life
from auxiliar import *

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


class Project:  # Classe do Projeto de TCC
    Azul = [0, 74, 173]  # Cores código RGB
    Verde = [126, 217, 87]
    Preto = [0, 0, 0]
    Branco = [255, 255, 255]
    Azul_escuro = [36, 62, 106]
    Verde_abacate = [153, 204, 35]
    Ciano = [6, 168, 228]
    Cinza = [62, 68, 67]
    Verde_limao = [93, 173, 77]
    Vermelho = [226, 50, 54]
    Bege = [240, 240, 240]

    def __init__(self):  # Construtor de inicialização
        pygame.init()  # Inicia os recursos da biblioteca

        # self.width, self.height = 1920, 1080  # Dimensões da janela
        self.state = "MainMenu"  # Tela Inicial
        self.width, self.height = pygame.display.Info().current_w, pygame.display.Info().current_h

    def start(self):  # Máquina de estado responsável por evitar uma pilha de chamadas de funções
        icon_surface = pygame.Surface([32, 32], pygame.SRCALPHA)  # Remove o ícone do pygame
        pygame.display.set_icon(icon_surface)  # posiciona um ícone transparente no lugar

        while self.state != "Quit":  # Condição de finalizar o jogo
            self.game_of_life()  # Retorna para o jogo da vida

        pygame.quit()  # Encerra os recursos da biblioteca

    def game_of_life(self):  # Game of Life
        pygame.display.set_caption("Game of Life")  # Nome da Tela
        screen = pygame.display.set_mode([self.width, self.height], pygame.RESIZABLE)  # Tela do jogo
        clock = pygame.time.Clock()  # Controle de fps do menu principal

        # Criar duas superfícies separadas uma para o jogo e outra para o menu
        surface1 = pygame.Surface((int(self.width * 0.75), self.height))
        surface2 = pygame.Surface((int(self.width * 0.25), self.height))
        surface1.fill(self.Azul_escuro)  # Cor de fundo de cada superfície
        surface2.fill(self.Verde)  # Cor de fundo de cada superfície

        # Recursos do jogo | Escalas ≥ 10
        grid = game.Game(width=surface1.get_width(), height=surface1.get_height(), scale=10, offset=1, padding=10)
        running = True  # Variável de Controle para o jogo
        pause = True  # Variável de Controle para o jogo

        # Objetos em Tela
        g_width_button, g_height_button = 300, 60  # Nome largura x altura
        play_pause_button_rect = pygame.Rect((231, 80, g_height_button, g_height_button))  # rect das imagens
        bg_1 = pygame.Rect((10, 10, g_width_button, g_height_button))  # 10, 10 são as margens dos botões da tela

        # Carregar imagens de play e pause
        image_pause = pygame.transform.scale(
            pygame.image.load(os.path.join(os.path.dirname(__file__), "img", "pause.png")),
            (g_height_button, g_height_button))
        image_play = pygame.transform.scale(
            pygame.image.load(os.path.join(os.path.dirname(__file__), "img", "play.png")),
            (g_height_button, g_height_button))

        while running:  # loop do old
            clock.tick(60)  # fps da tela do jogo
            screen.fill(self.Azul_escuro)  # Limpa e define a cor da tela

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Verifica saída
                    running = False  # Quebra o while
                    self.state = "Quit"  # Muda o estado para quando retornar a função start finalizar

                if event.type == pygame.KEYUP:  # Verifica se alguma tecla foi pressionada
                    # chama a função keyup para verificar qual tecla foi pressionada
                    running, pause = self.keyup(event, running, grid, pause)

            # Cria e atualiza os recursos do menu
            self.update_menu_gof(surface2, bg_1, image_pause, image_play, play_pause_button_rect, grid, pause)
            # Executa o código para atualizar o grid
            grid.runnable(off_color=self.Branco, on_color=self.Verde, surface=surface1, pause=pause)
            # Verifica teclas que proporcionam maior interatividade
            interatividade_gof(grid)

            # associa o menu e grid a tela principal
            screen.blit(surface1, (0, 0))
            screen.blit(surface2, (int(self.width * .75), 0))

            pygame.display.flip()  # Atualiza o display
            pygame.display.update()  # Atualiza elementos de tela por uma função diferente

    def keyup(self, event, running, grid, pause):
        """
        Responde a eventos de teclado soltos durante a execução do jogo.

        Parameters
        ----------
        event : pygame.event.Event
            Evento de teclado solto.
        running: bool
            Estado de execução do jogo.
        grid: Grid
            Objeto da grade associado ao jogo.
        pause: bool
            Estado de pausa do jogo.

        Returns
        -------
        tuple
            Retorna uma tupla contendo o novo estado de execução do jogo e o novo estado de pausa.

        Notes
        -----
        - Se a tecla 'ESCAPE' for solta, encerra o jogo e retorna ao menu principal.
        - Se a tecla 'SPACE' for solta, alterna o estado de pausa.
        - Se a tecla 'C' for solta, limpa a grade e pausa o jogo.
        - Se a tecla 'R' for solta, gera uma nova grade aleatória.
        - Se a tecla 'LEFT' for solta e o timing da grade for maior que 1, diminui o timing.
        - Se a tecla 'RIGHT' for solta e o timing da grade for menor que 60, aumenta o timing.
        - Se a tecla 'TAB' for solta, aumenta o timing em 10 unidades, com limite de 60.
        - Se a tecla 'LEFT SHIFT' for solta, diminui o timing em 10 unidades, com limite de 1.
        """
        if event.key == pygame.K_ESCAPE:
            running = False
            self.state = "Quit"
        elif event.key == pygame.K_SPACE:
            pause = not pause
        elif event.key == pygame.K_c:
            grid.clear()
            pause = True
        elif event.key == pygame.K_r:
            grid.random_grid()
        elif event.key == pygame.K_LEFT and grid.timing > 1:
            grid.timing -= 1
        elif event.key == pygame.K_RIGHT and grid.timing < 60:
            grid.timing += 1
        elif event.key == pygame.K_TAB:
            grid.timing = min(grid.timing + 10, 60)
        elif event.key == pygame.K_LSHIFT:
            grid.timing = max(grid.timing - 10, 1)
        elif pygame.K_1 <= event.key <= pygame.K_9:
            numero = event.key - pygame.K_0
            grid.standard(numero)
        elif event.key == pygame.K_0:
            grid.standard(0)

        return running, pause

    def update_menu_gof(self, surface, bg_1, image_pause, image_play, play_pause_button_rect, grid, pause):
        """
        Atualiza a interface do menu do jogo Game of Life na tela.

        Parameters
        ----------
        surface : pygame.Surface
            Objeto de superfície sobre o qual a interface do menu será desenhada.
        bg_1 : pygame.Rect
            Objeto Rect representando a área de fundo do menu.
        image_pause : pygame.Surface
            Imagem representando o botão de pausa.
        image_play : pygame.Surface
            Imagem representando o botão de reprodução.
        play_pause_button_rect : pygame.Rect
            Objeto Rect representando a área clicável do botão de pausa/repodução.
        grid : Grid
            Objeto da grade associado ao jogo.
        pause : bool
            Estado de pausa do jogo.

        Returns
        -------
        None
            Atualiza a interface do menu na tela.

        Notes
        -----
        - Preenche a tela com verde.
        - Desenha o botão de pausa ou reprodução na tela com base no estado de pausa.
        - Cria botões e caixas de texto para exibir informações relevantes sobre o estado atual da grade do jogo.

        """
        surface.fill(self.Verde_abacate)  # Limpa a tela e define a cor verde

        surface.blit(image_pause if pause else image_play, play_pause_button_rect.topleft)  # atualiza a imagem

        aux.create_button(surface, caixa=bg_1, texto="Game of Life", cor_texto=self.Branco,
                          cor_caixa=self.Azul_escuro, size=60)

        elements = [("Linhas", grid.size[1], self.Azul_escuro, (10, 80, 93, 60)),
                    ("Colunas", grid.size[0], self.Azul_escuro, (113, 80, 93, 60)),
                    ("Total", grid.size[0] * grid.size[1], self.Azul_escuro, (216, 150, 93, 60)),
                    ("Vivas", grid.live, self.Ciano, (10, 150, 93, 60)),
                    ("Mortas", grid.dead, self.Vermelho, (113, 150, 93, 60)),
                    ("Atualização de Grid", f"{grid.timing} s^-1", self.Azul, (10, 220, 196, 60)),
                    ("Geração", grid.gen, self.Azul, (216, 220, 93, 60))]

        for element in elements:
            aux.get_values(texto=element[0], cor_texto=self.Branco, var=element[1], cor_var=self.Branco, font_size=25,
                           screen=surface, cor_caixa=element[2], alinhamento="midtop", pos=element[3])
