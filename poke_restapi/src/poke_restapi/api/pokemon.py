from fastapi import FastAPI
from poke_restapi.model.pokemon import Pokemon

app = FastAPI()

@app.get("/pokemon/", response_model=Pokemon)
async def get_pokemon(pokemon_name: str):
    ret_poke = Pokemon(name=pokemon_name, description="random poke description")
    return ret_poke


def get_app():
    return app