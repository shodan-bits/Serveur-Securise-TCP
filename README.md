
---

## 📄 **README.md (Guide d'utilisation complet)**  
```md
# 🔥 Serveur TCP Sécurisé avec Authentification & Commandes Admin 🔥

## 📌 Description  
Ce projet implémente un **serveur TCP sécurisé** avec les fonctionnalités suivantes :  
✅ **Authentification des utilisateurs (SQLite + SHA-256)**  
✅ **Chiffrement AES des messages** (protection contre les interceptions)  
✅ **Gestion multi-clients** (connexion simultanée de plusieurs utilisateurs)  
✅ **Commandes Admin** (`/kick`, `/list`, `/shutdown`)  
✅ **Interface Web Flask** pour voir les logs en direct  

---

## 📌 **1️⃣ Installation Automatique**  
Si tu veux **tout installer d'un coup**, exécute :  
```bash
python install.py
```
✅ Cette commande va automatiquement :  
- 📦 **Installer les dépendances** (`cryptography`, `flask`, etc.)  
- 🔑 **Générer la clé de chiffrement AES** (`secret.key`)  
- 📂 **Créer la base de données SQLite** (`users.db`)  

---

## 📌 **2️⃣ Installation Manuelle**  
Si tu préfères **installer chaque étape séparément** :  

1️⃣ **Installer les dépendances**  
```bash
pip install -r requirements.txt
```

2️⃣ **Générer la clé AES pour le chiffrement**  
```bash
python generate_key.py
```

3️⃣ **Créer la base de données SQLite**  
```bash
python database_setup.py
```

---

## 📌 **3️⃣ Démarrer le Serveur**  
Exécute cette commande pour **lancer le serveur** :  
```bash
python server.py
```
✅ Le serveur écoute sur le **port 5555** et accepte plusieurs connexions simultanées.  

📡 **Surveillance en direct** : ouvre un navigateur et accède à :  
```
http://127.0.0.1:5000
```
✅ Cet affichage permet de **voir toutes les connexions et messages échangés** en temps réel.  

---

## 📌 **4️⃣ Lancer un Client**  
Pour **se connecter au serveur**, exécute :  
```bash
python client.py
```
✅ Il te demandera **un login et un mot de passe** (stockés dans `users.db`).  

---

## 📌 **5️⃣ Afficher les Utilisateurs Enregistrés**  
Pour voir les utilisateurs existants dans la base SQLite, exécute :  
```bash
sqlite3 users.db "SELECT * FROM users;"
```
✅ Exemple de sortie :  
```
1 | admin  | 5e88489... | admin
2 | user1  | 123456...  | user
```
🔹 **Le mot de passe est stocké sous forme de hachage SHA-256 pour plus de sécurité.**  

---

## 📌 **6️⃣ Commandes Admin Disponibles**  
Si tu es connecté en tant qu’**admin**, tu peux exécuter ces commandes spéciales :  

| **Commande**  | **Description** |
|--------------|----------------|
| `/kick user1` | Expulse un utilisateur du serveur |
| `/list` | Liste les utilisateurs actuellement connectés |
| `/shutdown` | Arrête complètement le serveur |

---

## 📌 **7️⃣ Convertir le Client en Exécutable (.exe ou .app)**  
Si tu veux **transformer `client.py` en application exécutable**, exécute cette commande :  
```bash
pyinstaller --onefile --noconsole client.py
```
✅ L'exécutable sera disponible dans le dossier `dist/`.

---

## 📌 **8️⃣ Désinstaller le Projet**  
Si tu veux **supprimer toutes les dépendances installées**, exécute :  
```bash
pip uninstall -r requirements.txt -y
```
✅ Cela supprimera **toutes les bibliothèques installées**.

---

## 📌 **9️⃣ Sécurité & Bonnes Pratiques**  
⚠ **Ne partage jamais le fichier `secret.key`**, car il permet de chiffrer et déchiffrer les messages.  
⚠ **Change régulièrement les mots de passe des utilisateurs** pour éviter les accès non autorisés.  
⚠ **Active un pare-feu** et bloque les connexions non souhaitées sur le **port 5555**.

---

## 📌 **🔗 Ressources Utiles**  
📚 [Documentation SQLite](https://www.sqlite.org/docs.html)  
📚 [Documentation Cryptography](https://cryptography.io/en/latest/)  
📚 [Documentation Flask](https://flask.palletsprojects.com/en/2.0.x/)  

---



---

