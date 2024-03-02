import requests
import pyttsx3

if __name__ == '__main__':
    while True:
        city = input('Enter city name: ')
        try:
            API_key = 'bb4641d61412dc320bb0bf47c338e87e'

            fetched_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=imperial')

            # Getting only required fields from 'fetched_data':
            weather_condition = fetched_data.json()['weather'][0]['main']

            temp_fahrenheit = fetched_data.json()['main']['temp']
            temp_celsius = (temp_fahrenheit - 32) * 5 / 9  # convert temperature into celsius:
            rounded_temp_celsius = round(temp_celsius, 2)  # Rounds to 2 decimal places:

            wind_speed_mph = fetched_data.json()['wind']['speed']
            wind_speed_kph = wind_speed_mph * 1.60934           # convert speed from 'mph' to 'kph':
            rounded_wind_speed_kph = round(wind_speed_kph, 2)   # Rounds to 2 decimal places:

            humidity = fetched_data.json()['main']['humidity']

            # showing outputs:
            print(f'Weather condition in {city}: {weather_condition}')
            print(f'Temperature is: {rounded_temp_celsius}°C')
            print(f'Wind speed is: {rounded_wind_speed_kph} kph')
            print(f'Humidity is: {humidity}')

            # speach functionality:
            speach = pyttsx3.init()
            speach.setProperty('rate', 150)
            speach.say(f'currently there is {weather_condition} in {city}')
            speach.runAndWait()

            user_input = input("Do you want to check for another city? 'yes' OR 'no': ").lower()
            if user_input == 'no':
                print("Program exit.")
                break

        # exception handling:
        except requests.exceptions.RequestException as e:   # network error:
            print(f"Error: {e}")
        except KeyError:                                    # invalid entry:
            print("Invalid Entry, please try again.")
