# Calculadora Cliente-Servidor com Socket e Threads em Python

## Objetivo

Este projeto implementa uma calculadora simples no modelo cliente-servidor utilizando sockets TCP e threads em Python.

## Tecnologias utilizadas

- Python 3
- Socket
- Threading

## Estrutura do projeto

- server.py
  Inicia o servidor, aceita conexões e atende múltiplos clientes com threads.

- client.py
  Cliente que se conecta ao servidor e envia operações matemáticas.

- teste_multithreading.py
  Script de teste para simular vários clientes conectando ao mesmo tempo.

## Como executar

### Executar o servidor

No terminal, execute:

python server.py

### Executar o cliente

Na mesma máquina:

python client.py 127.0.0.1

Em outra máquina da mesma rede:

python client.py IP_DO_SERVIDOR

### Executar o teste

Com o servidor já em execução:

python teste_multithreading.py 127.0.0.1

Ou pela rede:

python teste_multithreading.py IP_DO_SERVIDOR