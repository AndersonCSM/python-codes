import matplotlib
import pygame

"""
This project was part of my undergraduate thesis. It is divided into three main modules:

- Auxiliary Module: File containing functions that are not essential for the operation of the Game of Life but are used
 in the project's construction;
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


def create_button(screen, caixa, texto, cor_caixa, cor_texto, clicado=False, size=36):
    """
    Função para criar botões ou caixas de texto.

    Parameters
    ----------
    screen : pygame.Surface
        Objeto de tela do pygame onde o botão será desenhado.
    caixa : pygame.Rect
        Objeto Rect do pygame representando a caixa do botão.
    texto : str
        Texto exibido no botão.
    cor_caixa : Tuple[int, int, int]
        Código RGB da cor da caixa do botão.
    cor_texto : Tuple[int, int, int]
        Código RGB da cor do texto do botão.
    clicado : bool, optional
        Estado do botão (clicado ou não) para animação de clique.
    size : int, optional
        Tamanho da fonte do texto no botão.

    Returns
    -------
    None
        Cria os objetos na tela informada.

    Notes
    -----
    - Inicializa os recursos do pygame.
    - Ajusta temporariamente o tamanho do botão se estiver clicado.
    - Desenha a caixa do botão, o texto e centraliza o texto dentro da caixa.
    - Restaura o tamanho original do botão após desenhar o texto.
    """

    pygame.init()  # Inicializa os recursos

    if clicado:  # Ajusta o tamanho do botão temporariamente se estiver clicado
        caixa.inflate_ip(-5, -5)  # Reduz o tamanho do botão

    pygame.draw.rect(screen, cor_caixa, caixa)  # Rect do botão
    fonte = pygame.font.Font(None, size)  # Fonte do texto
    texto_surface = fonte.render(texto, True, cor_texto)  # Texto da superfície
    texto_caixa = texto_surface.get_rect(center=caixa.center)  # Centraliza o texto
    screen.blit(texto_surface, texto_caixa)  # Associa o texto a caixa de texto

    if clicado:  # Restaura o tamanho original após desenhar o texto
        caixa.inflate_ip(5, 5)


def get_values(texto, cor_texto, var, cor_var, font_size, screen, cor_caixa, alinhamento="midtop", pos=None):
    """
    Função que retorna o valor de uma variável em uma caixa de texto.

    Parameters
    ----------
    texto : str
        Texto informativo do valor que será retornado.
    cor_texto : Tuple[int, int, int]
        Tupla com código RGB para a cor do texto.
    var : var
        Variável que será resgatada e exibida.
    cor_var : Tuple[int, int, int]
        Tupla com código RGB para a cor da variável.
    font_size : int
        Tamanho da fonte.
    screen : pygame.Surface
        Objeto de tela do pygame onde os objetos serão desenhados.
    cor_caixa : Tuple[int, int, int]
        Tupla com código RGB para a cor da caixa.
    alinhamento : str, optional
        Posição de alinhamento do texto ("midtop" ou "topleft").
    pos : Tuple[int, int, int, int], optional
        Posição da tela onde o objeto será desenhado (left, top, width, height).

    Returns
    -------
    None
        Desenha os objetos na tela informada.

    Notes
    -----
    - Define a fonte e renderiza o texto e a variável.
    - Cria um retângulo diretamente.
    - Desenha a caixa na tela.
    - Define a posição do texto e da variável com base no alinhamento.
    - Desenha os textos na tela.
    """
    font = pygame.font.Font(None, font_size)  # Define a fonte
    text_label = font.render(texto, True, cor_texto)  # Renderiza o texto
    text_var = font.render(str(var), True, cor_var)  # Renderiza a variável

    if pos is None:
        pos = (0, 0, 0, 0)

    box_rect = pygame.Rect(pos)  # Cria retângulo diretamente

    # Desenha a caixa na tela
    pygame.draw.rect(screen, cor_caixa, box_rect)

    # Dicionário de alinhamentos
    alignments = {
        "midtop": lambda rect: (rect.centerx, rect.top + 10),
        "topleft": lambda rect: (rect.left + 10, rect.top + 10),
    }

    # Define a posição do texto e da variável
    text_label_rect = text_label.get_rect(**{alinhamento: alignments[alinhamento](box_rect)})
    text_var_rect = text_var.get_rect(midtop=(box_rect.centerx, text_label_rect.bottom + 10))

    # Desenha os textos na tela
    screen.blit(text_label, text_label_rect)
    screen.blit(text_var, text_var_rect)


def interatividade_gof(grid):
    """
    Lida com a interatividade do usuário no modo Game of Life (GoF).

    Parameters
    ----------
    grid : Grid
        Objeto da grade associado ao jogo Game of Life.

    Returns
    -------
    None
        Atualiza o estado da grade com base na interatividade do usuário.

    Notes
    -----
    - Se o botão esquerdo do mouse for pressionado, a função chama o método `handle_mouse` da grade,
      definindo o estado da célula como vivo (1).
    - Se o botão direito do mouse for pressionado, a função chama o método `handle_mouse` da grade,
      definindo o estado da célula como morto (0).

    """
    if pygame.mouse.get_pressed() and pygame.mouse.get_pressed(num_buttons=3)[0]:  # Botão esquerdo do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        grid.handle_mouse(mouse_x, mouse_y, off=False)
    elif pygame.mouse.get_pressed() and pygame.mouse.get_pressed(num_buttons=3)[2]:  # Botão direito do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        grid.handle_mouse(mouse_x, mouse_y, off=True)
