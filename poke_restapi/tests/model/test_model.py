from poke_restapi.model.pokemon import Pokemon


def test_pokemon_ok():
    expected_name = "poke1_name"
    expected_desc = "poke1_description"
    
    poke1 = Pokemon(name=expected_name, description=expected_desc)
    
    assert poke1.name == expected_name
    assert poke1.description == expected_desc
    