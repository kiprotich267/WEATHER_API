from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY_HERE' with your actual OpenWeatherMap API key
API_KEY = '26ad9af02159f5e5b5e653033173cc23'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def home():
    return 'Welcome to the Weather API!'

@app.route('/weather', methods=['GET'])
def get_weather():
    # Get latitude and longitude from query parameters
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({'error': 'Please provide latitude (lat) and longitude (lon) as query parameters.'}), 400

    # Make a request to the OpenWeatherMap API
    try:
        response = requests.get(
            API_URL,
            params={
                'lat': lat,
                'lon': lon,
                'appid': API_KEY,
                'units': 'metric'  # Add units for Celsius
            },
            timeout=10  # Optional: add timeout for better error handling
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()
        return jsonify(weather_data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to fetch weather data.', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)