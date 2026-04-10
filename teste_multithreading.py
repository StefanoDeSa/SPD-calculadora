import socket
import threading
import sys
import time

PORTA = 5000
OPERACOES = [
    "2 + 3",
    "10 * 5",
    "100 / 4",
    "7 - 2",
    "9 * 9",
    "50 / 2",
    "8 + 12",
    "30 - 10"
]


def cliente_teste(host, operacao, indice):
    try:
        inicio = time.time()

        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((host, PORTA))

        print(f"[Cliente {indice}] Conectado e enviando: {operacao}")
        cliente.send(operacao.encode("utf-8"))

        resposta = cliente.recv(1024).decode("utf-8")
        fim = time.time()

        print(f"[Cliente {indice}] Resposta: {resposta} | Tempo: {fim - inicio:.2f}s")

        cliente.send("sair".encode("utf-8"))
        cliente.recv(1024)

        cliente.close()

    except Exception as erro:
        print(f"[Cliente {indice}] Erro: {erro}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python teste_multithreading.py <host>")
        return

    host = sys.argv[1]
    threads = []

    inicio_total = time.time()

    for i, operacao in enumerate(OPERACOES, start=1):
        thread = threading.Thread(
            target=cliente_teste,
            args=(host, operacao, i)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    fim_total = time.time()
    print(f"\nTempo total do teste: {fim_total - inicio_total:.2f}s")


if __name__ == "__main__":
    main()