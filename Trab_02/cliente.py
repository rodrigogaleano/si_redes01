import socket

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor está escutando

print('+-----------------------------------------------------+')
print('|                                                     |')
print('|                       CLIENTE                       |')
print('|                                                     |')
print('+-----------------------------------------------------+\n')

# ===== Conexão com o servidor =====
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
cliente.connect((HOST, PORT)) # Conecta ao servidor
print('Conexão estabelecida com', HOST, 'na porta', PORT, '!\n')

# ===== Recebe e informa as opções na tela para escolha =====

opcoes = cliente.recv(1024).decode() # Recebe a mensagem de opções

opcao = input(opcoes) # Cliente escolhe a opção
while opcao not in ['1', '2', '3']:
    opcao = input('Opção inválida, tente novamente:')

cliente.sendall(str.encode(opcao)) # Envia a opção escolhida para o servidor

mensagem_escolha = cliente.recv(1024).decode() # Recebe a mensagem de escolha
print(mensagem_escolha) # Imprime a mensagem de escolha

# ===== Informa os valores =====

# Se a opção escolhida for 1
if opcao == '1':

    #Repete até o cliente informar um valor válido
    while True:
        try:
            valor1 = int(input("Informe o primeiro valor: "))
            valor2 = int(input("Informe o segundo valor: "))
            break
        except:
            print("\nValor inválido, por favor informe um valor inteiro!\n")
            continue

    cliente.sendall(str.encode(str(valor1))) # Envia o primeiro valor para o servidor
    cliente.sendall(str.encode(str(valor2))) # Envia o segundo valor para o servidor

# Se a opção escolhida for 2
elif opcao == '2': 
    string1 = input('Digite a primeira string: ') # Armazena a primeira string
    string2 = input('Digite a segunda string: ') # Armazena a segunda string
    cliente.sendall(str.encode(string1)) # Envia a primeira string para o servidor
    cliente.sendall(str.encode(string2)) # Envia a segunda string para o servidor

resposta = cliente.recv(1024).decode() # Recebe a mensagem de resposta
print('\nResultado:', resposta) # Imprime a mensagem de resposta