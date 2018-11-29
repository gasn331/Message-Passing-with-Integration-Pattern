from socket import *
from threading import *
import datetime

def aceitar_conexoes():
	while 1:
		client, addr = serverSocket.accept()
		print(str(addr) + ' conectado')
		client.send(bytes('Ola! Digite o seu nome: '))
		ends[client] = addr
		Thread(target=cliente, args=(client,)).start()
		
def cliente(client):
	
	nome = client.recv(1024)
	clients[client] = nome
	#-----------------------dead queue check
	if nome in dead_message_queue.keys():
		#print(dead_message_queue)
		for ms in dead_message_queue[nome]:
			client.send(bytes(ms))
		dead_message_queue[nome] = []
		
	else:
		dead_message_queue[nome] = []
	print(dead_message_queue)
	#----------------------------------------
	clients_list[nome] = True
	now = datetime.datetime.now()
	formatted_date = now.strftime('%d-%m-%Y %H:%M')
	greeting = nome + ' se juntou ao chat ' + formatted_date
	sendall(greeting, client)
	flag = True
	while flag:
		message = client.recv(1024)
		now = datetime.datetime.now()
		formatted_date = now.strftime('%d-%m-%Y %H:%M')
		if message == '{q}':
			client.send(bytes('{q}'))
			clients_list[nome] = False
			client.close()
			del clients[client]
			goodbye = nome + ' saiu ' + formatted_date
			sendall(goodbye, client)
			break
		else:
			sendall(str(clients[client]) + ' ' + formatted_date + ': ' + message, client)
			
			
def sendall(message, client):
	for cl in clients:
		if cl != client:
			cl.send(bytes(message))
	#clients off
	for nome in clients_list:
		if clients_list[nome] == False:
			dead_message_queue[nome].append(message + '\n')
			
serverPort = 12004
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
clients = {}
clients_list = {}
dead_message_queue = {}
ends = {}


if __name__ == "__main__":
	serverSocket.listen(200)
	print ('Servidor online')
	th = Thread(target=aceitar_conexoes)
	th.start()
	th.join()
	serverSocket.close()



