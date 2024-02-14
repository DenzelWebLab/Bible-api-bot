import requests

from config import api_key

code_to_smile = {
            "Ясно": "☀️",
            "Хмарно": "☁️",
            "Дощ": "🌧",
            "Дощик": "🌦",
            "Гроза": "⛈",
            "Сніг": "❄️",
            "Туман": "😶‍🌫️"
        }


class Weather:
    def __init__(self):
        self.api_key = api_key
        self.url = 'https://api.openweathermap.org'

    def get_description(self, city: str):
        url = self.url + f"/data/2.5/weather?q={city}&lang={'ua'}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        main = data['weather'][0]['description']
        name_country = data['sys']['country']
        name_city = data['name']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        temp = data['main']['temp']
        feels = data['main']['feels_like']

        weather_text = f"Місто: {name_city}\n"
        weather_text += f"Країна: {name_country}\n"
        weather_text += f'Опис: {main.capitalize()}\n'
        weather_text += f"Температура повітря: {temp}°C\n"
        weather_text += f"Відчувається як: {feels}°C\n"
        weather_text += f"Швидкість вітру: {wind}м/с\n"
        weather_text += f"Вологість повітря: {humidity}%"
        return f'{weather_text}\nГарного дня :)'

