import requests

def get_journey(origin_id, destination_id,app_key):
    url = (
        f"https://api.tfl.gov.uk/Journey/JourneyResults/{origin_id}/to/{destination_id}"
        f"?journeyPreference=leastinterchange"
        f"&accessibilityPreference=stepFreeToVehicle"
        f"&app_key={app_key}"
    )
    response = requests.get(url)
    return response.json