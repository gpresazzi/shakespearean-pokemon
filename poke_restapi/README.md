======
poke_restapi
======

This is thhe python code responsible to create the rest API using FastAPI and uvicorn.
There is only one simple api implemented that given a pokemon name it returns a shakespearean description

`GET /pokemon/<pokemon_name>` 

Output: 
```
{
  "name":"butterfree",
  "description":"In hurlyburly,  't flaps its wings at high speed to release highly toxic dust into the air. ...
}
```

The verbose pokemon description is retrieved merging the `flavor_text` of the species where the pokemon belongs to.

### Developer guide
The following steps will help any developer to setup the dev environment to run and test the application.

* 0 - Requirements
   * Python3.8+
   * venv -> `pip3 install virtualenv`

* 1 - Setup the develop environment using env
```bash
python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt
```
* 2 - Build the application
```bash
python setup.py develop
```
* 3 - Run the application - run the server
```bash
pokemon_server
```

* 4 - Test the application
```bash
curl http://0.0.0.0:8000/pokemon/butterfree
```

### Run unit tests
By default the tests will run the coverage

```bash
python -m pytest
```