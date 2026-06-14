from weather_app.weather_api import get_weather
from weather_app.weather_parser import parse_weather
from weather_app.weather_display import display_weather


def main():

    print("=" * 40)
    print("WEATHER DASHBOARD")
    print("=" * 40)

    while True:

        city = input(
            "\nEnter city name (or quit): "
        )

        if city.lower() == "quit":

            break

        data = get_weather(city)

        weather = parse_weather(data)

        display_weather(weather)


if __name__ == "__main__":

    main()