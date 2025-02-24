import sqlite3
import hashlib

# Connexion à la base de données
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Création de la table utilisateurs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL  -- "admin" ou "user"
    )
''')

# Fonction pour hacher un mot de passe avec SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Ajouter des utilisateurs par défaut
cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", 
               ("admin", hash_password("root"), "admin"))
cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", 
               ("user1", hash_password("1234"), "user"))

conn.commit()
conn.close()

print("✅ Base de données `users.db` créée avec succès !")
