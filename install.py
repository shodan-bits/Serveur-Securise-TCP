import os

print("📦 Installation des dépendances...")
os.system("pip install -r requirements.txt")

print("🔑 Génération de la clé AES...")
os.system("python generate_key.py")

print("📂 Création de la base de données...")
os.system("python database_setup.py")

print("✅ Installation terminée ! Vous pouvez maintenant lancer `server.py` et `client.py`.")
