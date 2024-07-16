import os
from datetime import datetime

from dotenv import load_dotenv
import requests
import googlemaps
from googlemaps import Client


def get_directions(api_key, origin, destination):
    maps_url = "https://routes.googleapis.com/$discovery/rest?version=v2"
    params = {
        "origin": origin,
        "destination": destination,
        "mode": "driving",
        "key": api_key
    }
    response = requests.get(maps_url, params=params)
    if response.status_code == 200:
        directions = response.json()
        print(directions)
        return directions
    else:
        print(f"Error: {response.status_code}, {response.text}")


def get_directions_gmaps(origin, destination):
    load_dotenv()
    API_KEY = os.getenv("GOOGLE_API_KEY")
    gmaps: Client = googlemaps.Client(key=API_KEY)
    now = datetime.now()
    directions_result = gmaps.directions(origin,
                                         destination,
                                         mode="driving",
                                         departure_time=now)
    print(directions_result)

if __name__ == "__main__":

    origin = "Boston, MA"
    destination = "New York, NY"
    # load my api key from .env, DONT commit that lol
    load_dotenv()
    API_KEY = os.getenv("GOOGLE_API_KEY")
    dirs = get_directions_gmaps(API_KEY, origin, destination)
    # print(dirs['geocoded_waypoints'])
