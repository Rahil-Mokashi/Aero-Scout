import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth


SHEETY_ENDPOINT = "https://api.sheety.co/25fddd07859d2666aebf5de29336aa50/flightDeals/prices"
SHEETY_ENDPOINT_U = "https://api.sheety.co/25fddd07859d2666aebf5de29336aa50/flightDeals/users"


load_dotenv()


class DataManager:
    
    def __init__(self):
        self._user = os.getenv("SHEETY_USER")
        self._pass = os.getenv("SHEETY_PASS")
        self._authorization = HTTPBasicAuth(self._user, self._pass)
        self.sheets_data = {}
        self.customer_data = {}
        
    #This class is responsible for talking to the Google Sheet.
    def get_customer_emails(self):
        response = requests.get(url=SHEETY_ENDPOINT_U, auth=self._authorization)
        user_data = response.json()
        
        self.customer_data = user_data["users"]
        return self.customer_data
    
    def getting_sheets_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.sheets_data = data["prices"]
        
        return self.sheets_data
    
    def update_sheets_data(self):
        for city in self.sheets_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)