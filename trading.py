import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# Initialisation (comme dans main.py)
load_dotenv()
API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_API_BASE_URL")

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

def buy_stock_in_dollars(symbol, amount_dollars):
    """
    Achète une action (ou une fraction) pour un montant précis en $.
    Type d'ordre : MARKET (achat immédiat).
    """
    try:
        # Vérification basique : a-t-on assez d'argent ?
        account = api.get_account()
        buying_power = float(account.buying_power)
        
        if buying_power < amount_dollars:
            print(f"❌ Fonds insuffisants ! Dispo: {buying_power}$, Requis: {amount_dollars}$")
            return

        print(f"⏳ Envoi de l'ordre d'achat pour {amount_dollars}$ de {symbol}...")
        
        # Envoi de l'ordre fractionné
        order = api.submit_order(
            symbol=symbol,
            notional=amount_dollars, # 'notional' permet de dire "Je veux pour X dollars"
            side='buy',
            type='market',
            time_in_force='day' # L'ordre s'annule ce soir s'il n'est pas passé
        )
        
        print(f"✅ Ordre envoyé ! ID: {order.id}")
        return order

    except Exception as e:
        print(f"❌ Erreur lors de l'achat : {e}")

def close_all_positions():
    """
    PANIC BUTTON : Vend tout le portefeuille.
    Utile à la fin de la journée pour sécuriser les gains/pertes.
    """
    try:
        print("🧹 Nettoyage du portefeuille en cours...")
        
        # 1. D'abord, on annule tous les ordres en attente (Limit, Stop...)
        api.cancel_all_orders()
        print("   ✅ Ordres en attente annulés.")

        # 2. Ensuite, on ferme toutes les positions détenues
        api.close_all_positions()
        print("   ✅ Positions fermées (Ordres de vente au marché envoyés).")
        
    except Exception as e:
        print(f"❌ Erreur lors du nettoyage : {e}")

def get_positions():
    """Affiche ce qu'on possède actuellement."""
    try:
        positions = api.list_positions()
        if not positions:
            print("📭 Portefeuille vide.")
        else:
            print("📋 POSITIONS ACTUELLES :")
            for p in positions:
                print(f"   🔹 {p.symbol} : {p.qty} actions (Valeur: {p.market_value}$)")
    except Exception as e:
        print(f"❌ Erreur lecture positions : {e}")

# Petit test rapide si on lance ce fichier directement
if __name__ == "__main__":
    print("Test des fonctions de trading...")
    get_positions()