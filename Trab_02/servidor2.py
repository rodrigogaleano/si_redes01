# Servidor com a soma de inteiros

import socket

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5001        # Porta que o Servidor esta

print('========== SERVIDOR DE SOMA ==========')

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
servidor.bind((HOST, PORT)) # Conecta ao servidor
servidor.listen(1) # Aceita conexoes de um cliente
print('Servidor pronto para conexoes')

conexao, endereco = servidor.accept() # Aceita conexoes de um cliente
print('Conexao estabelecida com', endereco)

valores = conexao.recv(1024).decode()
valores = valores.split('+')
valor1 = int(valores[0])
valor2 = int(valores[1])
soma = valor1 + valor2

if not valor1 or not valor2:
    conexao.close()
soma = valor1 + valor2
print('Soma:', soma)
conexao.send(str(soma).encode()) # Envia a opção para o servidor
conexao.close()