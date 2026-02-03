# models.py
import sqlite3


class Produit:
    def __init__(self, id_prod, nom, categorie, quantite, prix, seuil_alerte=5):
        self.id = id_prod
        self.nom = nom
        self.categorie = categorie
        self.quantite = quantite
        self.prix = prix
        self.seuil_alerte = seuil_alerte

    def est_en_alerte(self):
        return self.quantite <= self.seuil_alerte

    def valeur_totale(self):
        return self.quantite * self.prix


class Database:
    def __init__(self, db_name="stock.db"):
        self.db_name = db_name
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def init_db(self):
        """Créer les tables si elles n'existent pas"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Table produits
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                categorie TEXT NOT NULL,
                quantite INTEGER NOT NULL,
                prix REAL NOT NULL,
                seuil_alerte INTEGER DEFAULT 5
            )
        ''')

        conn.commit()
        conn.close()

    # ========== CRUD ==========

    def ajouter_produit(self, nom, categorie, quantite, prix, seuil_alerte=5):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO produits (nom, categorie, quantite, prix, seuil_alerte)
            VALUES (?, ?, ?, ?, ?)
        ''', (nom, categorie, quantite, prix, seuil_alerte))
        conn.commit()
        produit_id = cursor.lastrowid
        conn.close()
        return produit_id

    def obtenir_tous(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produits ORDER BY id DESC')
        rows = cursor.fetchall()
        conn.close()

        produits = []
        for row in rows:
            produits.append(Produit(row[0], row[1], row[2], row[3], row[4], row[5]))
        return produits

    def obtenir_par_id(self, produit_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produits WHERE id = ?', (produit_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Produit(row[0], row[1], row[2], row[3], row[4], row[5])
        return None

    def modifier_produit(self, produit_id, nom, categorie, quantite, prix, seuil_alerte):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE produits
            SET nom = ?, categorie = ?, quantite = ?, prix = ?, seuil_alerte = ?
            WHERE id = ?
        ''', (nom, categorie, quantite, prix, seuil_alerte, produit_id))
        conn.commit()
        conn.close()

    def supprimer_produit(self, produit_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM produits WHERE id = ?', (produit_id,))
        conn.commit()
        conn.close()

    def rechercher(self, nom=None, categorie=None):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = 'SELECT * FROM produits WHERE 1=1'
        params = []

        if nom:
            query += ' AND nom LIKE ?'
            params.append(f'%{nom}%')

        if categorie:
            query += ' AND categorie = ?'
            params.append(categorie)

        query += ' ORDER BY id DESC'

        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()

        produits = []
        for row in rows:
            produits.append(Produit(row[0], row[1], row[2], row[3], row[4], row[5]))
        return produits

    def produits_en_alerte(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produits WHERE quantite <= seuil_alerte')
        rows = cursor.fetchall()
        conn.close()

        produits = []
        for row in rows:
            produits.append(Produit(row[0], row[1], row[2], row[3], row[4], row[5]))
        return produits

    def valeur_stock_total(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(quantite * prix) FROM produits')
        total = cursor.fetchone()[0] or 0
        conn.close()
        return round(total, 2)
