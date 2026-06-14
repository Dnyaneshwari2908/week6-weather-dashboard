def display_weather(weather):

    if not weather:

        print("Weather data not available.")
        return

    print("\nWEATHER REPORT")
    print("-" * 30)

    print(f"City: {weather['city']}")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Condition: {weather['condition']}")