from tfl.journey import get_journey

origin = "1000175"  # Paddington
destination = "1000173"  # Oxford Circus
app_key = "6e3c2ce67d484aa0b87611695cf7b1dc"

data = get_journey(origin,destination,app_key)
print(data)