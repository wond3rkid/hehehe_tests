import random
import sqlite3

import requests


def get_random_pokemon_info():
    p_id = random.randint(0, 1302)
    url = f'https://pokeapi.co/api/v2/pokemon/{p_id}'
    response = requests.get(url)

    data = response.json()
    return {
        'name': data['name'],
        'abilities': [ability['ability']['name'] for ability in data['abilities']],
    }


def get_pokemon_info(p_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{p_id}'
    response = requests.get(url)

    data = response.json()
    return {
        'name': data['name'],
        'abilities': [ability['ability']['name'] for ability in data['abilities']],
    }


def calculate_len_random_pokemon_abilities():
    pokemon = get_random_pokemon_info()
    return len(pokemon['abilities'])


def calculate_len_pokemon_name():
    pokemon = get_random_pokemon_info()
    return len(pokemon['name'])


def get_pokemon_from_db(p_id):
    conn = sqlite3.connect("pokemon/methods/example.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemons WHERE pokemon_id = ?", (p_id,))
    pokemon = cursor.fetchone()
    conn.close()
    return pokemon
