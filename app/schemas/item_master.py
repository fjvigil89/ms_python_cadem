from typing import List, Union
from pydantic import BaseModel
# from .movimiento import Movimiento


class ItemMaster(BaseModel):
    i_ean: str
    i_item: str
    i_factor_volumen: float
    # movimientos: List[Movimiento] = []

    class Config:
        orm_mode = True


class Response(BaseModel):
    message: str
