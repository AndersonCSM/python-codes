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
# Importando as bibliotecas
import projeto


def file():  # Função de chamada
    project = projeto.Project()  # Objeto project
    project.start()  # Chamada do Método start


# Main
if __name__ == '__main__':
    file()
