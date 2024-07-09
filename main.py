import socket
import threading


def receber(cliente):
    while True:
        mensagem = cliente.recv(1024).decode('utf-8')
        if mensagem:
            print(mensagem)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    sc.bind(('127.0.0.1', 4444))
    sc.listen()
    print('servidor iniciado!')

    while True:
        cliente_sc, _ = sc.accept()
        print('novo cliente!')
        threading.Thread(target=receber, args=(cliente_sc,)).start()
