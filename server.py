import socket
import threading
import sqlite3
import hashlib
from cryptography.fernet import Fernet
from flask import Flask, render_template_string

# Charger la clé AES
with open("secret.key", "rb") as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

# Stockage des logs et des clients connectés
logs = []
clients = {}

# Interface Web pour afficher les logs en direct
app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
        <h2>Logs du Serveur</h2>
        <ul>
            {% for log in logs %}
                <li>{{ log }}</li>
            {% endfor %}
        </ul>
    """, logs=logs)

def start_web():
    app.run(host="0.0.0.0", port=5000, debug=False)

# Vérification des identifiants avec SHA-256
def check_credentials(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = cursor.fetchone()
    conn.close()
    return user[0] if user else None

# Gestion d'un client
def handle_client(client_socket, address):
    global logs
    print(f"[+] Nouveau client : {address}")
    logs.append(f"Connexion de {address}")

    # Authentification
    client_socket.send("Login: ".encode())
    username = client_socket.recv(1024).decode().strip()

    client_socket.send("Mot de passe: ".encode())
    password = client_socket.recv(1024).decode().strip()

    role = check_credentials(username, password)

    if role:
        client_socket.send(f"Authentification réussie ! Rôle: {role}\n".encode())
        logs.append(f"Utilisateur {username} connecté (Rôle: {role})")
        clients[username] = client_socket
    else:
        client_socket.send("Accès refusé.\n".encode())
        logs.append(f"Échec de connexion pour {username}")
        client_socket.close()
        return

    while True:
        try:
            encrypted_data = client_socket.recv(1024)
            if not encrypted_data:
                break

            message = cipher_suite.decrypt(encrypted_data).decode()
            print(f"[{username}] {message}")
            logs.append(f"{username}: {message}")

            # Commandes Admin
            if role == "admin":
                if message.startswith("/kick "):
                    user_to_kick = message.split(" ")[1]
                    if user_to_kick in clients:
                        clients[user_to_kick].send("Vous avez été expulsé !".encode())
                        clients[user_to_kick].close()
                        del clients[user_to_kick]
                        logs.append(f"{user_to_kick} a été expulsé par {username}")
                elif message == "/list":
                    client_socket.send(f"Utilisateurs connectés: {', '.join(clients.keys())}".encode())
                elif message == "/shutdown":
                    logs.append("Fermeture du serveur demandée par l'admin")
                    client_socket.send("Arrêt du serveur...".encode())
                    exit()

            response = f"Reçu: {message}"
            encrypted_response = cipher_suite.encrypt(response.encode())
            client_socket.send(encrypted_response)

        except:
            break

    print(f"[-] Déconnexion de {username}")
    logs.append(f"Déconnexion de {username}")
    del clients[username]
    client_socket.close()

# Démarrer le serveur
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(10)

    print("[*] Serveur en attente de connexions...")

    while True:
        client, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()

# Lancer le serveur et l'interface web en parallèle
threading.Thread(target=start_web, daemon=True).start()
start_server()
