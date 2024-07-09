import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    sc.connect(('127.0.0.1', 4444))

    while True:
        mensagem = input('mensagem: ').encode()
        sc.send(mensagem)
