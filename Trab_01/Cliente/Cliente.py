import socket

HOST = '127.0.0.1'
PORTA = 7777

#Família de Protocolo  e tipo de protocolo
#AF_INET -> IPV4
#SOCK_STREAM -> TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Solicita conexão ao servidor
cliente.connect((HOST, PORTA))
print('Conectado ao servidor.\n')

#Solicita um arquivo ao servidor
#encode() transforma string em bytes
arquivo = str(input('Informe o nome do arquivo desejado: '))
cliente.send(arquivo.encode())

#Receber os dados do servidor
#wb: writebytes
with open (arquivo,'wb') as file:
    while True:
        dados = cliente.recv(1000000)
        if not dados:
            break
        file.write(dados)

print(f'{arquivo} recebido :)\n')