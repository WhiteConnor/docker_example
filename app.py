import requests

# Function to fetch data from the SWAPI
def fetch_data(endpoint):
    url = f"https://swapi.dev/api/{endpoint}/"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['results']

# Fetch starships data
starships_data = fetch_data('starships')

# Initialize empty lists to store starship and pilot information
ships = []
pilots = []

# Iterate over each starship and retrieve pilot information
for starship in starships_data:
    ships.append(starship['name'])
    pilots_List = starship['pilots']
    # Iterate over each pilot and append pilot name to pilots
    for pilot_url in pilots_List:
        pilot_response = requests.get(pilot_url)
        pilot_data = pilot_response.json()
        pilots.append(pilot_data['name'])

print("Starships:")
for ship in ships:
    print(" " + ship)
print()

pilots_print = "Pilots:\n"
for pilot in pilots:
    pilots_print += " " + pilot + "\n"
print(pilots_print)

# sudo docker build -t python-docker-app .
# sudo docker run -p 4000:80 python-docker-app
