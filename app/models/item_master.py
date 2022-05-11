from unicodedata import numeric
from sqlalchemy import Column, Float, ForeignKey, String

from app.conexion.database import Base

class ItemMaster(Base):
    __tablename__ = "item_master"

    i_ean = Column(String(20), primary_key=True, index=True)
    i_item = Column(String(100))
    i_factor_volumen = Column(Float)
    
    def __init__(self, i_ean: str, i_item: str, i_factor_volumen: float):
        self.i_ean = i_ean
        self.i_item = i_item
        self.i_factor_volumen = i_factor_volumen


    def __repr__(self) -> str:
        return f"<ItemMaster {self.i_ean}, {self.i_item}>"

# La relación entre la item master y la movimiento es movimiento.ean = item_master.i_ean