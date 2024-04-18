import requests
from flight_data import FlightData

URL = "https://api.tequila.kiwi.com"
END_POINT = "/locations/query"
API_KEY = "API_KEY"

HEADERS = {
    "apikey": API_KEY
}

LONDON = "LHR"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def get_iata(self, city_name):
        url_params = {
            "term": city_name,
            "location_types": "city",
            "limit": 1
        }
        response = requests.get(url=F"{URL}{END_POINT}", params=url_params, headers=HEADERS)
        response.raise_for_status()
        data = response.json()["locations"][0]["code"]
        return data
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        url_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "one_for_city": 1,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "max_stopovers": 0
        }
        
        response = requests.get(
            url=F"{URL}/v2/search", 
            params=url_params, 
            headers=HEADERS
        )
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        
        print(str(self))
        
        return flight_data
