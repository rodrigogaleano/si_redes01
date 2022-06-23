# Servidor com a soma de inteiros

import socket

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5001        # Porta que o Servidor esta

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
servidor.bind((HOST, PORT)) # Conecta ao servidor
servidor.listen(1) # Aceita conexoes de um cliente
print('Servidor pronto para conexoes')

conexao, endereco = servidor.accept() # Aceita conexoes de um cliente
print('Conexao estabelecida com', endereco)

valor1 = int(conexao.recv(1024).decode()) # Recebe a opção do cliente
valor2 = int(conexao.recv(1024).decode()) # Recebe a opção do cliente

soma = valor1 + valor2
conexao.send(str(soma).encode()) # Envia a opção para o servidor