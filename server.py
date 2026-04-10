import re
import socket
import threading
import time

HOST = "0.0.0.0"
PORTA = 5000


def calcular_operacao(operacao):
    padrao = r"^\s*(-?\d+(?:\.\d+)?)\s*([\+\-\*/])\s*(-?\d+(?:\.\d+)?)\s*$"
    resultado = re.match(padrao, operacao)

    if not resultado:
        return "Erro: operação inválida. Use exemplos como 2 + 3 ou 10 / 2"

    numero1 = float(resultado.group(1))
    operador = resultado.group(2)
    numero2 = float(resultado.group(3))

    if operador == "+":
        valor = numero1 + numero2
    elif operador == "-":
        valor = numero1 - numero2
    elif operador == "*":
        valor = numero1 * numero2
    elif operador == "/":
        if numero2 == 0:
            return "Erro: divisão por zero"
        valor = numero1 / numero2
    else:
        return "Erro: operador inválido"

    if valor.is_integer():
        valor = int(valor)

    return f"Resultado: {valor}"


def atender_cliente(cliente_socket, endereco):
    print(f"Cliente conectado: {endereco}")

    try:
        while True:
            dados = cliente_socket.recv(1024)

            if not dados:
                break

            operacao = dados.decode("utf-8").strip()

            if operacao.lower() == "sair":
                cliente_socket.send("Conexão encerrada pelo cliente".encode("utf-8"))
                break

            resposta = calcular_operacao(operacao)
            time.sleep(2)
            cliente_socket.send(resposta.encode("utf-8"))

    except Exception as erro:
        print(f"Erro com o cliente {endereco}: {erro}")

    finally:
        cliente_socket.close()
        print(f"Cliente desconectado: {endereco}")


def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORTA))
    servidor.listen()

    print(f"Servidor iniciado em 0.0.0.0:{PORTA}")
    print("Aguardando conexões...")

    while True:
        cliente_socket, endereco = servidor.accept()

        thread_cliente = threading.Thread(
            target=atender_cliente,
            args=(cliente_socket, endereco),
            daemon=True
        )
        thread_cliente.start()


if __name__ == "__main__":
    iniciar_servidor()