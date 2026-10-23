from flask import Flask, render_template, request
import yfinance as yf
import numpy as np
from scipy.optimize import minimize
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)
def calculer_variance_portefeuille(poids, matrice_cov):
    return np.dot(poids.T, np.dot(matrice_cov, poids))
@app.route('/', methods=['GET', 'POST'])


def accueil():
    if request.method == 'POST':
        liste_noms = request.form.getlist('nom_actif[]')
        nombre_actifs=len(liste_noms)
        if nombre_actifs < 2:
            return render_template('index.html',
                                   error_msg="Veuillez entrer au moins 2 actions pour optimiser un portefeuille.")

        donnees = yf.download(liste_noms, period="max")['Close']
        donnees = donnees.tail(20)
        if donnees.empty or (len(liste_noms) > 1 and donnees.dropna(axis=1).shape[1] < len(liste_noms)):
            # On renvoie la page avec un message d'erreur explicite
            return render_template('index.html',
                                   error_msg="Un ou plusieurs tickers sont invalides. Vérifiez les symboles (ex: AAPL, MSFT).")

        # Si tout est bon, on continue les calculs normalement
        rendements_quotidiens = donnees.pct_change().dropna()
        # 2. On calcule les rendements moyens annuels (on multiplie par 252, le nombre de jours de bourse par an)
        rendements_annuels = rendements_quotidiens.mean() * 252

        # 3. On calcule la matrice de covariance annuelle
        matrice_cov_annuelle = rendements_quotidiens.cov() * 252
        n = len(liste_noms)
        poids_initiaux = [1.0 / n] * n
        limites = [(0, 1) for _ in range(n)]
        contraintes = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})

        # 4. Lancement de l'optimiseur
        resultat = minimize(calculer_variance_portefeuille, poids_initiaux,
                            args=(matrice_cov_annuelle,),
                            method='SLSQP', bounds=limites, constraints=contraintes)

        poids_ideaux = resultat.x

        resultats_visuels={}
        for nom, poids in zip(liste_noms, poids_ideaux):
            resultats_visuels[nom] = round(poids * 100, 2)
        fig = px.pie(
            names=list(resultats_visuels.keys()),
            values=list(resultats_visuels.values()),
            hole=0.4  # Cette option crée le trou au milieu pour faire un "Donut Chart"
        )

            # 2. On transforme ce graphique en un bloc HTML/JavaScript lisible par le navigateur
        graph_html = pio.to_html(
                fig,
                full_html=False,
                include_plotlyjs='cdn',
                config={
                    'displayModeBar': True,  # On affiche la barre d'outils
                    'displaylogo': False,  # On cache le logo Plotly
                    # On liste ici tous les boutons qu'on veut ENLEVER (on ne garde que l'appareil photo)
                    'modeBarButtonsToRemove': [
                        'zoom2d', 'pan2d', 'select2d', 'lasso2d',
                        'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d'
                    ]
                }
            )
        return render_template('index.html', resultats=resultats_visuels, graph_html=graph_html)
    return render_template('index.html', resultats=None, graph_html=None)

if __name__ == '__main__':
    app.run(debug=True)

