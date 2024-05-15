# English Version
## ATTENTION!
The text below is an excerpt from my undergraduate thesis, subject to intellectual property and copyright laws. Use it to understand the project and seek further knowledge in the area. If you are interested in the complete work for academic purposes, please contact the [library](https://bibliotecas.ufersa.edu.br) of the Federal Rural University of the Semi-Arid, happy reading!

# Cellular Automata
The theory of cellular automata emerged in the late 1940s, by mathematicians John Von Neumann and Stanislaw Ulam, who sought to develop a model capable of merging biology with the concept of automata.

## Composition of Cellular Automaton
Cellular automata are complex, dynamic, and discrete systems that interact with each other over time. The composition of cellular automata systems presents essential characteristics for its modeling, such as:

* **Cell State:** the value or condition that a cell assumes, based on the problem addressed (alive, dead, infected). The state can be modified by means of transition rules;
* **Structure:** spatial and organizational system in which cells are subjected, such as: one-dimensional, two-dimensional (grid), and three-dimensional;
* **Geometry:** shape of cells, which can be square, hexagonal, or triangular;
* **Neighborhood:** a characteristic that defines how the cell interacts with others, being essential in implementing boundary conditions and transition rules of the system. There are three main types of neighborhoods: Von Neumann, Moore, and Extended Moore, as well as the concept of neighborhood radius, used to classify new neighborhoods based on the distance from the central cell to the farthest cell.
  * *Von Neumann Neighborhood:* considers the four closest neighboring cells to the centered cell, namely the cells above, below, left, and right;
  * *Moore Neighborhood:* considers a perimeter of neighboring cells around the centered cell, comprising eight neighboring cells, including diagonals, and can be referred to as a radius-one neighborhood;
  * *Extended Moore Neighborhood:* extends the Moore neighborhood to a perimeter of two neighboring cells, understood as a radius-two neighborhood, totaling 24 neighboring cells.

* **Transition Rules:** conditions for the change of cell states, utilizing other characteristics that compose the system to define the next state of the cell, with thousands of variations;
* **Boundary Condition:** conditions that define the behavior of cells at the structure's boundary (extremities of the structure). There are three basic boundaries that a structure can have, presented as follows:
  * *Fixed:* when the centered cell is in contact with the system's boundary, the neighborhood that is on the boundary or outside it is defined as a fixed state throughout the simulation, this is the most used boundary condition in literature, considering the state of boundary cells as null values;
  * *Periodic:* for the centered cell in contact with the boundary, the neighborhood that is on the boundary or outside it is extended to the other extreme, so that all cells of the system are connected;
  * *Reflective:* also when the centered cell is in contact with the system's boundary, the neighborhood that is on the boundary or outside it is the reflection of the cell's state.

## The Game of Life
One of the prominent applications of CA is the Game of Life developed by John Horton Conway. The game of life consists of a two-dimensional structure composed of square cells that can be in one of two mutually exclusive states: alive or dead. Using the Moore neighborhood, with a fixed boundary condition, while the system evolves over generations. The highlight of the Game of Life lies in the use of simple transition rules that generate various patterns and structures, the rules are:

* A live cell with one or fewer neighbors dies of loneliness;
* A live cell with more than three live neighbors dies of overpopulation;
* A live cell with 2 or 3 live neighbors survives to the next generation;
* A dead cell with exactly 3 live neighbors becomes alive;

From the rules of the Game of Life, it is possible to identify patterns in the structures that arise during the game.
* *Gliders:* shapes that move through the two-dimensional structure over generations, changing their shape in cycles;
* Stable Life: shapes that remain unchanged for any generation;
* *Oscillators:* shapes that oscillate cyclically over generations;

For more information, visit [LifeWiki](https://conwaylife.com/wiki/), or contact via email: andersoncarlos799@gmail.com.

# Versão PT-BR
## ATENÇÃO!
O texto abaixo é um fragmento do meu trabalho de conclusão de curso, estando sujeito a propriedade intelectual e leis de direito autoral, use-o para entender o projeto e buscar mais conhecimento na área, caso tenha interesse no trabalho completo para fins acadêmicos entre em contato com a [biblioteca](https://bibliotecas.ufersa.edu.br) da Universidade Federal Rural do Semi-Árido, boa leitura!

# Autômatos Celulares
A teoria dos autômatos celulares surgiu no final da década de 40, pelos matemáticos John Von Neumann e Stanislaw Ulam  que buscavam desenvolver um modelo capaz de mesclar biologia com o conceito de autômato.

## Composição do Autômato Celular
 Os autômatos celulares são sistemas complexos, dinâmicos e discretos, que interagem entre si ao longo do tempo. A composição do sistema dos autômatos celulares apresenta características essenciais para sua modelagem, como:

* **Estado da célula**: valor ou condição que uma célula assume, baseado no problema abordado (vivas, mortas, infectadas). O estado pode ser modificado por meios de regras de transição;
* **Estrutura**: sistema espacial e organizacional em que as células são submetidas, tais como: unidimensional, bidimensional (malha ou grid) e tridimensional;
* **Geometria**: forma das células, podendo ser: quadradas, hexagonais e triangulares;
* **Vizinhança**: característica que define como a célula interage com as demais, sendo característica essencial na implementação das condições de fronteira e nas regras de transição do sistema. Existem três tipos principais de vizinhanças, a de Von Neumann, Moore e Moore estendida, além do conceito de raio de vizinhança, usado para classificar novas vizinhanças com base na distância da célula central até a célula mais distante.
  * *Vizinhança de Von Neumann*: vizinhança que considera as quatro células vizinhas mais próximas da célula centrada, sendo as células superior, inferior, a esquerda e a direita;
  * *Vizinhança de Moore*: considera um perímetro de células vizinhas a partir da célula centrada, sendo oito células vizinhas, englobando as diagonais, e podendo ser referido como vizinhança de raio um;
  * *Vizinhança de Moore Estendida*: estende a vizinhança de Moore para um perímetro de duas células vizinhas, podendo ser entendida como vizinhança de raio dois, totalizando 24 células vizinhas.

* **Regras de transição**: condições para que ocorra a mudança de estados das células, utilizam das demais características que compõem o sistema para definir o próximo estado da célula, possuindo milhares de variações;
* **Condição de fronteira**: são condições que definem o comportamento das células no limite da estrutura (extremos da estrutura). Existem três limites básicos que uma estrutura pode possuir, apresentados a seguir:
  * *Fixo*: quando a célula centrada está em contato com a fronteira do sistema, a vizinhança que se encontra na fronteira ou fora dela é definida como um estado fixo durante toda a simulação, este é o limite mais usado na literatura, considerando o estado das células da fronteira como valores nulos;
  * *Periódico*: para a célula centrada em contato com a fronteira, a vizinhança que se encontra na fronteira ou fora dela é estendida para o outro extremo, de maneira que todas as células do sistema estão conectadas;
  * *Reflexivo*: também quando a célula centrada se encontra em contato com a fronteira do sistema, a vizinhança que se encontra na fronteira ou fora dela é o reflexo do estado da célula.


        
## O Jogo da Vida
Uma das aplicações de destaque dos ACs, é o jogo da vida (*Game of Life*) desenvolvido por John Horton Conway. O jogo da vida consiste em uma estrutura bidimensional composta por células quadradas que podem estar em um de dois estados  não simultâneos: vivas ou mortas. Utilizando a vizinhança de Moore, com condição de fronteira de limite fixo, enquanto a evolução do sistema ocorre ao longo das gerações. O destaque do jogo da vida está no uso de regras de transição simples  que geram padrões e estruturas diversas, sendo as regras:

* Uma célula viva com um vizinho ou menos, morre de solidão;
* Uma célula viva com mais de três vizinhos vivos, morre por superpopulação;
* Uma célula viva com 2 ou 3 vizinhos vivos, sobrevive para a próxima geração;
* Uma célula morta com exatamente 3 vizinhos vivos, nasce;

A partir das regras do jogo da vida é possível identificar padrões nas estruturas que surgiam durante o jogo.
* *Gliders*:  formas que se movem pela estrutura bidimensional ao longo das gerações, modificando sua forma em ciclos;
* Vida Estável: formas que permancem inalteradas para qualquer geração;  
* *Oscilators*: formas que oscilam de maneira cíclica ao longo das gerações; 

Para mais informações acessa a [Lifiwiki](https://conwaylife.com/wiki/), ou entre em contato pelo email: andersoncarlos799@gmail.com
