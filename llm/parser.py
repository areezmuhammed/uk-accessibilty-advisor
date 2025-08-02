import google.generativeai as genai
import re
import json 
import os 

os.environ["GOOGLE_API_KEY"] =  "Enter your Code , no stealing hahaha"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("models/gemini-2.5-flash")

def parse_user_query(query: str):
    prompt = f"""
You are an assistant helping elderly and disabled users travel across UK public transport.

From this user query, extract:

- origin station (Tube or rail) — **only human-readable names like 'Oxford Circus'**
- destination station — same rule
- accessibility requirement — only one of: "stepFreeToVehicle", "stepFreeToPlatform", or null

Do **NOT** return IDs like '940GZZLUOXC' or 'HUBPAD'. Use plain English station names as people would speak.

Respond with **only** raw JSON:
{{
  "origin": "Oxford Circus",
  "destination": "Paddington",
  "accessibility": "stepFreeToVehicle"
}}

User query: {query}
"""
    response = model.generate_content(prompt)
    raw_output = response.text.strip()

    print("🔍 [GEMINI RAW OUTPUT]:", raw_output)  # Debug print

    # Remove markdown block if present
    cleaned = re.sub(r"```json|```", "", raw_output).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        print("❌ Error parsing Gemini response:", e)
        print("Raw output:", raw_output)
        return None
