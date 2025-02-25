import requests
import json
from database_conn import get_pokemon_count, create_pokemon

def get_pokemons(limit=100):
    print(f"Scraping {limit} Pokemon...")
    
    # Check if we already have Pokemon in the database
    count = get_pokemon_count()
    
    if count >= limit:
        print(f"Database already contains {count} Pokemon.")
        return
    
    # Fetch Pokemon list
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit={limit}")
    pokemon_list = response.json()["results"]
    
    for pokemon in pokemon_list:
        # Fetch detailed Pokemon data
        pokemon_url = pokemon["url"]
        response = requests.get(pokemon_url)
        pokemon_data = response.json()
        
        # Mapping and Insert Pokemon to Database
        mapped_data = mapping_pokemon_data(pokemon_data)
        create_pokemon(mapped_data)
        
        print(f"Get Pokemon #{mapped_data['id']}: {mapped_data['name']}")
    
    print("Pokemon getting completed.")

def mapping_pokemon_data(pokemon_data):
    # Mapping basic data
    pokemon_id = pokemon_data["id"]
    name = pokemon_data["name"]
    height = pokemon_data["height"]
    weight = pokemon_data["weight"]
    
    # Mapping types
    types = [t["type"]["name"] for t in pokemon_data["types"]]
    
    # Mapping abilities 
    abilities_data = get_abilities_data(pokemon_data["abilities"])
    
    # Mapping stats
    stats = {s["stat"]["name"]: s["base_stat"] for s in pokemon_data["stats"]}
    
    # Mapping sprite URL
    sprite_url = pokemon_data["sprites"]["front_default"]
    
    return {
        "id": pokemon_id,
        "name": name,
        "height": height,
        "weight": weight,
        "types": types,
        "abilities": abilities_data,
        "stats": stats,
        "sprite_url": sprite_url
    }

def get_abilities_data(abilities_list):
    abilities_data = []
    
    for ability_entry in abilities_list:
        ability_name = ability_entry["ability"]["name"]
        ability_url = ability_entry["ability"]["url"]
        ability_response = requests.get(ability_url)
        ability_details = ability_response.json()
        
        # Get English description
        description = ""
        for entry in ability_details["effect_entries"]:
            if entry["language"]["name"] == "en":
                description = entry["effect"]
                break
        
        abilities_data.append({
            "name": ability_name,
            "description": description,
            "is_hidden": ability_entry["is_hidden"]
        })
        
    return abilities_data
