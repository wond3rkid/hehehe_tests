import os
import sqlite3


def create_connection():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    return cursor, conn


def init_db():
    cursor, conn = create_connection()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pokemon_id INTEGER,
        pokemon_name TEXT NOT NULL,
        first_ability TEXT, 
        pic_url TEXT
    )
    """)
    conn.commit()

    cursor.execute("INSERT INTO pokemons (pokemon_id, pokemon_name, first_ability, pic_url) VALUES (?, ?, ?, ?)",
                   (35, 'clefairy', 'cute-charm', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/35.png'))
    conn.commit()

    cursor.execute("INSERT INTO pokemons (pokemon_id, pokemon_name, first_ability, pic_url) VALUES (?, ?, ?, ?)",
                   (25, 'pikachu', 'static', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png'))
    conn.commit()

    cursor.execute("SELECT * FROM pokemons")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

if __name__ == '__main__':
    init_db()