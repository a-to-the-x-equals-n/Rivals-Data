# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Marvel Rivals Analytics is a Python-based data aggregation project that interfaces with the Marvel Rivals API to collect and analyze hero data from the game. The project is in early stages, currently focused on fetching and storing hero information with plans to aggregate DPS statistics.

## Environment Setup

The project requires an API key from [marvelrivalsapi.com](https://marvelrivalsapi.com/). You must link your Discord account on their website to create an account and obtain API access.

The API key must be stored in a `.env` file with the following format:
```
KEY=your_api_key_here
```

Dependencies:
- `requests` - HTTP client for API calls
- `python-dotenv` - Environment variable management
- `json` (stdlib) - JSON data handling

## Running the Project

Execute the main API script to fetch hero data:
```bash
python api.py
```

This will:
1. Load the API key from `.env`
2. Make a GET request to `https://marvelrivalsapi.com/api/v1/heroes`
3. Save the response to `heroes.json` in the current directory

## Architecture

### Data Flow
1. **api.py** - Main entry point that fetches hero data from the Marvel Rivals API and saves it to JSON
2. **data/heroes.json** - Cached hero data containing comprehensive information about each hero including:
   - Basic info (id, name, real_name, role, attack_type)
   - Team affiliations
   - Bio and lore
   - Transformations (with health and movement speed stats)
   - Costumes and abilities

### API Structure
- **Base URL**: `https://marvelrivalsapi.com/api/v1`
- **Authentication**: API key passed via `x-api-key` header
- **Current endpoint**: `/heroes` - Returns array of all hero objects

### Data Model
Hero objects contain:
- Core attributes: id, name, real_name, role (Vanguard/Duelist/Strategist), attack_type, difficulty
- `transformations` array - Different forms with varying stats (e.g., Bruce Banner, Hero Hulk, Monster Hulk)
- `costumes` array - Cosmetic variations
- `team` array - Affiliations (e.g., Avengers, X-Men)

## File Organization

```
/
├── api.py              # Main API client script
├── data/
│   └── heroes.json     # Cached hero data from API
├── brain.md            # Personal notes (gitignored)
├── .env                # API credentials (gitignored)
└── README.md           # Project documentation
```

Note: `brain.md` is gitignored for personal notes and planning.
