from decimal import Decimal
from typing import List
from pydantic import BaseModel, validator
from app.schemas.item_master import ItemMaster


class ItemBase(ItemMaster):
    i_factor_volumen: float


class Movimiento(BaseModel):
    ean: str
    venta_unidades: Decimal
    venta_volumen: Decimal
    item: ItemMaster

    # @validator('c', pre=True, always=True)
    # def make_c(cls, v: str, values: dict):
    #     return values['a'] + values['b']

    class Config:
        orm_mode = True


class MoveResponse(BaseModel):
    ean: str
    item: ItemMaster
