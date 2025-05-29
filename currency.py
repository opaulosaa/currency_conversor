import requests

API_KEY = 'fca_live_gtKomSAIcUDtKdYKUZvHcBkhfLefiXkXj76s1oTN'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "BRL"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Insira um moeda valida")
        return None
    
while True:  
    base = input("Insira a moeda base (s para sair): ").upper()

    if base == "S":
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value:.2f}")
