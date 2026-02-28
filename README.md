# 📦 Gestion de Stock - CRUD Flask

[![Déployé sur Replit](https://replit.com/badge/github/Salaheddine0201/gestion-stock-flask)](https://replit.com/@Salaheddine05/gestion-stock-flask)
[![Statut](https://img.shields.io/badge/statut-en%20ligne-brightgreen.svg)](https://gestion-stock-flask--salaheddine05.replit.app)

**Essayez l'application en ligne (100% gratuit, sans carte bancaire)** →  
https://gestion-stock-flask--salaheddine05.replit.app

Application web de gestion de stock avec interface moderne (Bootstrap 5).  
POO Python + Flask + SQLite + HTML/CSS.

![Screenshot](static/images/screenshot.png)

## ✨ Fonctionnalités

- ✅ CRUD complet (Ajouter/Modifier/Supprimer/Rechercher)
- ✅ Stockage persistant avec SQLite (fichier `stock.db` créé automatiquement)
- ✅ Alertes visuelles quand le stock est faible (badge rouge)
- ✅ Calcul automatique de la valeur totale du stock
- ✅ Recherche multi-critères (nom + catégorie)
- ✅ Design responsive (mobile/tablette/PC)

## 🌐 Démo en ligne

Pas besoin d'installer quoi que ce soit — testez directement :

🔗 **https://gestion-stock-flask--salaheddine05.replit.app**

> 💡 *Note : Replit est une plateforme 100% gratuite sans exigence de carte bancaire.  
> Le premier chargement peut prendre 10-15 secondes ("cold start").*

## 🚀 Installation & Lancement (en local)

```bash
# 1. Cloner le dépôt
git clone https://github.com/Salaheddine0201/gestion-stock-flask.git
cd gestion-stock-flask

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