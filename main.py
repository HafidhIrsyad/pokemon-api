import json
from flask import Flask
from database_conn import init_db
from pokemon import get_pokemons


app = Flask(__name__)

if __name__ == "__main__":
    # Init database
    init_db()
    
    # Get Data Pokemon From Pokemon APi
    get_pokemons(limit=100)
    
    # Run App
    app.run(debug=True)