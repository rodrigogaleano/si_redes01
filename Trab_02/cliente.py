import socket # Importa o módulo socket

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor está escutando

print('========== CLIENTE ==========')

# ===== Conexão com o servidor =====

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
cliente.connect((HOST, PORT)) # Conecta ao servidor
print('Conectado ao servidor') # Imprime mensagem de conexão

# ===== Envio e recebimento de mensagem =====

mensagem_opcoes = cliente.recv(1024).decode() # Recebe a mensagem de opções
opcao = input(mensagem_opcoes) # Armazena a opção escolhida
cliente.sendall(str.encode(opcao)) # Envia a opção escolhida para o servidor

mensagem_escolha = cliente.recv(1024).decode() # Recebe a mensagem de escolha
print(mensagem_escolha) # Imprime a mensagem de escolha

# ===== Envio dos valores =====

 # Se a opção escolhida for 1
if opcao == '1':
    valor1 = int(input('Digite o primeiro valor: ')) # Armazena o primeiro valor
    valor2 = int(input('Digite o segundo valor: ')) # Armazena o segundo valor
    cliente.sendall(str.encode(str(valor1))) # Envia o primeiro valor para o servidor
    cliente.sendall(str.encode(str(valor2))) # Envia o segundo valor para o servidor

# Se a opção escolhida for 2
elif opcao == '2': 
    string1 = input('Digite a primeira string: ') # Armazena a primeira string
    string2 = input('Digite a segunda string: ') # Armazena a segunda string
    cliente.sendall(str.encode(string1)) # Envia a primeira string para o servidor
    cliente.sendall(str.encode(string2)) # Envia a segunda string para o servidor

reposta = cliente.recv(1024).decode() # Recebe a resposta do servidor

# ===== Impressão da resposta =====
if opcao == '3':
    print('Encerrando conexao')
else:
    print('Resposta do servidor: ' + reposta)
