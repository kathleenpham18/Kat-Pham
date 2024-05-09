# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kathleen Pham
# kathlep3@uci.edu
# 79281883

import urllib
import json
from WebAPI import WebAPI


class OpenWeather(WebAPI):

    def __init__(self, zipcode='92697', ccode='US'):
        self.zipcode = zipcode
        self.country_code = ccode
        self.apikey = None
        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None
        self.longitude = None
        self.latitude = None
        self.description = None
        self.humidity = None
        self.sunset = None
        self.city = None


    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.

        '''
        if not self.apikey:
            raise ValueError("API key is not set. Please set the API key using the set_apikey method.")
        
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.country_code}&appid={self.apikey}&units=metric"

        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read())
            self.description = data['weather'][0]['description']
            trans = self.description
            return trans

        except urllib.error.URLError as e:
            raise ConnectionError("Internet Connection failed.") from e
            
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("404 Error. URL could not be found.", e)
            elif e.code == 503:
                raise ConnectionError("503 Error. Server overloaded.")


    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        trans = self.load_data()
        message_trans = message.replace("@weather", trans)
        return message_trans
