import requests
import sys
import time

# Function to fetch data from the SWAPI
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request for URL: {url} threw exception '{e}'")
        sys.exit(1)

# Function to fetch all data with pagination
def fetch_all_data(url):
    all_data = []
    while url:
        time.sleep(1) # prevent rate limiting
        data = fetch_data(url)
        all_data.extend(data['results'])
        url = data.get('next')
    return all_data

# Fetch starships data
starships_data = fetch_all_data("https://swapi.dev/api/starships/")

print("Ships:")
# Iterate through each starship and subsequent pilot
for starship in starships_data:
    pilots_list = starship['pilots']
    print("└─ " + starship['name'])
    for pilot_url in pilots_list:
        pilot_name = fetch_data(pilot_url)['name']
        print("   └─ " + pilot_name)



# sudo docker build -t python-docker-app .
# sudo docker run -p 4000:80 python-docker-app
