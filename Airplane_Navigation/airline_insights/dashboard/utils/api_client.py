
import requests

def fetch_flight_data(arrival_iata='SYD'):
    try:
        response = requests.get(
            'https://api.aviationstack.com/v1/flights',
            params={
                'access_key': 'd64f446359b14e2f6accfb95d29b87fd',  # Replace with your actual key
                'limit': 100,
                'arr_iata': arrival_iata.split(" - ")[0]  # Extract only IATA code
            },
            timeout=10
        )
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print("API fetch failed:", e)
        return []
