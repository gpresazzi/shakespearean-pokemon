import logging
import uvicorn
from poke_restapi.api.pokemon import get_app


# setup loggers, default as DEBUG level
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def run():
    uvicorn.run(get_app(), host="0.0.0.0", port=8000)

