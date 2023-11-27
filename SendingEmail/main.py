from message import Message

# Criando uma instância da classe Message
message = Message()

# Mensagem de exemplo
msg = f"""Olá
Está mensagem veio através de uma automação em Python, eai o que acho?

Atenciosamente,
Eu mesmo :p
"""

# Lendo informações de configuração do arquivo "config.txt"
"""
    Aqui é preciso fazer uma configuração pessoal, basicamente pegar uma senha de aplicativo do Gmail e ordenar na forma:
    1 linha - gmail
    2 linha - senha do app
"""
with open("config.txt") as f:
    content = f.readlines()
    f.close()

# Removendo caracteres de nova linha (\n) do final das linhas lidas
email = content[0][:-1]
senhaEmail = content[1][:-1]

# Enviando o email com anexo
message.send(to='andersoncarlos799@gmail.com',
             email=email,
             passwordapp=senhaEmail,
             msg=msg,
             attachment=True,
             directory="C:/Users/AnD_B/Desktop/ArquivoTeste.txt",
             typeattachment="txt",
             nameattachment="UmNomeDiferente")
