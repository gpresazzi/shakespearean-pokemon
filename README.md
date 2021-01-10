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
Detailed development documentation for the module `poke_restapi` is available in the related [README.md](poke_restapi/README.md).
It contains information on how to execute the application with all the options and the tests.

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

The application is using the python default logging library. 
By default the application is logging at INFO level and using JSON format, but the developer can use command line arguments to increase the verbosity and change the format:
```bash
  --verbose, -v         Increase the log verbosity
  --disable-json-log, -j
                        Flag to determine if we need to disable json format for the logs.
```

The JSON log is in the format:
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
[TravisCI](https://travis-ci.org/) is used to build the application and run the unit tests.
- [pytest](https://docs.pytest.org/en/stable/) is uses as framework for the unit tests
- [pytest-cov](https://pypi.org/project/pytest-cov/) and [coveralls](https://pypi.org/project/coveralls/) used for code coverage and integration with TravisCI
- [flake8](https://flake8.pycqa.org/en/latest/) for style enforcement

For further detail refer to `.travis.yml`, the TravisCI pipeline is available [here](https://travis-ci.com/github/gpresazzi/shakespearean-pokemon)

### Limitations
The free version of [Shakespeare translator API](https://funtranslations.com/api/shakespeare) is limited with 60 API calls a day with distribution of 5 calls an hour. For that reason the application might return `429` if the user has reached that limit.

### Improvements
There is a lot of space for improvements on the app. Here some examples:
 - [CACHING] Add some caching on the top of the API using Redis, Memcached or DynamoDB
 - [LOGS] Using JSON format for logs to send them to ELK (Elasticsearch, Logstash, and Kibana)  
 - [SCALABILITY] Use Kubernets to scale, manage deployments and manage the cluster 
 - [CI] Add some integrations tests in the CI.
 - .. and many more


*Third party APIs:*
- PokeAPI: https://pokeapi.co/docs/v2
- Shakespeare translator: https://funtranslations.com/api/shakespeare