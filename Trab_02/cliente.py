import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000        # Porta que o Servidor esta

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket

cliente.connect((HOST, PORT)) # Conecta ao servidor
print('Conectado ao servidor')

mensagem_opcoes = cliente.recv(1024).decode()
opcao = input(mensagem_opcoes)
cliente.sendall(str.encode(opcao))

mensagem_escolha = cliente.recv(1024).decode()
print(mensagem_escolha)

if opcao == '1':
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    cliente.sendall(str.encode(str(valor1)))
    cliente.sendall(str.encode(str(valor2)))
elif opcao == '2':
    string1 = input('Digite a primeira string: ')
    string2 = input('Digite a segunda string: ')
    cliente.sendall(str.encode(string1))
    cliente.sendall(str.encode(string2))

reposta = cliente.recv(1024).decode()
print(reposta)

# opcao = int(input('Digite 1 para somar, 2 para concatenar e 3 para sair: '))
# cliente.send(str(opcao).encode()) # Envia a opção para o servidor
