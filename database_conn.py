import sqlite3
import json
import os

# Database configuration
DB_PATH = "pokemon.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        height INTEGER,
        weight INTEGER,
        types TEXT,
        abilities TEXT,
        stats TEXT,
        moves TEXT,
        evolution_chain TEXT,
        characteristics TEXT,
        sprite_url TEXT
    )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized.")

def create_pokemon(pokemon_data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT OR REPLACE INTO pokemon (id, name, height, weight, types, abilities, stats, sprite_url)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        pokemon_data["id"], 
        pokemon_data["name"], 
        pokemon_data["height"], 
        pokemon_data["weight"], 
        json.dumps(pokemon_data["types"]), 
        json.dumps(pokemon_data["abilities"]), 
        json.dumps(pokemon_data["stats"]), 
        pokemon_data["sprite_url"]
    ))
    
    conn.commit()
    conn.close()

def get_pokemon_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM pokemon")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_list_pokemons(page=1, limit=10):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Calculate offset
    offset = (page - 1) * limit
    
    # Get total count
    cursor.execute("SELECT COUNT(*) FROM pokemon")
    total = cursor.fetchone()[0]
    
    # Get paginated list
    cursor.execute("SELECT id, name, height, weight, types, abilities, stats, sprite_url FROM pokemon LIMIT ? OFFSET ?", (limit, offset))
    pokemon_list = cursor.fetchall()
    
    conn.close()
    return pokemon_list, total

def get_pokemon_by_id(pokemon_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM pokemon WHERE id = ?", (pokemon_id,))
    pokemon = cursor.fetchone()
    
    conn.close()
    return dict(pokemon) if pokemon else None