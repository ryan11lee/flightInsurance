import requests
from main import *


class FlightAndPassengerInformation:
    '''Get The Passenger Information via User Input'''

    def __init__(self):
        self.flightNumber = input("Enter Flight Number: ")
        self.customerFirstName = input("Enter Passenger First Name: ")
        self.customerLastName = input("Enter Passenger Last Name: ")

        self.delayURL = "https://aerodatabox.p.rapidapi.com/flights/" + \
                        self.flightNumber + "/delays"
        self.headers = {
            'x-rapidapi-key': "xxxx",
            'x-rapidapi-host': "aerodatabox.p.rapidapi.com"
        }
        self.request = requests.request("GET", self.delayURL, headers=self.headers)
        self.response = self.request.text
        print(self.response)

    # delayURL = "https://aerodatabox.p.rapidapi.com/flights/WN2630/delays"
