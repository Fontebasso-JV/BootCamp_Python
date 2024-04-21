import requests
from db import SessionLocal, engine, Base
from models import Pokemon
from schema import PokemonSchame

Base.metadata.create_all(bind=engine)

def pegar_pokemon(id: int):

    URL = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(URL)
    data = response.json()
    data_types = data['types']

    types_list = []

    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchame(name=data['name'], type=types)

def add_pokemon_to_db(pokemon_schema: PokemonSchame) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon= Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon