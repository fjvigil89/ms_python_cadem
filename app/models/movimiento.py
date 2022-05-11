from unicodedata import numeric
from sqlalchemy import Column, Float, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from app.conexion.database import Base

class Movimiento(Base):
    __tablename__ = "movimiento"

    ean = Column(String(100))
    venta_volumen = Column(Numeric(10, 5), primary_key=True, index=True)

    def __init__(self, ean: str, venta_volumen: numeric):
        self.ean = ean
        self.venta_volumen = venta_volumen        

    def __repr__(self) -> str:
        return f"<Movimiento {self.ean}, {self.venta_volumen}>"
