import requests


def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/AZN"
    response = requests.get(url)

    # Eğer yanıt başarılı değilse hata verelim
    if response.status_code != 200:
        print(f"API hatası: {response.status_code}")
        return {"USD": "Veri Yok", "EUR": "Veri Yok", "TRY": "Veri Yok", "RUB": "Veri Yok"}

    # JSON verisini alalım ve terminale yazdıralım
    data = response.json()
    print("API Yanıtı:", data)  # Terminale veriyi yazdır

    # Veriyi ters çevirerek doğru oranı elde edelim
    rates = {
        "USD": round(1 / data["rates"].get("USD", 1), 4),
        "EUR": round(1 / data["rates"].get("EUR", 1), 4),
        "TRY": round(1 / data["rates"].get("TRY", 1), 4),
        "RUB": round(1 / data["rates"].get("RUB", 1), 4)
    }

    print("Kurlar:", rates)  # Bu kurları da yazdıralım
    return rates


import requests

def get_exchange_rate(currency):
    api_key = "6f4f0e0fc95dfeb6ca8ed11d"  # Sizin API açarınız
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates']['AZN']  # AZN üçün məzənnə
    return None
