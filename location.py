import requests

def get_location_coordinates(location_name):
    api_key = "82a3b5fdea28444d9dd9c1a3c26bc179"  # Replace with your OpenCage API key
    base_url = "https://api.opencagedata.com/geocode/v1/json"

    params = {
        "q": location_name,
        "key": api_key,
        "limit": 1
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data['results']:
        location = data['results'][0]['geometry']
        latitude = location['lat']
        longitude = location['lng']
        print(f"📍 Location: {location_name}")
        print(f"🌍 Latitude: {latitude}, Longitude: {longitude}")
    else:
        print(f"⚠️ Error: Could not retrieve location for '{location_name}'.")

# Get user input
location_name = input("Enter a location name: ")
get_location_coordinates(location_name)

