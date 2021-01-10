import sys
import logging
import uvicorn
import argparse
from poke_restapi.api.pokemon import get_app
from prometheus_fastapi_instrumentator import Instrumentator
from pythonjsonlogger import jsonlogger


def setup_logging(log_level: int, disable_json: bool) -> None:
    """
    Set log format and verbosity
    :param log_level: verbosity log level
    :param disable_json: Flag to determine whether the logs has to be in json or plain format
    :return: NA
    """
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    if disable_json:
        logging.basicConfig(level=log_level, format=log_format)
        logger = logging.getLogger(__name__)
    else:
        logger = logging.getLogger()
        logger.setLevel(log_level)
        json_handler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter(fmt=log_format)
        json_handler.setFormatter(formatter)
        logger.addHandler(json_handler)

    logger.info("Initializing pokemon server using verbosity level: %s", log_level)


def init():
    """
    Initialize application arguments and logs and return parsed input args
    :return: parsed arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count', default=0, help='Increase the log verbosity')
    parser.add_argument('--disable-json-log', '-j', dest='disable_json', action='store_true', default=False,
                        help='Flag to determine if we need to disable json format for the logs.')
    parser.add_argument('--port', '-p', dest='port', default=8000, type=int, required=False,
                        help='Application server listening port')

    args_namespace = parser.parse_args(sys.argv[1:])

    # setup loggers, default as INFO level
    log_level = logging.DEBUG if args_namespace.verbose else logging.INFO
    setup_logging(log_level, args_namespace.disable_json)

    return args_namespace


def run():
    args = init()
    app = get_app()

    Instrumentator().instrument(app).expose(app)
    uvicorn.run(app, host="0.0.0.0", port=args.port)
