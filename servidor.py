import socket

HOST = 'localhost'
PORT = 7777

#Família de Protocolo  e tipo de protocolo
#AF_INET -> IPV4
#SOCK_STREAM -> TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Objeto que guarda as informaçoes citadas nos comentários anteriores
servidor.bind((HOST, PORT)) #Vincula HOST e Porta

#Coloca em escuta
servidor.listen() 
print('Aguardando conexão de um cliente')

#Aceitar a conexão
conexao, endereco = servidor.accept()
print('Conectado em', endereco)

while True: 
	resposta = conexao.recv(1024)
	if not resposta: #Fecha a conexão quando não tiver mais dados
		print('Fechando a conexão')
		conexao.close()
		break
	conexao.send(resposta)  #Envia os dados de volta para o cliente