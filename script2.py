import requests
import json

# Define the API endpoint
api_endpoint = "http://localhost:8080/api/v1/play/round"

# Define your session ID and API ID
session_id = "8bcd68e4-9936-46b4-a598-09f099dfa9d1"
api_key = "7bcd6334-bc2e-4cbf-b9d4-61cb9e868869"

# Load movements data from file
with open('movements1.txt', 'r') as file:
    movements_data = json.load(file)

# Iterate over each day from 0 to 42
for day in range(43):
    # Extract movements for the current day
    day_movements = next((item['movements'] for item in movements_data if item['day'] == day), [])

    # Prepare the data to be sent in the POST request
    data = {
        "day": day,
        "movements": day_movements
    }
    
    # Define headers including session ID and API ID
    headers = {
        "SESSION-ID": session_id,
        "API-KEY": api_key
    }
    
    # Make the POST request
    response = requests.post(api_endpoint, json=data, headers=headers)
    
    # Check the response status
    if response.status_code == 200:
        print(f"Successfully posted data for day {day}")
        # Print only the totalKpis from the response data
        try:
            response_data = response.json()
            total_kpis = response_data.get("totalKpis", {})
            print("Total KPIs:", total_kpis)
        except ValueError:
            print("Response is not in JSON format")
    else:
        print(f"Failed to post data for day {day}: {response.status_code}")
        print("Response content:", response.text)