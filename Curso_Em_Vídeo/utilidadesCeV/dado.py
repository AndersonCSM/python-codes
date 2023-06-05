def leiadinheiro(msg):
    valido = False

    while not valido:
        entrada = str(input(msg)).replace(",", ".").strip()

        if entrada.isalpha() or entrada == "":  # se for texto(alfanúmerico)
            print(f'\033[0;31m ERRO: "{entrada}" é um preço inválido! \033[0;31m ')

        else:
            valido = True
            return float(entrada)
