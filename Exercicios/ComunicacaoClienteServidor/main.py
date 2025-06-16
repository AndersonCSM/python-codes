import socket  # módulo socket para comunicação de rede
import sys  # módulo sys para manipulação de argumentos da linha de comando


# host como a porta padrão localhost, só aceita conexão da própria máquina
def run_server(host="127.0.0.1", port=65432):
    """Inicia o servidor para escutar conexões de clientes.
    Cria um objeto socket chamado s
    1. Específica o endereço IPv4 em socket.AF_INET
    2. Especeficia o tipo de protocolo de conexão como TCP em socket.SOCK_STREAM
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))  # associa o host e port ao socket
        s.listen()  # usa o socket para ouvir conexões de entrada.
        print(f"Servidor escutando em {host}:{port}")  # exibe que o servidor está escutando

        # O servidor pode aceitar múltiplas conexões sequencialmente (uma de cada vez)
        while True:  # loop para as múltiplas conexões possíveis do servidor
            conn, addr = s.accept()  # espera um cliente se conectar, atribuindo a conexão e endereço
            with conn:
                print(f"Conectado por {addr}")  # endereço do cliente
                while True:  # loop para comunicação do cliente
                    try:  # tenta receber os dados do cliente
                        data = conn.recv(1024)  # Recebe até 1024 bytes
                        if not data:  # se não receber os dados é desconexão
                            print(f"Cliente {addr} desconectou (sem dados).")
                            break

                        message = data.decode("utf-8")  # decoder da mensagem
                        print(f"Mensagem recebida de {addr}: {message}")  # informa que recebeu uma mensagem

                        if message.lower() == "sair":  # se o cliente informou que quer encerrar a conexão
                            print(f"Cliente {addr} solicitou desconexão.")  # informa na tela
                            conn.sendall("Servidor: Desconectando...".encode("utf-8"))  # mensagem de desconexão
                            break  # sai do loop de comunicação

                        # "Encaminha" a mensagem (neste caso, apenas processa e envia uma confirmação)
                        response = f"Servidor recebeu: '{message}'"
                        conn.sendall(response.encode("utf-8"))  # mensagem de resposta ao cliente
                    except ConnectionResetError:  # raise erros possíveis durante o uso
                        print(f"Conexão com {addr} foi resetada pelo cliente.")
                        break
                    except Exception as e:  # raise erros possíveis durante o uso
                        print(f"Erro ao comunicar com {addr}: {e}")
                        break
                print(f"Conexão com {addr} encerrada.")
            # Após o cliente desconectar, o servidor volta a escutar por novas conexões.


def run_client(host="127.0.0.1", port=65432):
    """Inicia o cliente para conectar ao servidor e enviar mensagens.
    Cria um objeto socket chamado s
    1. Específica o endereço IPv4 em socket.AF_INET
    2. Especeficia o tipo de protocolo de conexão como TCP em socket.SOCK_STREAM"""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:  # tenta estabelecer conexão com o servidor
            s.connect((host, port))  # associa o host e port ao socket
            print(f"Conectado ao servidor em {host}:{port}")  # informa que conectou a um servidor
        except ConnectionRefusedError:  # raise erros possíveis durante o uso
            print(f"Não foi possível conectar ao servidor em {host}:{port}. Verifique se o servidor está em execução.")
            return
        except Exception as e:  # raise erros possíveis durante o uso
            print(f"Erro ao conectar: {e}")
            return

        while True:  # loop para comunicação entre cliente e servidor
            message_to_send = input(
                "Digite a mensagem para o servidor (ou 'sair' para desconectar): "
            )  # mensagem para ser enviada
            if not message_to_send.strip():  # Evita enviar mensagens vazias
                print("Por favor, digite uma mensagem ou 'sair'.")
                continue

            try:  # bloco para tentar enviar mensagem
                s.sendall(message_to_send.encode("utf-8"))  # envia para o servidor

                if message_to_send.lower() == "sair":  # solicitação de desconexão
                    print("Enviando solicitação de desconexão para o servidor...")
                    # Espera uma confirmação do servidor antes de fechar, se houver
                    try:  # bloco esperando resposta do servidor para desconexão
                        response_data = s.recv(1024)  # recebe mensagem do servidor
                        if response_data:  # se receber, imprima
                            print(f"Resposta do servidor: {response_data.decode('utf-8')}")
                    except Exception as e:  # raise erros possíveis durante o uso
                        print(f"Nenhuma resposta final do servidor ou erro: {e}")
                    break

                # Espera a resposta do servidor do envio da mensagem em # 74
                response_data = s.recv(1024)
                if not response_data:  # Servidor fechou a conexão inesperadamente
                    print("Servidor fechou a conexão.")
                    break
                print(f"Resposta do servidor: {response_data.decode('utf-8')}")

            except ConnectionResetError:  # raise erros possíveis durante o uso
                print("A conexão foi resetada pelo servidor.")
                break
            except BrokenPipeError:  # raise erros possíveis durante o uso
                print("A conexão com o servidor foi perdida (Broken pipe).")
                break
            except Exception as e:  # raise erros possíveis durante o uso
                print(f"Erro ao enviar/receber dados: {e}")
                break

        print("Cliente desconectado.")


if __name__ == "__main__":  # tratamento para liberar permissões
    if len(sys.argv) < 2:  # maneira intuitiva de mostrar ao usuário como utilizar o código
        print("Uso: python main.py [server|client]")
        print("Exemplo para iniciar o servidor: python main.py server")
        print("Exemplo para iniciar o cliente: python main.py client")
        sys.exit(1)  # encerra o programa

    mode = sys.argv[1].lower()  # recebe o argumento direito do terminal, faz o tratamento

    if mode == "server":  # de acordo com o argumento informado, executa o servidor ou o cliente
        print("Iniciando o servidor...")
        run_server()  # inicia o servidor
    elif mode == "client":
        print("Iniciando o cliente...")
        run_client()  # inicia o cliente
    else:  # se o usuário passar um argumento inválido
        print(f"Modo desconhecido: {sys.argv[1]}. Use 'server' ou 'client'.")
