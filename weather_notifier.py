import requests

# === CONFIG ===
BOT_TOKEN = '7609212380:AAEZ3auUEuhOMgHdbOwPrRWJbEJqvR_-XQo'
CHAT_ID = '8032942142'
CITY = 'Gaza'
WEATHER_API_KEY = 'dfc76fc743db10fcbf4970f458174fa3'
# ==============

def get_temperature():
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={WEATHER_API_KEY}&units=metric"
    )
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    if 'main' not in data or 'temp' not in data['main']:
        raise RuntimeError("Temperature information missing from API response")
    return data['main']['temp']

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

if __name__ == "__main__":
    temp = get_temperature()
    message = f"🌤️ Good morning!\nToday’s temperature in {CITY} is {temp}°C."
    send_telegram_message(message)
