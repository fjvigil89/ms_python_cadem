from typing import List
from unicodedata import numeric
from pydantic import BaseModel
from . import item_master


class Movimiento(BaseModel):
    ean: str
    venta_volumen: numeric

    class Config:
        orm_mode = True


class Result(BaseModel):
    message: str
