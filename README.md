# Pokémon API

A Python application that scrapes Pokémon data from the PokéAPI, stores it in a local SQLite database, and build REST API to access the data pokemons.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pokemon-api.git
   cd pokemon-api
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the application with:

```bash
python main_app.py
```
## API Endpoints

### Get All Pokémon (Paginated)

```
GET /api/pokemon
```

Parameters:
- `page` (optional): Page number (default: 1)
- `limit` (optional): Number of items per page (default: 10)

Example:
```bash
curl -X GET "http://localhost:5000/api/pokemon?page=1&limit=20" -H "Accept: application/vnd.api+json"
```

### Get Specific Pokémon

```
GET /api/pokemon/{id}
```

Example:
```bash
curl -X GET "http://localhost:5000/api/pokemon/25" -H "Accept: application/vnd.api+json"
```
