from decimal import Decimal
from typing import List
from pydantic import BaseModel


class Movimiento(BaseModel):
    ean: str
    venta_volumen: Decimal

    class Config:
        orm_mode = True


class Result(BaseModel):
    message: str
