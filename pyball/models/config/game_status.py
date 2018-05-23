from pyball.models import BaseModel


class GameStatus(BaseModel):
    _fields = {
        'abstractGameState': {'default_value': None, 'field_type': str},
        'codedGameState': {'default_value': None, 'field_type': str},
        'detailedState': {'default_value': None, 'field_type': str},
        'statusCode': {'default_value': None, 'field_type': int},
        'reason': {'default_value': None, 'field_type': int},
        'abstractGameCode': {'default_value': None, 'field_type': int},
    }
