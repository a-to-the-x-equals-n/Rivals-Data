import json
import os

# Read the heroes.json file
with open('db/heroes.json', 'r') as f:
    heroes = json.load(f)

# Create output directory for individual hero files
output_dir = 'db/.json'
os.makedirs(output_dir, exist_ok=True)

# Split each hero into their own file
for hero in heroes:
    hero_name = hero['name']
    filename = f"{output_dir}/{hero_name}.json"

    with open(filename, 'w') as f:
        json.dump(hero, f, indent=2)

    print(f"Created {filename}")

print(f"\nDone! Split {len(heroes)} heroes into individual files.")
