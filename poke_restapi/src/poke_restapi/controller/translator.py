import logging
import pokebase
import requests

from poke_restapi.exceptions import (PokemonNotFound, PokemonInternalError, GenericAPIError, TooManyRequestError)


logger = logging.getLogger(__name__)

class Translator:
    
    def __init__(self, pokemon_name: str):
        self.pokemon_name = pokemon_name
    
    def get_shakespearean_description(self) -> str:
        """
        Return the shakespearean description for a given pokemon name
        :return: Pokemon description translated in shakespearean language
        """
        description = self._get_pokemon_description()
        return self._translate_description(description)
    
    def _get_pokemon_description(self) -> str:
        """
        Given a pokemon name it will retrieve the description concatenating the species flavor_texts.
        :return: description of the pokemon, concatenating the species flavor_texts
        """
        description_set = set()
        try:
            pokemon_obj = pokebase.pokemon(self.pokemon_name)
        except Exception as ex:
            logger.error(f"Error while calling get_pokemon. Exception: {ex}")
            raise GenericAPIError("Pokemon API error occurred.")
            
        if not pokemon_obj:
            logger.warning("Invalid pokemon object")
            raise PokemonNotFound()
        
        if not pokemon_obj.species:
            logger.warning("Pokemon species is not valid")
            raise PokemonInternalError()
    
        species = pokebase.pokemon_species(pokemon_obj.species.name)
        for text in species.flavor_text_entries:
            if text.language.name == "en":
                cleaned_description = text.flavor_text.strip().replace("-\n", "").replace("\n", "").replace("\f", " ")
                
                # Deduping species descriptions
                if not cleaned_description in description_set:
                    logger.debug(f"Found valid description: {cleaned_description}")
                description_set.add(cleaned_description)
    
        return ' '.join(str(s) for s in description_set)
        
    def _translate_description(self, description: str) -> str:
        """
        Translate the shakespearen description from a plain description
        :param description: 
        :return: 
        """
        try:
            r = requests.post("https://api.funtranslations.com/translate/shakespeare.json", data={"text": description})
        except ConnectionError as ex:
            logger.error(f"Unknown exception occurred while calling translate API. {ex}")
            raise GenericAPIError()
    
        if r.status_code == 429:
            logger.error("Reached max number of call per hour.")
            raise TooManyRequestError()
        if r.status_code != 200:
            logger.debug("Translation call succeeded.")
            raise GenericAPIError()
    
        data = r.json()
        return data["contents"]["translated"]
