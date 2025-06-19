import threading
import time
import random

# Configuracoes do Buffer -> sera o recurso compartilhado entre produtor e consumidor
# Uso de buffer circular, ou seja, volta para o inicio
BUFFER_SIZE = 5
buffer = [-1] * BUFFER_SIZE
in_index = 0
out_index = 0
count = 0

# Variaveis do Algoritmo de Peterson
N = 2  # Numero de threads (0 para produtor, 1 para consumidor)
flag = [False] * N  # Sinalizadores para indicar prontidao
turn = 0  # Variavel para indicar a vez

# Constantes para os indices das threads
P_ID = 0
C_ID = 1

# Numero de itens a serem produzidos/consumidos antes de terminar
TOT_ITEMS = 10
producer_items = 0
consumer_items = 0


# Funcao para a thread produtora
def producer_thread_func():
    # indica as variaveis globais que serao usadas
    global in_index, count, turn, producer_items

    while producer_items < TOT_ITEMS:
        item = random.randint(1, 100)  # Produz um item aleatorio

        flag[P_ID] = True  # Produtor esta pronto para produzir
        turn = C_ID  # Da a vez ao consumidor

        while flag[C_ID] and turn == C_ID:  # Espera a vez do consumidor
            time.sleep(0.01)  # Pequena espera
            pass

        # Secao Critica: Produtor produz um item e o coloca no buffer
        if count < BUFFER_SIZE:
            buffer[in_index] = item
            print(f"Produtor produziu: {item} na posicao {in_index} (Buffer: {count+1}/{BUFFER_SIZE})")
            in_index = (in_index + 1) % BUFFER_SIZE  # incrementa o indice de entrada no buffer circular
            # (0 + 1) % 5 = 1; (4 + 1) % 5 = 1; reinicia o ciclo
            count += 1  # adiciona um elemento a contagem
            producer_items += 1  # controla os itens produzidos
            time.sleep(0.1)
        else:
            print(f"Produtor: Buffer cheio, esperando... (Buffer: {count}/{BUFFER_SIZE})")

        flag[P_ID] = False  # Produtor saiu da secao critica

        # Seção Restante: Ações adicionais após a seção crítica
        # Se o buffer estava cheio, uma pequena pausa antes de tentar novamente
        if count == BUFFER_SIZE:
            time.sleep(0.2)
        else:
            time.sleep(0.01)


# Funcao para a thread consumidora
def consumer_thread_func():
    # indica as variaveis globais que serao usadas
    global out_index, count, turn, consumer_items

    while consumer_items < TOT_ITEMS:
        flag[C_ID] = True  # Consumidor esta pronto para consumir
        turn = P_ID  # Da a vez ao produtor
        while flag[P_ID] and turn == P_ID:  # Espera a vez do consumidor
            time.sleep(0.01)
            pass

        # Secao Critica: Consumidor consome um item do buffer
        if count > 0:  # verifica se tem um elemento para consumir
            item = buffer[out_index]  # usa out_index para resgatar o elemento do buffer
            # exibe na tela a operacao
            print(f"Consumidor consumiu: {item} da posicao {out_index} (Buffer: {count-1}/{BUFFER_SIZE})")
            out_index = (out_index + 1) % BUFFER_SIZE  # atualiza out_index (0 + 1) % 5 => 1 mod 5 => 1
            # 5 % 5 = 0 ou seja retorna pro inicio
            count -= 1  # diminui um elemento a contagem
            consumer_items += 1  # controla os itens consumidos
            time.sleep(0.1)
        else:
            print(f"Consumidor: Buffer vazio, esperando... (Buffer: {count}/{BUFFER_SIZE})")

        flag[C_ID] = False  # Consumidor saiu da secao critica

        # Seção Restante: Ações adicionais após a seção crítica
        # Se o buffer estava vazio, uma pequena pausa antes de tentar novamente
        if count == 0:
            time.sleep(0.2)
        else:
            time.sleep(0.5)


if __name__ == "__main__":
    # Cria as threads produtora e consumidora
    producer = threading.Thread(target=producer_thread_func)
    consumer = threading.Thread(target=consumer_thread_func)

    # Inicia as threads
    producer.start()
    consumer.start()

    # Espera que as threads terminem
    producer.join()
    consumer.join()

    print("\nProducao e consumo finalizados.")
    print(f"Itens produzidos: {producer_items}")
    print(f"Itens consumidos: {consumer_items}")
    print(f"Buffer final: {buffer}")
    print(f"Contagem final no buffer: {count}")
