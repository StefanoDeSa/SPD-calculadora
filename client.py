import socket

HOST = "127.0.0.1"
PORTA = 5000


def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORTA))

    print(f"Conectado ao servidor {HOST}:{PORTA}")

    try:
        while True:
            operacao = input("Digite uma operação ou 'sair': ").strip()

            cliente.send(operacao.encode("utf-8"))

            resposta = cliente.recv(1024).decode("utf-8")
            print(resposta)

            if operacao.lower() == "sair":
                break

    except Exception as erro:
        print(f"Erro na conexão: {erro}")

    finally:
        cliente.close()
        print("Cliente encerrado.")


if __name__ == "__main__":
    iniciar_cliente()