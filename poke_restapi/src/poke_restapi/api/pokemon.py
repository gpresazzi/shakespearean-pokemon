import logging
from poke_restapi.model.pokemon import Pokemon
from poke_restapi.exceptions import PokemonNotFound, PokemonInternalError, GenericAPIError, TooManyRequestError
from poke_restapi.controller.translator import Translator
from fastapi import FastAPI, HTTPException

logger = logging.getLogger(__name__)
app = FastAPI()

@app.get("/pokemon/{pokemon_name}", response_model=Pokemon)
async def get_shakespearean_pokemon_description(pokemon_name: str):
    
    try:
        poke_translator = Translator(pokemon_name)
        description = poke_translator.get_shakespearean_description()
        logger.info("Request for pokemon: %s succeeded.", pokemon_name)
    except PokemonNotFound as ex:
        raise HTTPException(status_code=404, detail=f"Item #{pokemon_name} not found")
    except TooManyRequestError:
        raise HTTPException(status_code=429, detail=f"Translation APIs request limit exceeded.")
    except (GenericAPIError, PokemonInternalError):
        raise HTTPException(status_code=500, 
                            detail=f"Internal error while retrieving translation for pokemon: `{pokemon_name}`")
    
    ret_poke = Pokemon(name=pokemon_name, description=description)
    return ret_poke


def get_app() -> FastAPI:
    return app