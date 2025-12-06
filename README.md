# Guide: Créer un Excellent README.md

C'est une excellente idée ! Un bon **README.md** est la carte de visite de ton projet. Il te permet de savoir où tu en es et explique à n'importe qui (ou au "toi du futur") comment utiliser ton robot.

Voici un `README.md` complet, structuré et stylé, adapté à notre défi **"Road to 150"**.

Crée un fichier nommé **`README.md`** à la racine de ton projet et colle ce contenu dedans :

````markdown
# 🚀 Road to 150: Défi Algo-Trading Python

Bienvenue dans le projet **Road to 150**.
Ce dépôt contient le code source d'un bot de trading algorithmique construit dans un but pédagogique.

**L'Objectif :** Apprendre à coder un robot de trading en partant de zéro.
**Le Défi :** Faire passer un compte de Paper Trading (virtuel) de **100 $ à 150 $** (+50%) en moins de 3 mois.

---

## 🛠️ Stack Technique

Ce projet utilise une stack Python moderne et robuste :

* **Langage :** Python 3.12+ 🐍
* **Gestionnaire de paquets :** `uv` (par Astral) ⚡
* **Broker & Data :** Alpaca Markets (Paper Trading API) 🦙
* **Librairies Clés :**
    * `alpaca-trade-api` : Connexion au marché.
    * `pandas` : Analyse de données.
    * `python-dotenv` : Sécurité des clés API.

---

## ⚙️ Installation & Configuration

### 1. Pré-requis
Avoir **uv** installé sur votre machine.

## 2. Initialisation
Cloner le projet (ou créer le dossier), puis dans le terminal :

```bash
uv sync
# Ou si c'est la première fois :
# uv init
# uv add alpaca-trade-api pandas python-dotenv
````

## 3. Configuration des Clés (.env)

Créez un fichier `.env` à la racine du projet et ajoutez vos clés **Alpaca Paper Trading** :

```ini
APCA_API_KEY_ID=VOTRE_CLE_PUBLIQUE
APCA_API_SECRET_KEY=VOTRE_CLE_SECRETE
APCA_API_BASE_URL=[https://paper-api.alpaca.markets](https://paper-api.alpaca.markets)
```

⚠️ *Ne jamais partager ce fichier \!*

-----

## 🏃‍♂️ Utilisation

### Tableau de Bord (Dashboard)

Pour voir l'état du compte, le P\&L (Gains/Pertes) et si le marché est ouvert :

```bash
uv run main.py
```

### Trading Manuel (via Code)

Le fichier `trading.py` contient les fonctions d'exécution. Pour les utiliser en mode interactif :

```bash
uv run python
```

Puis dans la console Python :

```python
from trading import buy_stock_in_dollars, close_all_positions, get_positions

# Voir les positions
get_positions()

# Acheter pour 10$ de SPY (S&P 500)
buy_stock_in_dollars("SPY", 10)

# Tout vendre (Panic Button)
close_all_positions()
```

-----

## 📚 Progression du Cursus

* [x] **Module 1 : Initialisation**
  * Setup environnement `uv`.
  * Connexion API Alpaca.
  * Script "Hello World" & Dashboard.
* [x] **Module 2 : Exécution d'Ordres**
  * Achat fractionné (en Dollars).
  * Gestion des positions.
  * Nettoyage du portefeuille.
* [ ] **Module 3 : Stratégies Algorithmiques**
  * Moyennes Mobiles (Golden Cross).
  * RSI & Mean Reversion.
* [ ] **Module 4 : Backtesting**
  * Simulation sur données passées.
* [ ] **Module 5 : Automatisation**
  * Boucle de trading autonome.

-----

## ⚠️ Disclaimer

Ce projet est strictement éducatif et utilise de l'argent fictif (Paper Trading).
Le trading comporte des risques de perte en capital. L'auteur ne fournit aucun conseil financier.

## 💡 Astuce VSCode

Une fois le fichier créé, tu peux faire un clic droit sur l'onglet `README.md` et choisir **"Open Preview"** pour le voir joliment mis en forme avec les émojis et le gras !

Dis-moi quand c'est fait, et on valide ce **Module 2** avec ton premier achat ! 🎯
