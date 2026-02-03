# 📦 Gestion de Stock - CRUD Flask

Application web de gestion de stock avec interface moderne (Bootstrap 5).  
POO Python + Flask + SQLite + HTML/CSS.

![Screenshot](screenshot.png)

## ✨ Fonctionnalités

- ✅ CRUD complet (Ajouter/Modifier/Supprimer/Rechercher)
- ✅ Stockage persistant avec SQLite (fichier `stock.db` créé automatiquement)
- ✅ Alertes visuelles quand le stock est faible
- ✅ Calcul automatique de la valeur totale du stock
- ✅ Design responsive (mobile/tablette/PC)

## 🚀 Installation & Lancement

```bash
# 1. Cloner le dépôt
git clone https://github.com/Salaheddine0201/gestion-stock-flask.git

# 2. Créer un environnement virtuel
python -m venv venv

# Windows :
venv\Scripts\activate

# Mac/Linux :
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
flask run