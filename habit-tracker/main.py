import requests
from datetime import datetime

TOKEN = "qwerty12345"
USERNAME = "grewalr"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"  
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


today = datetime.now()
create_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
create_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

# response = requests.post(url=create_pixel_endpoint, json=create_pixel_config, headers=headers)
# print(response.text)


first_march = datetime(year=2024, month=3, day=1).strftime("%Y%m%d")
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{first_march}"
print(update_pixel_endpoint)
update_pixel_config = {
    "quantity": "100"
}

# response = requests.put(headers=headers, json=update_pixel_config, url=update_pixel_endpoint)
# print(response.text)

response = requests.delete(headers=headers, url=update_pixel_endpoint)
