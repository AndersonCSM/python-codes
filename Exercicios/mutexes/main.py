import threading
import time
import random

# Lista com os elementos
BUFFER_SIZE = 5
buffer = []
key = 0  # 0 = livre, 1 = ocupado

# Constantes para os indices das threads
P_ID = 0
C_ID = 1

# Numero de itens a serem produzidos/consumidos antes de terminar
TOT_ITEMS = 10
producer_items = 0
consumer_items = 0


def mutex_lock():
    global key
    while True:
        if key == 0:
            key = 1  # tranca o recurso
            return
        else:
            time.sleep(0.01)  # espera


def mutex_unlock():
    global key
    key = 0  # libera o recurso


# Funcao para a thread produtora
def producer_thread_func():
    # variaveis globais que serao usadas
    global buffer, producer_items

    while producer_items < TOT_ITEMS:
        item = random.randint(1, 100)  # Produz um item aleatorio

        # entra na seção crítica
        mutex_lock()

        try:
            # Secao Critica: Produtor produz um item e o coloca no buffer
            size = len(buffer)
            if size < BUFFER_SIZE:
                buffer.append(item)
                print(f"Produtor produziu: {item} na posicao {size} (Buffer: {size}/{BUFFER_SIZE})")
                producer_items += 1  # controla os itens produzidos
                time.sleep(0.1)
            else:
                print(f"Produtor: Buffer cheio, esperando... (Buffer: {size}/{BUFFER_SIZE})")

        finally:
            # sai da seção crítica
            mutex_unlock()

        # Seção Restante: Ações adicionais após a seção crítica
        # Se o buffer estava cheio, uma pequena pausa antes de tentar novamente
        size = len(buffer)
        if size == BUFFER_SIZE:
            time.sleep(0.2)
        else:
            time.sleep(0.01)


# Funcao para a thread consumidora
def consumer_thread_func():
    # variaveis globais que serao usadas
    global buffer, consumer_items

    while consumer_items < TOT_ITEMS:

        # entra na seção crítica
        mutex_lock()

        try:
            size = len(buffer)
            # Secao Critica: Consumidor consome um item do buffer
            if size > 0:  # verifica se tem um elemento para consumir
                item = buffer.pop(0)  # consome o item do indice mais antigo [0]
                print(f"Consumidor consumiu: {item} da posicao (Buffer: {size}/{BUFFER_SIZE})")
                consumer_items += 1  # controla os itens consumidos
                time.sleep(0.1)
            else:
                print(f"Consumidor: Buffer vazio, esperando... (Buffer: {size}/{BUFFER_SIZE})")

        finally:
            # sai da seção crítica
            mutex_unlock()

        # Seção Restante: Ações adicionais após a seção crítica
        # Se o buffer estava vazio, uma pequena pausa antes de tentar novamente
        size = len(buffer)
        if size == 0:
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

    # Espera que as threads terminarem | qtd de elementos atingida
    producer.join()
    consumer.join()

    print("\nProducao e consumo finalizados.")
    print(f"Itens produzidos: {producer_items}")
    print(f"Itens consumidos: {consumer_items}")
    print(f"Buffer final: {buffer}")
    print(f"Contagem final no buffer: {len(buffer)}")
