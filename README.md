**Shakespearean Pokemon description API**

[![Build Status](https://travis-ci.com/gpresazzi/shakespearean-pokemon.svg?branch=main)](https://travis-ci.com/gpresazzi/shakespearean-pokemon)


This is a simple REST API implemented using Python and FastAPI that returns a shakespearean description for a given pokemon.

### Requirements
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/)

### Instructions
We have 2 options to run the application:
 * using [Docker](https://www.docker.com/) - intended more for production environments
 * locally using python [setuptools](https://pypi.org/project/setuptools/) - intended for development

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

### API Documentation

The Swagger documentation is served at http://0.0.0.0:8000/docs

### Metrics

The server is exposing metrics using a [Prometheus FastAPI Instrumentator](prometheus-fastapi-instrumentator). 
Have a look at :

* http://0.0.0.0:8000/metrics


### Logging 

The application is using the Python default logging library to log the information. 
Only basic configurations have been applied to the logs in this example, it's possible to format them in JSON and store them in a centralized service for further analysis.  

### Continuous integration
[Travis-ci](https://travis-ci.org/) is used to build the application and run the unit tests.

For further detail refer to `.travis.yml`, the TravisCI pipeline is available [here](https://travis-ci.com/github/gpresazzi/shakespearean-pokemon)

### What's next ?
 - Add some integrations tests using TravisCI
 - Add some caching on the API using Redis or DynamoDB
 - Configure the logs using JSON format and send them to ELK (Elasticsearch, Logstash, and Kibana)  


*Third party APIs:*
- PokeAPI: https://pokeapi.co/docs/v2
- Shakespeare translator: https://funtranslations.com/api/shakespeare