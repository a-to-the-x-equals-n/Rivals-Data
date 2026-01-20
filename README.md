# Marvel Rivals Analytics <!-- omit in toc -->

_A Python project to aggregate and analyze hero data from Marvel Rivals, with plans to calculate DPS statistics._

## Table of Contents <!-- omit in toc -->
- [Intro](#intro)
- [Setup](#setup)
- [Usage](#usage)
- [Database](#database)

## Intro

Some fans of the game created an [API](https://marvelrivalsapi.com/) to pull all of the Hero data, among other uses.

> __NOTE__: You can link your Discord on their [website](https://marvelrivalsapi.com/) to create an account to have access to the API.

## Setup

1. Get an API key from [marvelrivalsapi.com](https://marvelrivalsapi.com/)

2. Create a `.env` file with your API key:
   ```
   KEY=your_api_key_here
   ```

3. Install dependencies:
   ```bash
   pip install requests python-dotenv
   ```

## Usage

Fetch hero data from the API:
```bash
python api.py
```

Split into individual hero files:
```bash
python split_heroes.py
```

Load data into SQLite database:
```bash
python db.py
```

## Database

The SQLite database (`db/.sql/rivals.db`) contains 5 tables:

| Table | Description |
|-------|-------------|
| heroes | Core hero info (name, role, attack_type, etc.) |
| hero_teams | Team affiliations |
| transformations | Hero forms with health/movement stats |
| costumes | Cosmetic variations |
| abilities | Abilities with damage stats in `additional_fields` JSON |

Query example:
```python
import sqlite3
conn = sqlite3.connect('db/.sql/rivals.db')
cur = conn.cursor()

# Get all Duelist heroes
cur.execute('SELECT name FROM heroes WHERE role = "Duelist"')
print(cur.fetchall())
```
