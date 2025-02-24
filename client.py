import socket
from cryptography.fernet import Fernet


with open("secret.key", "rb") as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

server_ip = "127.0.0.1"
server_port = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

# Authentification
username = input("Login: ")
client.send(username.encode())

password = input("Mot de passe: ")
client.send(password.encode())

auth_response = client.recv(1024).decode()
print(auth_response)

if "Accès refusé" in auth_response:
    client.close()
    exit()

while True:
    message = input("Message : ")
    encrypted_message = cipher_suite.encrypt(message.encode()) 
    client.send(encrypted_message)

    response = client.recv(1024)
    decrypted_response = cipher_suite.decrypt(response).decode()
    print(f"Serveur: {decrypted_response}")
