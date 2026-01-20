import requests
import json
import os
from dotenv import load_dotenv

# load .env
load_dotenv()

# globals
API_KEY = os.getenv('KEY')
BASE_URL = 'https://marvelrivalsapi.com/api/v1'
HEADER = {'x-api-key': API_KEY}

print("Fetching all heroes...")
url = f'{BASE_URL}/heroes'

try:
    response = requests.get(url, headers = HEADER)

    # check if request had 'great success'
    if response.status_code == 200:
        hero_data = response.json()


        # save to file
        with open('heroes.json', 'w', encoding = 'utf-8') as f:
            json.dump(hero_data, f, indent = 2, ensure_ascii = False)

        print('[ok]: data saved to heroes.json')

    else:
        print(f'[error]: {response.status_code}')
        print(response.text)

    
except Exception as e:
    print(f'[error]: {e}')
        
        




