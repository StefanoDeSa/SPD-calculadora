import socket
import sys

PORTA = 5000


def iniciar_cliente(host):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, PORTA))

    print(f"Conectado ao servidor {host}:{PORTA}")

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
    if len(sys.argv) < 2:
        print("Uso: python client.py <host>")
    else:
        host = sys.argv[1]
        iniciar_cliente(host)