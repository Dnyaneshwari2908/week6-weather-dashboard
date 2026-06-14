import requests

from weather_app.config import API_KEY, BASE_URL


def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(
            BASE_URL,
            params=params
        )

        if response.status_code == 200:

            return response.json()

        else:

            return None

    except Exception:

        return None