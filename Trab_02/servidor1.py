#Servidor de disponibilidade de serviços
import socket # Importa o módulo socket

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5000 
PORT_SOMA = 5001 #Porta do servidor de soma
PORT_CONCATENACAO = 5002 #Porta do servidor de concatenação

print('+-----------------------------------------------------+')
print('|                                                     |')
print('|      SERVIDOR DE DISPONIBILIDADE DE SERVIÇOS        |')
print('|                                                     |')
print('+-----------------------------------------------------+\n')

# ===== Cria o socket do servidor =====

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
servidor.bind((HOST, PORT)) # Conecta ao servidor

servidor.listen(1) # Escuta a conexão
print('Servidor escutando na porta', PORT,'...\n')
conexao_cliente, endereco = servidor.accept() # Aceita a conexão

print('Conexão estabelecida com', endereco, '!\n') # Imprime mensagem de conexão

# ===== Informa as opções na tela para escolha =====
msg_opcoes = 'Opções: \n 1 - Somar\n 2 - Concatenar\n 3 - Sair\n' # Mensagem de opções
conexao_cliente.send(msg_opcoes.encode()) # Envia a opção para o servidor

# ===== Recebe a opção do cliente =====

opcao = conexao_cliente.recv(1024).decode() # Recebe a opção do cliente
print('Opção escolhida pelo cliente: ' + opcao) # Imprime a opção escolhida

if opcao == '1':
    msg_escolha = 'Você escolheu somar!' # Mensagem de escolha
    conexao_cliente.send(msg_escolha.encode()) # Envia a mensagem de escolha

elif opcao == '2':
    msg_escolha = 'Você escolheu concatenar!'
    conexao_cliente.send(msg_escolha.encode()) # Envia a mensagem de escolha
elif opcao == '3':
    msg_escolha = 'Você escolheu sair!'
    conexao_cliente.send(msg_escolha.encode()) # Envia a mensagem de escolha
    conexao_cliente.close() # Fecha a conexão
else:
    msg_escolha = 'Opção inválida!'
    conexao_cliente.send(msg_escolha.encode()) # Envia a mensagem de escolha

# ===== Repassa para o servidor responsável =====

valor1 = conexao_cliente.recv(1024).decode() # Recebe o valor 1
valor2 = conexao_cliente.recv(1024).decode() # Recebe o valor 2
valores = valor1 + ' ' + valor2 # Atribui os valores a uma string separando por espaço

# --- Soma ---
if opcao == '1':
    #Estabalece conexão com o servidor de soma
    conexao_soma = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
    conexao_soma.connect((HOST, PORT_SOMA)) # Conecta ao servidor

    #Envia os valores para o servidor de soma
    print('Enviando para o servidor de soma...')
    conexao_soma.send(str.encode(valores)) # Envia a opção para o servidor

    #Recebe o resultado da soma
    print('Recebendo do servidor de soma...')
    resultado = conexao_soma.recv(1024).decode() # Recebe o resultado da soma
    print('Resultado da soma: ' + resultado) # Imprime o resultado da soma
    print('Enviando para o cliente...')
    conexao_cliente.send(resultado.encode()) # Envia o resultado para o cliente

elif opcao == '2':
    #Estabelece conexão com o servidor de concatenação
    conexao_concatenacao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexao_concatenacao.connect((HOST, PORT_CONCATENACAO)) # Conecta ao servidor

    #Envia os valores para o servidor de concatenação
    print('Enviando para o servidor de concatenação...')
    conexao_concatenacao.send(str.encode(valores)) # Envia a opção para o servidor

    #Recebe o resultado da concatenação
    print('Recebendo do servidor de concatenação...')
    resultado = conexao_concatenacao.recv(1024).decode() # Recebe o resultado da concatenação
    print('Resultado da concatenação: ' + resultado) # Imprime o resultado da concatenação
    print('Enviando para o cliente...')
    conexao_cliente.send(resultado.encode()) # Envia o resultado para o cliente
