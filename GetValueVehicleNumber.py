import requests
from pprint import pprint

API_TOKEN = "8b88fdaa4ba0c9a6bdc1c5cc853f9b89facb4aa5"

def Work(imagePath):
    with open(imagePath, 'rb') as fp:
        response = requests.post(
            'https://platerecognizer.com/api/plate-reader/',
            files=dict(upload=fp),
            headers={'Authorization': 'Token ' + API_TOKEN})
    #pprint(response.json())
    carNumber = response.json()['results'][0]['plate']
    # print("carNumber = ", carNumber)
    return carNumber
