import socket,os,sys

numero_port=8080
ma_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
ma_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ma_socket.bind(('',numero_port))
ma_socket.listen(socket.SOMAXCONN)

while 1:

	(nouvelle_connexion,TSAP_from)=ma_socket.accept()

	print("Nouvelle connexion depuis",TSAP_from)
	nouvelle_connexion.sendall(b'\Bienvenue\n')

	ligne=ma_socket.recv(1024
)
	print(ligne)

	nouvelle_connexion.close()

ma_socket.close()