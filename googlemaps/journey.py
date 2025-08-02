import googlemaps

def get_coordinates(place_name, api_key):
    gmaps = googlemaps.Client(key=api_key)
    geocode = gmaps.geocode(place_name + ", London, UK")
    if geocode:
        location = geocode[0]['geometry']['location']
        return location['lat'], location['lng']
    return None, None

def get_accessible_journey(origin, destination, api_key):
    gmaps = googlemaps.Client(key=api_key)

    # Get coordinates
    origin_lat, origin_lng = get_coordinates(origin, api_key)
    dest_lat, dest_lng = get_coordinates(destination, api_key)

    if not origin_lat or not dest_lat:
        return None, None

    # Get wheelchair-accessible directions
    directions = gmaps.directions(
        origin=(origin_lat, origin_lng),
        destination=(dest_lat, dest_lng),
        mode="transit",
        transit_mode="subway",
        alternatives=False,
        transit_routing_preference="less_walking"
    )

    if not directions:
        return None, None

    # Parse steps
    steps = []
    total_duration = directions[0]['legs'][0]['duration']['text']
    for step in directions[0]['legs'][0]['steps']:
        steps.append(step['html_instructions'].replace("<div", "\n").replace("</div>", "").replace("<b>", "").replace("</b>", ""))

    return steps, total_duration
