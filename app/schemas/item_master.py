from pydantic import BaseModel


class ItemMaster(BaseModel):
    i_ean: str
    i_item: str
    i_factor_volumen: float

    class Config:
        orm_mode = True


class Result(BaseModel):
    message: str
