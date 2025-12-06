import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# --- CONFIGURATION ---
load_dotenv()

# Récupération des clés
API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_API_BASE_URL")

# Objectif du défi
TARGET_CAPITAL = 150.0

# --- CONNEXION ALPACA ---
try:
    api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')
except Exception as e:
    print(f"❌ Erreur critique de configuration : {e}")
    exit()

def get_account_data():
    """Récupère les infos réelles du compte Alpaca."""
    try:
        account = api.get_account()
        return account
    except Exception as e:
        print(f"❌ Erreur lors de la récupération du compte : {e}")
        return None

def show_dashboard():
    """Affiche le tableau de bord Road to 150."""
    
    # 1. Infos Marché
    clock = api.get_clock()
    market_status = "🟢 OUVERT" if clock.is_open else "🔴 FERMÉ"
    
    # 2. Infos Compte Réel
    account = get_account_data()
    if not account:
        return

    # Equity = Cash + Valeur des actions détenues
    current_equity = float(account.equity)
    
    # Buying Power = Ce qu'on peut dépenser (souvent 2x ou 4x l'equity en marge, mais on restera prudents)
    buying_power = float(account.buying_power)
    
    # Calculs de progression
    start_cap = 100.0 # On sait que tu as reset à 100
    pnl_total = current_equity - start_cap
    pnl_percent = (pnl_total / start_cap) * 100
    distance_to_target = TARGET_CAPITAL - current_equity

    # 3. Affichage
    print("\n" + "="*50)
    print(f"   🚀 TEACH ALGO TRADE - DASHBOARD RÉEL")
    print("="*50)
    print(f"Marché US        : {market_status}")
    print(f"Heure Serveur    : {clock.timestamp}")
    print("-" * 50)
    print(f"💰 CAPITAL RÉEL (Equity) : ${current_equity:.2f}")
    print(f"💳 POUVOIR D'ACHAT       : ${buying_power:.2f}")
    print("-" * 50)
    print(f"📈 GAIN/PERTE            : {pnl_total:+.2f} $ ({pnl_percent:+.2f}%)")
    print(f"🎯 OBJECTIF 150 $        : Reste {distance_to_target:.2f} $ à gagner")
    print("="*50 + "\n")

if __name__ == "__main__":
    show_dashboard()