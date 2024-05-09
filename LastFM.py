# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kathleen Pham
# kathlep3@uci.edu
# 79281883
# openweather.py


import urllib
import json
from WebAPI import *


class LastFM(WebAPI):
    '''
    Holds methods for LastFm.
    '''
    def __init__(self, artist="The_Weeknd"):
        self.artist = artist


    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.

        '''
        if not self.apikey:
            raise ValueError("API key is not set. Please set the API key using the set_apikey method.")

        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={self.artist}&api_key={self.apikey}&format=json"

        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read())

            self.first_track = data['toptracks']['track'][0]['name']
            return self.first_track

        except urllib.error.URLError as e:
            raise ConnectionError("Internet Connection failed.") from e

        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("404 Error. URL could not be found.", e)
            if e.code == 503:
                print("503 Error. Server overloaded.", e)


    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        trans = self.load_data()
        message_trans = message.replace("@lastfm", trans)
        return message_trans
