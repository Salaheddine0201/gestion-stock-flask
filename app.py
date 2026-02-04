# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from models import Database
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
db = Database()


# ========== Routes ==========

@app.route('/')
def index():
    """Page principale - liste tous les produits"""
    produits = db.obtenir_tous()
    total_valeur = db.valeur_stock_total()
    alertes = db.produits_en_alerte()
    return render_template('index.html', produits=produits, total_valeur=total_valeur, alertes=alertes)


@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    """Formulaire d'ajout"""
    if request.method == 'POST':
        nom = request.form['nom']
        categorie = request.form['categorie']
        quantite = int(request.form['quantite'])
        prix = float(request.form['prix'])
        seuil_alerte = int(request.form.get('seuil_alerte', 5))

        db.ajouter_produit(nom, categorie, quantite, prix, seuil_alerte)
        flash(f'✅ Produit "{nom}" ajouté avec succès !', 'success')
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/modifier/<int:id>', methods=['GET', 'POST'])
def modifier(id):
    """Modifier un produit"""
    produit = db.obtenir_par_id(id)

    if not produit:
        flash('❌ Produit non trouvé', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        nom = request.form['nom']
        categorie = request.form['categorie']
        quantite = int(request.form['quantite'])
        prix = float(request.form['prix'])
        seuil_alerte = int(request.form.get('seuil_alerte', 5))

        db.modifier_produit(id, nom, categorie, quantite, prix, seuil_alerte)
        flash(f'✅ Produit "{nom}" modifié avec succès !', 'success')
        return redirect(url_for('index'))

    return render_template('edit.html', produit=produit)


@app.route('/supprimer/<int:id>')
def supprimer(id):
    """Supprimer un produit"""
    produit = db.obtenir_par_id(id)
    if produit:
        db.supprimer_produit(id)
        flash(f'🗑️ Produit "{produit.nom}" supprimé', 'warning')
    return redirect(url_for('index'))


@app.route('/rechercher', methods=['POST'])
def rechercher():
    """Recherche par nom ou catégorie"""
    nom = request.form.get('recherche_nom')
    categorie = request.form.get('recherche_categorie')

    produits = db.rechercher(nom=nom, categorie=categorie)
    total_valeur = sum(p.valeur_totale() for p in produits)

    flash(f'🔍 {len(produits)} résultat(s) trouvé(s)', 'info')
    return render_template('index.html', produits=produits, total_valeur=total_valeur, alertes=[])


# ========== Lancement ==========

if __name__ == '__main__':
    app.run(debug=True)
