from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

LONDON = "LON"

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
dm = DataManager()
fs = FlightSearch()
nm = NotificationManager()

destination_data = dm.get_data()

if destination_data[0]["iataCode"] == "":
    for price in destination_data:
        iata_code = fs.get_iata(price["city"])
        price["iataCode"] = iata_code
    
        # Now update the data
        dm.update_data(price)

tomorrow_from_today = datetime.now() + timedelta(days=1)
todays_date = tomorrow_from_today.strftime("%d/%m/%Y")

# 6 months from now
six_month_datetime = tomorrow_from_today + timedelta(weeks=(6*4))

for destination in destination_data:
    iata_code = destination["iataCode"]
    
    flight = fs.check_flights(origin_city_code=LONDON, 
                     destination_city_code=iata_code, 
                     from_time=tomorrow_from_today, 
                     to_time=six_month_datetime
    )
    
    txt_message = f"""
        Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} 
        to {flight.destination_city}-{flight.destination_airport}, 
        from {flight.out_date} to {flight.return_date}.
    """
    
    if flight.price < destination["lowestPrice"]:
        nm.send_sms(
            message=txt_message
        )
