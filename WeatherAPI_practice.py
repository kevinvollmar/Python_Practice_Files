import requests

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    print(response.status_code)
    data = response.json
    print(data) # Prints JSON data

    if response.status_code == 200:
        data = response.json()

        if data['cod'] != '404':
            # Extract weather information
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']

            # Print the wather information
            print(f'Weather in {city}:')
            print(f'Temperature: {temperature} K')
            print(f'Humidity: {humidity}%')
            print(f'Description: {description}')
        else:
            print('City not found!')
    else:
        print('An error occurred while fetching weather data!')

# Replace 'YOUR API KEY' and 'YOUR CITY' with your actual API key and city
api_key = input('YOUR API KEY:')
city = input('YOUR CITY:')

get_weather(api_key, city)