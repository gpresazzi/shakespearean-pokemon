import uvicorn
from poke_restapi.api.pokemon import get_app


def run():
    uvicorn.run(get_app(), host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()
