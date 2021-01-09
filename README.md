**Shakespearean Pokemon description API**

[![Build Status](https://travis-ci.com/gpresazzi/shakespearean-pokemon.svg?branch=main)](https://travis-ci.com/gpresazzi/shakespearean-pokemon)


This is a simple REST API implemented using Python and FastAPI that returns a shakespearean description for a given pokemon.

### Requirements
* Git
* Docker

### Instructions

#### 1 - Run using docker

```bash
git clone https://github.com/gpresazzi/shakespearean-pokemon.git
```

```bash
docker build -t shakespearean-server . && docker run -d -p 8000:8000 shakespearean-server
```

Test the API
 * `curl http://0.0.0.0:8000/pokemon/charizard `

#### 2 - Run locally
Refer to the Python module [README](poke_restapi/README.md)

---
*Third party APIs:*
- PokeAPI: https://pokeapi.co/docs/v2
- Shakespeare translator: https://funtranslations.com/api/shakespeare