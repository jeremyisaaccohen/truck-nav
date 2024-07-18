import os
from dotenv import load_dotenv
import requests


def get_directions(origin, destination):
    load_dotenv()
    API_KEY = os.getenv("GOOGLE_API_KEY")
    maps_url = "https://routes.googleapis.com/directions/v2:computeRoutes"

    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': API_KEY,
        'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.legs.steps.navigationInstruction,routes.legs.steps.localizedValues'
    }
    payload = {
        "origin": {"address": origin},
        "destination": {"address": destination},
        "travelMode": "DRIVE",
        # "routingPreference": "TRAFFIC_AWARE",
        # "routeModifiers": {
        #     "avoidTolls": False,
        #     "avoidHighways": False,
        #     "avoidFerries": False
        # },
        # "key": API_KEY,
        "computeAlternativeRoutes": True
    }
    response = requests.post(maps_url, headers=headers, json=payload)
    if response.status_code == 200:
        directions = response.json()
        print(directions)
        return directions
    else:
        print(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    origin = "Nyack, NY 10960"
    destination = "Valley Cottage, NY 10989"
    dirs = get_directions(origin, destination)
