import requests
import pandas as pd
import numpy as np

# Function to fetch data from the SWAPI
def fetch_data(endpoint):
    url = f"https://swapi.dev/api/{endpoint}/"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['results']

# Fetch starships data
starships_data = fetch_data('starships')

# Initialize an empty list to store starship and pilot information
starships_pilots = []

# Iterate over each starship and retrieve pilot information
for starship in starships_data:
    starship_name = starship['name']
    pilots = starship['pilots']
    pilot_names = []
    for pilot_url in pilots:
        pilot_response = requests.get(pilot_url)
        pilot_data = pilot_response.json()
        pilot_names.append(pilot_data['name'])
    starships_pilots.append({'starship': starship_name, 'pilots': pilot_names})

# Create a DataFrame from the starships and pilots data
df_starships_pilots = pd.DataFrame(starships_pilots)

print(df_starships_pilots.pilots.sum())

# sudo docker build -t python-docker-app .
# sudo docker run -p 4000:80 python-docker-app
