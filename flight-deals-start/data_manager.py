import requests

SHEETY_URL = "https://api.sheety.co/b9efb4077c4782f60a6946f066852b9b/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    
    
    def get_data(self):
        response = requests.get(url=SHEETY_URL)
        response.raise_for_status()
        self.destination_data = response.json()
        return self.destination_data["prices"]
        
    
    def update_data(self, updated_city):
        json_body = {
            "price": updated_city
        }
        
        response = requests.put(url=f"{SHEETY_URL}/{updated_city['id']}", json=json_body)
        response.raise_for_status()
        