import pytest
from dataclasses import dataclass
from poke_restapi.controller.translator import Translator
from poke_restapi.exceptions import PokemonNotFound, PokemonInternalError, GenericAPIError, TooManyRequestError


@dataclass
class FakeLanguage:
    name: str


@dataclass
class FakeTextEntries:
    language: FakeLanguage
    flavor_text: str


@dataclass
class FakeSpecies:
    name: str
    flavor_text_entries: []


@dataclass
class FakePokemon:
    name: str
    species: FakeSpecies


class FakeResponse:
    def __init__(self, ret_descr, status_code=200):
        self._stored_desc = ret_descr
        self.status_code = status_code

    def json(self):
        return {
            "contents": {
                "translated": self._stored_desc
            }
        }


mock_language = FakeLanguage("en")
mock_desc = FakeTextEntries(mock_language, "simple description for mocked pokemon")
mock_species = FakeSpecies("MockedSpecies", [mock_desc])
mock_pokemon = FakePokemon("PokemonName", mock_species)


class TestTraslator:

    def test_get_shakespearen_description_success(self, mocker):
        expected_description = "simple translated shakespearen description for mocked pokemon"

        mocker.patch("poke_restapi.controller.translator.pokebase.pokemon", return_value=mock_pokemon)
        mocker.patch("poke_restapi.controller.translator.pokebase.pokemon_species", return_value=mock_species)
        mocker.patch("poke_restapi.controller.translator.requests.post",
                     return_value=FakeResponse(expected_description))

        poke_traslator = Translator("PokemonName")
        description = poke_traslator.get_shakespearean_description()
        assert description == expected_description

    def test_get_shakespearen_description_too_many_requests(self, mocker):
        mocker.patch("poke_restapi.controller.translator.pokebase.pokemon", return_value=mock_pokemon)
        mocker.patch("poke_restapi.controller.translator.pokebase.pokemon_species", return_value=mock_species)
        mocker.patch("poke_restapi.controller.translator.requests.post", return_value=FakeResponse("desc", 429))

        poke_traslator = Translator("PokemonName")
        with pytest.raises(TooManyRequestError):
            poke_traslator.get_shakespearean_description()

    def test_get_pokemon_description_connection_error(self, mocker):
        mocker.patch("poke_restapi.controller.translator.pokebase.pokemon", side_effect=ConnectionError())
        poke_traslator = Translator("PokemonName")
        with pytest.raises(GenericAPIError):
            poke_traslator._get_pokemon_description()

    def test_get_pokemon_description_not_found(self, mocker):
        mocker.patch("poke_restapi.controller.translator.pokebase.pokemon", return_value=None)
        poke_traslator = Translator("PokemonName")
        with pytest.raises(PokemonNotFound):
            poke_traslator._get_pokemon_description()

    def test_get_pokemon_description_invalid_species(self, mocker):
        mocker.patch("poke_restapi.controller.translator.pokebase.pokemon",
                     return_value=FakePokemon("PokemonName", None))
        poke_traslator = Translator("PokemonName")
        with pytest.raises(PokemonInternalError):
            poke_traslator._get_pokemon_description()

    def test_translate_description_500_code(self, mocker):
        mocker.patch("poke_restapi.controller.translator.requests.post", return_value=FakeResponse("desc", 500))
        poke_traslator = Translator("PokemonName")
        with pytest.raises(GenericAPIError):
            poke_traslator._translate_description("Test description")

    def test_translate_description_connection_error(self, mocker):
        mocker.patch("poke_restapi.controller.translator.requests.post", side_effect=ConnectionError())
        poke_traslator = Translator("PokemonName")
        with pytest.raises(GenericAPIError):
            poke_traslator._translate_description("Test description")
