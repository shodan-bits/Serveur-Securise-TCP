from cryptography.fernet import Fernet

# Générer une clé AES
key = Fernet.generate_key()

# Enregistrer la clé dans un fichier
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("✅ Clé AES générée et enregistrée dans `secret.key` !")
