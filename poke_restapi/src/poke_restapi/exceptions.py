class PokemonNotFound(Exception):
    pass

class PokemonInternalError(Exception):
    pass

class GenericAPIError(Exception):
    pass

class TooManyRequestError(Exception):
    pass