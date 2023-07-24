import requests

API_ENDPOINT = "https://samples.openweathermap.org/data/2.5/forecast/hourly"

def get_weather_data(location):
    params = {
        'q': location,
        'appid': 'b6907d289e10d714a6e88b30761fae22',
    }

    try:
        response = requests.get(API_ENDPOINT, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data from the API:", e)
        return None

def get_temperature():
    date = input("Enter date (YYYY-MM-DD): ")
    weather_data = get_weather_data('London,us')
    if weather_data:
        for forecast in weather_data['list']:
            if date in forecast['dt_txt']:
                temperature = forecast['main']['temp']
                print("Temperature is", temperature, "°C")
                return
        print("No data available for the input date.")

def get_wind_speed():
    date = input("Enter date (YYYY-MM-DD): ")
    weather_data = get_weather_data('London,us')
    if weather_data:
        for forecast in weather_data['list']:
            if date in forecast['dt_txt']:
                wind_speed = forecast['wind']['speed']
                print("Wind Speed is", wind_speed, "m/s")
                return
        print("No data available for the input date.")

def get_pressure():
    date = input("Enter date (YYYY-MM-DD): ")
    weather_data = get_weather_data('London,us')
    if weather_data:
        for forecast in weather_data['list']:
            if date in forecast['dt_txt']:
                pressure = forecast['main']['pressure']
                print("Pressure is", pressure, "hPa")
                return
        print("No data available for the input date.")

def main():
    while True:
        print("\n1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            get_temperature()
        elif choice == '2':
            get_wind_speed()
        elif choice == '3':
            get_pressure()
        elif choice == '0':
            print("Terminating the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
