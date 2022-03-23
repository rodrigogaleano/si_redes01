import socket

HOST = '127.0.0.1'
PORT = 7777

#Família de Protocolo  e tipo de protocolo
#AF_INET -> IPV4
#SOCK_STREAM -> TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Solicita conexão ao servidor
cliente.connect((HOST, PORT))

#Enviando mensgem ao servidor
cliente.send(str.encode('Olá Mundo!'))

#Resposta do servidor
resposta = cliente.recv(1024)
print('Mensagem recebida do servidor:', resposta.decode())