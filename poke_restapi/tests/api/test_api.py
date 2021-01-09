from unittest.mock import Mock
from poke_restapi.api.pokemon import get_app, get_pokemon
from fastapi.testclient import TestClient
from poke_restapi.exceptions import PokemonNotFound, GenericAPIError

client = TestClient(get_app())

def test_get_pokemon_ok(mocker):
    expected_description = "shakespearean description"
    pokemon_name = "my_pokemon"
    
    mock_traslator = Mock()
    mock_traslator.get_shakespearean_description.return_value = expected_description
    mocker.patch("poke_restapi.api.pokemon.Translator", return_value=mock_traslator)
    response = client.get(f"/pokemon/{pokemon_name}")
    
    assert response.status_code == 200
    assert response.json() == {"name": pokemon_name, "description": expected_description}


def test_get_pokemon_not_found(mocker):
    mock_traslator = Mock()
    mock_traslator.get_shakespearean_description.side_effect = PokemonNotFound()
    mocker.patch("poke_restapi.api.pokemon.Translator", return_value=mock_traslator)
    response = client.get(f"/pokemon/name")

    assert response.status_code == 404
    
def test_get_pokemon_catched_internal_error(mocker):
    mock_traslator = Mock()
    mock_traslator.get_shakespearean_description.side_effect = GenericAPIError()
    mocker.patch("poke_restapi.api.pokemon.Translator", return_value=mock_traslator)
    response = client.get(f"/pokemon/name")

    assert response.status_code == 500