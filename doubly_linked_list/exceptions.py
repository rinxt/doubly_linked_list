from .const import INVALID_OBJECT_TYPE

class InvalidObjectTypeError(TypeError):
    def __init__(self):
        super().__init__(INVALID_OBJECT_TYPE)