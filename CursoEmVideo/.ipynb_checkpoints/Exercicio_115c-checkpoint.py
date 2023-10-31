# Exercicio_115c
from Exercicio_115a import *
from time import sleep
from Exercicio_115b import *


arq = "curso em vídeo.txt"
if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    resposta = menu(
        ["Ver pessoas cadastradas", "Cadastrar pessoas", "Sair do sistema"],
    )
    if resposta == 1:
        lerarquivo(arq)

    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho("Saindo do sistema")
        break

    else:
        print("Erro, opção inválida, digite uma opção válida")
        sleep(1.5)
