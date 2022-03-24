import socket

HOST = 'localhost'
PORTA = 7777

#Família de Protocolo  e tipo de protocolo
#AF_INET -> IPV4
#SOCK_STREAM -> TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))

#Coloca em escuta
servidor.listen(1)
print('Aguardando conexão de um cliente...\n')    

#Aceitar a conexão
conexao, endereco = servidor.accept()
print('Conectado em', endereco)

#Recebe o nome do arquivo
#decode() transofrma bytes em string
arquivo = conexao.recv(1024).decode()

#Abre o arquivo
#rb: readbytes
with open(arquivo, 'rb') as file:
    for dados in file.readlines(): #Lê toda o arquivo e envia ao cliente
        conexao.send(dados)

    print('Arquivo enviado com sucesso :)')       

