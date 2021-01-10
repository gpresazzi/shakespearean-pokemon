
**poke_restapi**

[![Build Status](https://travis-ci.com/gpresazzi/shakespearean-pokemon.svg?branch=main)](https://travis-ci.com/gpresazzi/shakespearean-pokemon)


This is the python module responsible to create the rest API using FastAPI and uvicorn.
There is only one simple API implemented that returns a shakespearean description given a specific pokemon name.

`GET /pokemon/<pokemon_name>` 

Output: 
```
{
  "name":"butterfree",
  "description":"In hurlyburly,  't flaps its wings at high speed to release highly toxic dust into the air. ...
}
```

The verbose pokemon description is composed by the merge of the `flavor_text` of the species where the pokemon belongs to.

### Developer guide
The following steps will help any developer to setup the dev environment to run and test the application.

* 0 - Requirements
   * Python3.8+
   * venv -> `pip3 install virtualenv`

* 1 - Setup the develop environment using env
  * `python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt`
* 2 - Build the application
   * `python setup.py develop`
* 3 - Run the application - run the server [1]
   * `pokemon_server`
* 4 - Test the application
   * `curl http://0.0.0.0:8000/pokemon/butterfree`

[1]: `pokemon_server` can supports the following cli arguments:
```bash
usage: pokemon_server [-h] [--verbose] [--disable-json-log] [--port PORT]

optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v         Increase the log verbosity
  --disable-json-log, -j
                        Flag to determine if we need to disable json format for the logs.
  --port PORT, -p PORT  Application server listening port
```


### Run unit tests
By default the tests will run the coverage

```bash
python -m pytest
```