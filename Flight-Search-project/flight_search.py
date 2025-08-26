import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"



class FlightSearch:
    
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_APP_KEY")
        self._api_secret = os.getenv("AMADEUS_APP_ID")
        self._token = self._get_new_token()
        
    def _get_new_token(self):

        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,       
            "client_secret": self._api_secret,
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url=TOKEN_ENDPOINT, data=body, headers=headers)
        token_data = response.json()

        _token = token_data["access_token"]
        return _token
        
    def get_destination_code(self, city_name):
        
        headers = {"Authorization": f"Bearer {self._token}"}
        code_data = {
            "keyword": city_name,
            "max": 1,
            "include": "AIRPORTS",
        }
        
        response = requests.get(url=IATA_ENDPOINT, params=code_data, headers=headers)
        
        try:
            code = response.json()["data"][0]["iataCode"]
        except KeyError:
            print(f"No value found for {city_name}")
            return "N/A"
        
        return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct = True):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true"if is_direct else "false",
            "currencyCode": "INR",
            "max": "10",
        }
        

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("Response body:", response.text)
            return None

        return response.json()
        
        
    

    