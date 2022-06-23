# Servidor de concatenacao de strings

import socket

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5002        # Porta que o Servidor esta

print('========== SERVIDOR DE CONCATENACAO ==========')

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
servidor.bind((HOST, PORT)) # Conecta ao servidor
servidor.listen(1) # Aceita conexoes de um cliente
print('Servidor pronto para conexoes')

conexao, endereco = servidor.accept() # Aceita conexoes de um cliente
print('Conexao estabelecida com', endereco)

strings = conexao.recv(1024).decode()
strings = strings.split('+')
string1 = strings[0]
string2 = strings[1]
concatenacao = string1 + string2

if not string1 or not string2:
    conexao.close()
concatenacao = string1 + string2
conexao.send(concatenacao.encode())
conexao.close()

# string1 = conexao.recv(1024).decode() # Recebe a opção do cliente
# string2 = conexao.recv(1024).decode() # Recebe a opção do cliente

# concatenacao = string1 + string2
# conexao.send(str(concatenacao).encode()) # Envia a opção para o servidor
