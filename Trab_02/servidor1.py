#Servidor de disponibilidade de serviços
import socket # Importa o módulo socket

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5000 
PORT_SOMA = 5001 #Porta do servidor de soma
PORT_CONCATENACAO = 5002 #Porta do servidor de concatenação

print('========== SERVIDOR DE DISPONIBILIDADE DE SERVIÇOS ==========')

# ===== Cria o socket do servidor =====

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
servidor.bind((HOST, PORT)) # Conecta ao servidor
servidor.listen(1) # Aceita conexoes de um cliente
print('Servidor pronto para conexoes') 

conexao_cliente, endereco = servidor.accept() # Aceita conexoes de um cliente
print('Conexao estabelecida com', endereco) # Imprime mensagem de conexão


# ===== Recebe a opção do cliente =====
mensagem_opcoes = 'Digite 1 para somar, 2 para concatenar e 3 para sair: ' # Mensagem de opções
conexao_cliente.send(mensagem_opcoes.encode()) # Envia a opção para o servidor

opcao = int(conexao_cliente.recv(1024).decode()) # Recebe a opção do cliente
print('Opcao recebida: ', opcao)
mensagem_escolha = 'Você escolheu a opção: ' + str(opcao)
conexao_cliente.send(mensagem_escolha.encode()) # Envia a opção para o servidor


# ===== Repassa para o servidor responsável =====

# Soma
if opcao == 1:

    #Recebe os valores do cliente para somar
    valor1 = int(conexao_cliente.recv(1024).decode()) 
    print ('Valor1:', valor1)
    valor2 = int(conexao_cliente.recv(1024).decode())
    print ('Valor2:', valor2)

    valores = str(valor1) + '+' + str(valor2)

    #Repassa para o servidor de soma
    print('Repassando para o servidor de soma')
    conexao_soma = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
    conexao_soma.connect((HOST, PORT_SOMA)) # Conecta ao servidor

    conexao_soma.send(str.encode(valores)) # Envia a opção para o servidor
    
    soma = int(conexao_soma.recv(1024).decode()) # Recebe a opção do cliente
    print('Soma:', soma)
    conexao_soma.close()
    conexao_cliente.send(str(soma).encode()) # Envia a opção para o servidor

# Concatenacao
elif opcao == 2:
    #Recebe os valores do cliente para concatenar
    string1 = conexao_cliente.recv(1024).decode()
    string2 = conexao_cliente.recv(1024).decode()
    strings = str(string1) + '+' + str(string2)

    #Repassa para o servidor de concatenação
    print('Repassando para o servidor de concatenacao')
    conexao_concatenacao = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
    conexao_concatenacao.connect((HOST, PORT_CONCATENACAO)) # Conecta ao servidor

    conexao_concatenacao.send(str.encode(strings)) # Envia a opção para o servidor

    concatenacao = conexao_concatenacao.recv(1024).decode() # Recebe a opção do cliente
    print('Concatenacao: ', concatenacao)
    conexao_concatenacao.close()
    conexao_cliente.send(concatenacao.encode()) # Envia a opção para o servidor

# Sair
elif opcao == 3:
    #fechar
    conexao_cliente.close()