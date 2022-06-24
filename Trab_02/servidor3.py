import socket

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5002        # Porta que o Servidor esta

print('+-----------------------------------------------------+')
print('|                                                     |')
print('|             SERVIDOR DE CONCATENAÇÃO                |')
print('|                                                     |')
print('+-----------------------------------------------------+')

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
servidor.bind((HOST, PORT)) # Conecta ao servidor
servidor.listen(1) # Aceita conexoes de um cliente
print('Servidor escutando na porta', PORT,'...\n')

conexao, endereco = servidor.accept() # Aceita conexoes de um cliente
print('Conexão estabelecida com', endereco)

strings = conexao.recv(1024).decode()
strings = strings.split(' ')
string1 = strings[0]
string2 = strings[1]
print('Strings recebidas:', string1, 'e', string2)

if not string1 or not string2:
    conexao.close()

concatenacao = string1 + string2
print('Concatenação:', concatenacao)
conexao.send(concatenacao.encode())
conexao.close()
