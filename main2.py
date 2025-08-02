import os
from dotenv import load_dotenv
from llm.parser import parse_user_query
from googlemaps.journey import get_accessible_journey

load_dotenv()
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
 #gmaps api key

query = input("Ask your travel question: ")
parsed = parse_user_query(query)

if not parsed:
    print("❌ Failed to understand your query.")
    exit()

origin = parsed.get("origin")
destination = parsed.get("destination")
accessibility = parsed.get("accessibility", "stepFreeToVehicle")

print(f"📍 Origin: {origin} → Destination: {destination}")

steps, duration = get_accessible_journey(origin, destination, API_KEY)

if steps:
    print(f"\n♿ Estimated Duration: {duration} minutes")
    for step in steps:
        print(f"- {step}")
else:
    print("⚠️ Could not find an accessible route.")
