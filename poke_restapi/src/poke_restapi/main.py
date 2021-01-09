import logging
import uvicorn
from poke_restapi.api.pokemon import get_app
from prometheus_fastapi_instrumentator import Instrumentator

# setup loggers, default as DEBUG level
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def run():
    app = get_app()

    Instrumentator().instrument(app).expose(app)
    uvicorn.run(app, host="0.0.0.0", port=8000)

