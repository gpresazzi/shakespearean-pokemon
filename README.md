**Shakespearean Pokemon description API**

[![Build Status](https://travis-ci.com/gpresazzi/shakespearean-pokemon.svg?branch=main)](https://travis-ci.com/gpresazzi/shakespearean-pokemon)
![Coverage Status](https://coveralls.io/repos/github/gpresazzi/shakespearean-pokemon/badge.svg?branch=main)

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
cd shakespearean-pokemon
docker build -t shakespearean-server . && docker run -d -p 8000:8000 shakespearean-server
```

#### 2 - Run locally
Refer to the Python module [README](poke_restapi/README.md)

Test the API
 * `curl http://0.0.0.0:8000/pokemon/charizard`

---

### API Documentation

The Swagger documentation is served at http://0.0.0.0:8000/docs

### Metrics

The server is exposing metrics using a [Prometheus FastAPI Instrumentator](prometheus-fastapi-instrumentator). 
Have a look at :

* http://0.0.0.0:8000/metrics


### Logging 

The application is using the Python default logging library to log the information. 
by default the application is logging at INFO level and JSON format, but a developer can use command line arguments to add more verbosity and change the format:
```bash
  --verbose, -v         Increase the log verbosity
  --disable-json-log, -j
                        Flag to determine if we need to disable json format for the logs.
```

The loggers have the format:
```json
{
 "asctime": <DATATIME>, 
 "name": <module_name>, 
 "levelname": <LOG_LEVEL>, 
 "message": <MESSAGE>
}
```

You can see the log stream on the docker container running `docker attach [containerid]`

### Continuous integration
[Travis-ci](https://travis-ci.org/) is used to build the application and run the unit tests.

For further detail refer to `.travis.yml`, the TravisCI pipeline is available [here](https://travis-ci.com/github/gpresazzi/shakespearean-pokemon)

### What's next ?
There is a lot of space for improvements on the app. Here some examples:
 - Add some caching on the API using Redis, Memcached or DynamoDB
 - Using JSON format we could send them to ELK (Elasticsearch, Logstash, and Kibana)  
 - Add some integrations tests in the CI.
 

*Third party APIs:*
- PokeAPI: https://pokeapi.co/docs/v2
- Shakespeare translator: https://funtranslations.com/api/shakespeare