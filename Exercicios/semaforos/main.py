import threading
import time
import random

# Lista com os elementos
BUFFER_SIZE = 5
buffer = []

# Semáforos simulados
empty = BUFFER_SIZE  # conta os espaços vazios no buffer
full = 0  # conta os itens disponíveis no buffer
mutex = 1  # controla o acesso exclusivo à seção crítica

# Numero de itens a serem produzidos/consumidos antes de terminar
TOT_ITEMS = 10
producer_items = 0
consumer_items = 0

# Lock para proteger operações sobre os semáforos (simula atomicidade)
semaphore_lock = threading.Lock()


# Implementação de wait (P) com espera ativa
def wait(sem_name):
    """
    Operação de espera (decrementa o semáforo).
    Bloqueia a thread se o valor do semáforo for 0.
    """

    global empty, full, mutex
    while True:
        # AQUI usamos o lock para garantir que a leitura e o decremento sejam atômicos
        with semaphore_lock:  # Verifica qual semáforo deve ser 'esperado' (waited)
            if sem_name == "empty" and empty > 0:
                empty -= 1
                return
            elif sem_name == "full" and full > 0:
                full -= 1
                return
            elif sem_name == "mutex" and mutex > 0:
                mutex -= 1
                return
        time.sleep(0.001)  # espera ativa leve


# Implementação de signal (V)
def signal(sem_name):
    """
    Operação de sinalização (incrementa o semáforo).
    """

    global empty, full, mutex
    with semaphore_lock:
        if sem_name == "empty":
            empty += 1
        elif sem_name == "full":
            full += 1
        elif sem_name == "mutex":
            mutex += 1


# Funcao para a thread produtora
def producer_thread_func():
    # variaveis globais que serao usadas
    global buffer, producer_items

    while producer_items < TOT_ITEMS:
        item = random.randint(1, 100)  # Produz um item aleatorio

        # entrada na seção crítica
        wait("empty")  # espera por espaço disponível
        wait("mutex")  # espera pelo acesso exclusivo ao buffer

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
            # Saída da seção crítica
            # A ordem é importante: libere o mutex ANTES de sinalizar o semáforo.
            signal("mutex")  # libera o acesso ao buffer
            signal("full")  # sinaliza que há um novo item no buffer

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

        # Entrada na seção crítica
        wait("full")  # espera por item disponível
        wait("mutex")  # espera pelo acesso exclusivo ao buffer

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
            # Saída da seção crítica
            # A ordem é importante: libere o mutex ANTES de sinalizar o semáforo.
            signal("mutex")  # libera o acesso ao buffer
            signal("empty")  # sinaliza que há espaço livre no buffer

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
