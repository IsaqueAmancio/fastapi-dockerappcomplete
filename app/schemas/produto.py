from pydantic import validator, BaseModel
import re

class Produtos(BaseModel):
    id: int
    item: str
    peso: float
    numero_caixas: int
    #sector_id = int #FK

    @validator('peso')
    def validate_peso(cls, value):
        if value <= 0:
            raise ValueError('Peso Invalido')
        return value

    @validator('item')
    def validate_item(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('Invalid item')
        return value