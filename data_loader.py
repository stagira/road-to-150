import pandas as pd
from trading import api # On réutilise ta connexion existante
from datetime import datetime, timedelta

def get_historical_data(symbol, timeframe='1Hour', limit=200):
    """
    Récupère les bougies historiques (Open, High, Low, Close).
    timeframe: '1Min', '1Hour', '1Day'
    """
    try:
        # Calcul des dates (Alpaca aime les dates précises)
        # On prend large pour être sûr d'avoir assez de données pour les moyennes
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30) # 30 jours en arrière

        print(f"📥 Récupération des données pour {symbol}...")
        
        # Requête API pour les barres (Bougies)
        bars = api.get_bars(
            symbol,
            timeframe,
            limit=limit,
            adjustment='raw'
        ).df # .df convertit direct la réponse en Pandas DataFrame (Tableau Excel puissant)

        if bars.empty:
            print("❌ Aucune donnée reçue.")
            return None

        # Nettoyage des données
        # On garde l'essentiel : prix de fermeture (close)
        df = bars[['close']].copy()
        
        return df

    except Exception as e:
        print(f"❌ Erreur Data : {e}")
        return None

def calculate_indicators(df):
    """
    Ajoute les Moyennes Mobiles au tableau de données.
    """
    # SMA = Simple Moving Average
    df['SMA_Fast'] = df['close'].rolling(window=9).mean()  # Moyenne courte
    df['SMA_Slow'] = df['close'].rolling(window=21).mean() # Moyenne longue
    
    # On supprime les lignes vides (au début, on ne peut pas calculer la moyenne)
    df.dropna(inplace=True) 
    
    return df

if __name__ == "__main__":
    # Test
    data = get_historical_data("SPY", timeframe='1Hour')
    if data is not None:
        data_with_indicators = calculate_indicators(data)
        print(data_with_indicators.tail(5)) # Affiche les 5 dernières lignes
        print("\n✅ Données chargées et indicateurs calculés !")