import requests

REST_ENDPOINT = "https://opentdb.com/api.php"

def fetch_questions():
    parameters = {
        "amount": 10,
        "type": "boolean"
    }
    
    response = requests.get(url=REST_ENDPOINT, params=parameters)
    response.raise_for_status()
    return response.json()["results"]


question_data = fetch_questions()
