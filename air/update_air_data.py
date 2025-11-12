import csv
from datetime import datetime

# Sample data
routes = [
    {
        "origin_city": "London",
        "origin_country": "England",
        "origin_lat": 51.5074,
        "origin_lon": -0.1278,
        "destination_city": "Paris",
        "destination_country": "France",
        "destination_lat": 48.8566,
        "destination_lon": 2.3522,
        "origin_airport_name": "Heathrow Airport",
        "origin_airport_iata": "LHR",
        "destination_airport_name": "Charles de Gaulle",
        "destination_airport_iata": "CDG",
        "airline_name": "British Airways",
        "airline_iata": "BA",
        "flight_duration_min": 75,
        "distance_km": 344,
        "frequency_per_day": 18,
        "last_updated": datetime.utcnow().isoformat()
    },
    {
        "origin_city": "Madrid",
        "origin_country": "Spain",
        "origin_lat": 40.4168,
        "origin_lon": -3.7038,
        "destination_city": "Barcelona",
        "destination_country": "Spain",
        "destination_lat": 41.3851,
        "destination_lon": 2.1734,
        "origin_airport_name": "Adolfo Suárez Madrid–Barajas Airport",
        "origin_airport_iata": "MAD",
        "destination_airport_name": "Barcelona–El Prat Airport",
        "destination_airport_iata": "BCN",
        "airline_name": "Iberia",
        "airline_iata": "IB",
        "flight_duration_min": 85,
        "distance_km": 504,
        "frequency_per_day": 12,
        "last_updated": datetime.utcnow().isoformat()
    }
]

# Write to CSV
with open("air/air_routes.csv", mode="w", newline="", encoding="utf-8") as csvfile:
    fieldnames = list(routes[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for route in routes:
        writer.writerow(route)

print("air_routes.csv updated successfully.")
