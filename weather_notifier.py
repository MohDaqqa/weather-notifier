import requests

# === CONFIG ===
BOT_TOKEN = '7609212380:AAEZ3auUEuhOMgHdbOwPrRWJbEJqvR_-XQo'
CHAT_ID = '8032942142'
CITY = 'Gaza'
WEATHER_API_KEY = 'dfc76fc743db10fcbf4970f458174fa3'
# ==============

def get_temperature():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    data = response.json()
    return data['main']['temp']

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

if __name__ == "__main__":
    temp = get_temperature()
    message = f"🌤️ Good morning!\nToday’s temperature in {CITY} is {temp}°C."
    send_telegram_message(message)
