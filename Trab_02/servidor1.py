#servidor de disponibilidade de serviços

import socket

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5000        # Porta que o Servidor esta
PORT_SOMA = 5001
PORT_CONCATENACAO = 5002

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
servidor.bind((HOST, PORT)) # Conecta ao servidor
servidor.listen(1) # Aceita conexoes de um cliente
print('Servidor pronto para conexoes')

conexao, endereco = servidor.accept() # Aceita conexoes de um cliente
print('Conexao estabelecida com', endereco)

mensagem_opcoes = 'Digite 1 para somar, 2 para concatenar e 3 para sair: '
conexao.send(mensagem_opcoes.encode()) # Envia a opção para o servidor

opcao = int(conexao.recv(1024).decode()) # Recebe a opção do cliente
mensagem_escolha = 'Você escolheu a opção: ' + str(opcao)
conexao.send(mensagem_escolha.encode()) # Envia a opção para o servidor

if opcao == 1:
    valor1 = int(conexao.recv(1024).decode()) # Recebe a opção do cliente
    valor2 = int(conexao.recv(1024).decode()) # Recebe a opção do cliente
    #enviar para o servidor de soma 
    conexao_soma = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
    conexao_soma.connect((HOST, PORT_SOMA)) # Conecta ao servidor
    conexao_soma.send(str(valor1).encode()) # Envia a opção para o servidor
    conexao_soma.send(str(valor2).encode()) # Envia a opção para o servidor
    soma = conexao_soma.recv(1024).decode() # Recebe a opção do cliente
    conexao.send(soma.encode()) # Envia a opção para o servidor
elif opcao == 2:
    string1 = conexao.recv(1024).decode()
    string2 = conexao.recv(1024).decode()
    #enviar para o servidor de concatenacao
    conexao_concatenacao = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
    conexao_concatenacao.connect((HOST, PORT_CONCATENACAO)) # Conecta ao servidor
    conexao_concatenacao.send(string1.encode()) # Envia a opção para o servidor
    conexao_concatenacao.send(string2.encode()) # Envia a opção para o servidor
    concatenacao = conexao_concatenacao.recv(1024).decode() # Recebe a opção do cliente
    conexao.send(concatenacao.encode()) # Envia a opção para o servidor
elif opcao == 3:
    #fechar
    conexao.close()